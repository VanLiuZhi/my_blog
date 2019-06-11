#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@time: 2019-05-28 23:06
"""

import datetime
import os
import random
import sys
import time
from itertools import groupby

import django
from concurrent.futures import ThreadPoolExecutor
from pykafka import KafkaClient


def retries(max_retries_count=10, conn_failed_wait_time=1):
    """
    获取连接对象失败时，进行重试
    :param max_retries_count: 最大重试次数
    :param conn_failed_wait_time: 连接失败等待时间
    :return:
    """

    def func(f):
        def _func(*args, **kwargs):
            conn_status = True
            conn_retries_count = 0  # 记录连接重试次数
            while conn_status and conn_retries_count <= max_retries_count:
                try:
                    res = f(*args, **kwargs)
                    conn_status = False
                    return res
                except BaseException as e:
                    print e
                    time.sleep(conn_failed_wait_time)
                    conn_retries_count += 1
                    print "retries count {}".format(conn_retries_count)
                    continue
            print "Link failed, Maximum number of retries exceeded"

        return _func

    return func


def run_time(f):
    def _func(*args, **kwargs):
        start = time.time()
        f(*args, **kwargs)
        print time.time() - start

    return _func


class KafkaConn(object):
    """连接kafka操作"""

    def __init__(self, host="", timeout=10000, DEBUG=False):
        self.host = host
        self.client = KafkaClient(hosts=self.host, socket_timeout_ms=timeout)
        self.DEBUG = DEBUG

    def _get_topic(self, topic_name):
        return self.client.topics[topic_name.encode()]

    @retries()
    def get_topics(self, topic_list):
        """获取topic实例列表"""
        return [self._get_topic(topic) for topic in topic_list]

    def simple_consumer(self, topic):
        """
        消费者指定消费
        """
        topic = self.client.topics[topic.encode()]
        partitions = topic.partitions
        consumer = topic.get_simple_consumer(b"simple_consumer_udal_group", auto_commit_enable=False,
                                             partitions=[partitions[0]])
        if self.DEBUG:
            print topic.latest_available_offsets()
            print consumer.fetch_offsets()
            consumer.reset_offsets([(partitions[0], 0)])
        _list = []
        for message in consumer:
            if message is not None:
                value = consumer.consume().value
                print value


class KafkaInsertDB(object):
    """kafka数据插入数据库"""

    STATISTICAL_INTERVAL = 60 * 60 * 24  # 统计时间间隔为一天，单位秒

    VALUE_TYPE = {''}

    def __init__(self, topic_instance):
        self.topic_instance = topic_instance
        self.start_time = None
        self.data_dict = {}
        self.DEBUG = False

    @staticmethod
    def time_str_change(str_time):
        time_str_format = "%Y-%m-%d %X.%f" if len(str_time) > 19 else "%Y-%m-%d %X"
        return datetime.datetime.strptime(str_time, time_str_format)

    @retries()
    def get_consumer(self):
        partitions = self.topic_instance.partitions
        consumer = self.topic_instance.get_simple_consumer(
            b"{name}_group_test1".format(name=self.topic_instance.name),
            auto_commit_enable=True, partitions=[partitions[0]],
        )
        return consumer

    @staticmethod
    def change_upper(v):
        value = {
            key.upper(): value
            for key, value in v.items()
        }
        return value

    @run_time
    def get_data_and_insert(self):
        """读取kafka数据到data_dict中，到达设置的时间间隔时停止消费，然后插入数据"""
        try:
            consumer = self.get_consumer()
            if self.DEBUG:
                print self.topic_instance.latest_available_offsets()
                print consumer.fetch_offsets()
            key_dict = {}
            for message in consumer:
                if message is not None:
                    value = message.value
                    try:
                        value = eval(value)
                        value = {
                            key.upper(): value
                            for key, value in value.items()
                        }
                    except BaseException as e:
                        print e
                        value = None
                    if value:
                        if not self.start_time:
                            self.start_time = self.time_str_change(value.get("COLLECTTIME"))
                        if self.start_time and self._time_interval_is_up2(
                                self.time_str_change(value.get("COLLECTTIME"))):
                            break
                        key = "%s-%s" % (value.get("COMPKEY"), value.get("METRICCODE"))
                        collect_time = KafkaInsertDB.time_str_change(value.get("COLLECTTIME"))
                        if key not in key_dict:
                            _tmp = dict()
                            _tmp['sid'] = "ES" + str(int(time.time())) + 'R' + str(random.randint(100000, 999999))
                            _tmp['ccompkey'] = value.get("COMPKEY")
                            _tmp['mmonth'] = collect_time.month
                            _tmp['ddate'] = collect_time.strftime("%Y-%m-%d")
                            _tmp['metriccode'] = value.get("METRICCODE")
                            _tmp['datacount'] = KafkaInsertDB.update_datacount({}, collect_time.hour)
                            _tmp['status'] = value.get('METRICTYPE', 0)  # compkey 使用
                            key_dict[key] = _tmp
                        else:
                            _dict = key_dict[key]
                            d = _dict['datacount']
                            d.update({collect_time.hour: d.get(collect_time.hour, 0) + 1})
                            _dict['datacount'] = d
            print key_dict
            self.data_dict = key_dict
            consumer.stop()
            # self.data_insert_DB()
        except BaseException as e:
            print e

    @run_time
    def get_data_and_insert2(self):
        """读取kafka数据到data_list中，到达设置的时间间隔时停止消费，然后插入数据"""
        try:
            consumer = self.get_consumer()
            if self.DEBUG:
                print self.topic_instance.latest_available_offsets()
                print consumer.fetch_offsets()
            key_dict = {}
            end_flag = False
            for message in consumer:
                if end_flag:
                    break
                if message is not None:
                    value = message.value
                    value_type = ''
                    try:
                        value = eval(value)
                        value_type = 'dict' if isinstance(value, dict) else 'list'
                        # 转换所有key为大写
                        if value_type == 'dict':
                            value = {
                                key.upper(): value
                                for key, value in value.items()
                            }
                            value = [value]
                        if value_type == 'list':
                            value = [KafkaInsertDB.change_upper(item) for item in value]
                    except BaseException as e:
                        print e
                        value = None
                    if value:
                        for item in value:
                            if not self.start_time:
                                self.start_time = self.time_str_change(item.get("COLLECTTIME"))
                            if self.start_time and self._time_interval_is_up(
                                    self.time_str_change(item.get("COLLECTTIME"))):
                                end_flag = True
                                break
                            key = "%s-%s" % (item.get("COMPKEY"), item.get("METRICCODE"))
                            collect_time = KafkaInsertDB.time_str_change(item.get("COLLECTTIME"))
                            if key not in key_dict:
                                _tmp = dict()
                                _tmp['sid'] = "ES" + str(int(time.time())) + 'R' + str(random.randint(100000, 999999))
                                _tmp['ccompkey'] = item.get("COMPKEY")
                                _tmp['mmonth'] = collect_time.month
                                _tmp['ddate'] = collect_time.strftime("%Y-%m-%d")
                                _tmp['metriccode'] = item.get("METRICCODE")
                                _tmp['datacount'] = KafkaInsertDB.update_datacount({}, collect_time.hour)
                                key_dict[key] = _tmp
                            else:
                                _dict = key_dict[key]
                                b = _dict['datacount']
                                b.update({collect_time.hour: b.get(collect_time.hour, 0) + 1})
                                _dict['datacount'] = b
            print key_dict
            consumer.stop()
            # self.data_insert_DB()
        except BaseException as e:
            print e

    @staticmethod
    def update_datacount(data, hours):
        """更新数据统计"""
        # if not isinstance(data, dict):
        #     data = eval(data)
        _tmp = {hours: data.get(hours, 0) + 1}
        data.update(_tmp)
        return data

    def _time_interval_is_up(self, now_time):
        """判断时间间隔是否达到"""
        res = (now_time - self.start_time).seconds >= KafkaInsertDB.STATISTICAL_INTERVAL
        return res

    def _time_interval_is_up2(self, now_time):
        res = (now_time - self.start_time).days == 1
        return res

    def data_insert_DB(self):
        data = []
        compkey_data = []
        for item in self.data_dict.values():
            item['datacount'] = "%s" % item['datacount']
            data.append(item)
            _tmp = dict()
            _tmp['t_topic'] = self.topic_instance.name
            _tmp['metriccode'] = item.get('metriccode')
            _tmp['ccompkey'] = item.get('ccompkey')
            _tmp['status'] = item.get('METRICTYPE', 0)
        ete_statistic.objects.bulk_create(data)

    def compkey_insert_or_update(self, compkey_data):
        # TODO 针对本次北向没有采集的对象，先批量置位状态为关闭，再更新
        _tmp = dict()
        _tmp['t_topic'] = self.topic_instance.name
        _tmp['metriccode'] = compkey_data.get('METRICCODE')
        _tmp['ccompkey'] = compkey_data.get('COMPKEY')
        _tmp['status'] = compkey_data.get('METRICTYPE', 0)
        ec = ete_compkey.objects.filter(
            metriccode=compkey_data.get('METRICCODE'), ccompkey=compkey_data.get('COMPKEY')).first()
        if not ec:
            _tmp['compkeyid'] = "CK" + str(int(time.time())) + 'R' + str(random.randint(100000, 999999))
            ete_compkey.objects.create(**_tmp)
        else:
            ete_compkey.objects.filter(metriccode=compkey_data.get('METRICCODE'),
                                       ccompkey=compkey_data.get('COMPKEY')).update(**_tmp)


def main(kafka_insert):
    print 'start'
    kafka_insert.get_data_and_insert()
    print 'end'


def get_topic_list():
    from apps.multiauth.models import ete_metric_base
    return ete_metric_base.objects.filter().values_list('t_topic', flat=True).distinct()


if __name__ == "__main__":
    # 启动django
    from apps.multiauth.models import ete_compkey, ete_statistic
    kafka_conn_instance = KafkaConn("")
    # topic_list = get_topic_list()
    topic_instance_list = kafka_conn_instance.get_topics(topic_list)
    params = [KafkaInsertDB(kafka_insert) for kafka_insert in topic_instance_list]
    # for i in params:
    #     main(i)
    with ThreadPoolExecutor() as executor:
        executor.map(main, params)
