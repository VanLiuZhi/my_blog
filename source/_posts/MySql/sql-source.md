---
title: MySQL Sql sentence
date: 2019-3-07 00:00:00
tags: [database, note]
categories: database
---

原生语句的使用

<!-- more -->

## 常见join

```
select * from table_a a left join table_b b on a.key = b.key

select * from table_a a inner join table_b b on a.key = b.key

select * from table_a a right join table_b b on a.key = b.key

select * from table_a a left join table_b b on a.key = b.key where b.key is NULL

select * from table_a a right join table_b b on a.key = b.key where a.key is NULL

select * from table_a a full outer join table_b b on a.key = b.key

select * from table_a a full outer join table_b b on a.key = b.key where a.key is NULL or b.key is NULL
```
查询的效果就是取两张表的join结果，有不同的join方法，字段会被组合在一行中，也就是笛卡尔积。

### 一些例子

select a.id from app_info a right join agents_profit_setting b on a.id = b.id;
注意使用了别名a为表app_info取别名，所以在其它需要用到表app_info都使用别名访问

select a.id, b.id as b_id from app_info a right join agents_profit_setting b on a.id = b.id;
返回a，b的id，并对b的id取别名b_id

## 函数

系统提供了一些通用函数，可以在语句中使用

### 时间函数

```
mysql> select now(), curdate(), sysdate(), curtime();
+---------------------+------------+---------------------+-----------+
| now()               | curdate()  | sysdate()           | curtime() |
+---------------------+------------+---------------------+-----------+
| 2019-03-07 17:17:44 | 2019-03-07 | 2019-03-07 17:17:44 | 17:17:44  |
+---------------------+------------+---------------------+-----------+
```



### concat 和 contcat_ws

concat用来连接字符串，contcat_ws用来以分隔符参数来连接字符串
`contcat_ws(',', 'a', 'b')  输出为：a,b`