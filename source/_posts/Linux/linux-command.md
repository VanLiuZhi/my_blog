---
title: linux-command 常用命令
date: 2018-10-22 00:00:00
tags: [linux, note]
categories: 操作系统
---

Linux 命令与工具

<!-- more -->

## chsh 修改用户使用的shell

查看 `cat /etc/shells` 文件，显示当前系统支持的shell，使用 `chsh -s /bin/zsh` 修改。该命令最终的效果会修改 `/etc/passwd` 文件。

## env printenv 查看环境变量

理解全局环境变量和局部环境变量，全局变量包括系统设置的和用户自己添加的，系统变量一般是全大写字母，通过printenv命令可以查看变量值 `printenv HOME`。

## scp 拷贝命令

scp命令 （主机和服务器相互拷贝数据，该命令要求开启scp服务。

从服务器到本地 `scp root@ip:拷贝路径 本地路径`

从本地到服务器 `scp 本地路径 root@ip:拷贝路径`

拷贝文件夹下的数据 scp -r /test/ root@ip:/root/target
记得拷贝文件夹要加 -r 斜杆遵照上面的格式，效果为把本地test文件夹拷贝到服务器，服务器在/root/target/test下得到文件夹下的文件

## cp

1. 复制指定目录下的全部文件到另一个目录中
如果dir2目录不存在，则可以直接使用
cp -r dir1 dir2

如果dir2目录已存在，则需要使用
cp -r dir1/. dir2

2. 复制文件
cp a.py /app/

## rm

删除当前目录下文件

在终端输入命令：rm ./*
解释：删除文件用rm命令，.点号代表当前目录，*星号是匹配符代表所有文件


## grep

内容查找命令，配合其它命令一起使用

## find 查找命令

查找命令，列出符合条件的文件路径。 find / -name *

## uptime 

查看系统运行情况，启动时间，登陆时间等。最后的三个数字代表系统最近1分钟，5分钟，15分钟负载情况。

    liuzhi@localhost  ~  uptime
    23:03  up 13:47, 3 users, load averages: 1.04 1.25 1.37


## lsof

lsof 是 linux 下的一个非常实用的系统级的监控、诊断工具。
它的意思是 `List Open Files`，很容易你就记住了它是 `“ls + of”` 的组合。
它可以用来列出被各种进程打开的文件信息，记住：linux 下 “一切皆文件”，
包括但不限于 pipes, sockets, directories, devices, 等等。
因此，使用 lsof，你可以获取任何被打开文件的各种信息。

监控进程：`lsof -p 2854` 查看指定进程打开的文件。

监控网络：`lsof -i:8080` 查看端口被哪些进程使用。

## wget

wget url 下载文件

## tar 解压

关于解压，如果是网络的包，文件后缀tar.gz

解压命令 tar zxvf filename

zip类型，需要安装解压工具 unzip

unzip filename 先创建好目标目录，在里面解压，或者指定目录

## screen 工具

需要下载

screen -r name

screen -S name  最好用大写的S

screen C d  关闭当前会话并结束进程

screen -ls

会话会有状态，dead 状态利用screen -wipe 清除

Detached 为没有人登陆，Attached为有人，有时候没有人也会是这个状态，一般是出问题了screen -D  -r ＜session-id> 先踢掉前一用户，再登陆。

screen -X -S session_id quit

## tmux 工具

需要下载，类似screen的分屏工具

创建新的会话 tmux new -s web，此时会进入新的会话web中，在下面可以看到会话名称，在tmux会话中，ctrl + b 后，才能执行对应的命令。

使用 Ctrl + b 按下 d 脱离当前会话，然后使用tmux attach 连接 web会话，这个命令用于连接刚才退出的会话，使用tmux a -t web 根据名字连接对应的会话。

## 查看发行版本信息

`cat /etc/issue` 或 `cat /etc/redhat-release`（Linux查看版本当前操作系统发行版信息）

## 查看内核信息

`uname -a`（Linux查看版本当前操作系统内核信息）

## 查看操作系统版本信息

`cat /proc/version`（Linux查看当前操作系统版本信息）

## mkdir -p

mkdir 用于创建文件夹，如果包含子目录，需要使用 -p ，这样就可以创建多层级的目录

例子：mkdir -p ~/web-develop/projects/data

## mv 移动、重命名

mv [options] 源文件或目录 目标文件或目录

## Debian 删除软件

基于Debian的Linux发行版使用apt-get管理软件包

- apt-get remove 会删除软件包而保留软件的配置文件
- apt-get purge 会同时清除软件包和软件的配置文件

## 查看端口

使用到的命令为 netstat 配合参数和 grep 命令一起使用
`netstat -an | grep 3306`

-a (all)显示所有选项，netstat默认不显示LISTEN相关
-t (tcp)仅显示tcp相关选项
-u (udp)仅显示udp相关选项
-n 拒绝显示别名，能显示数字的全部转化成数字。(重要)
-l 仅列出有在 Listen (监听) 的服務状态

-p 显示建立相关链接的程序名(macOS中表示协议 -p protocol)
-r 显示路由信息，路由表
-e 显示扩展信息，例如uid等
-s 按各个协议进行统计 (重要)
-c 每隔一个固定时间，执行该netstat命令。

提示：LISTEN和LISTENING的状态只有用-a或者-l才能看到 

## chmod 修改权限

chmod 664 file_name

可以通过 - 添加参数，一般是当前用户没有权限，才需要这个命令，权限列表分别为 所属用户，用户组，其它用户。你没有权限肯定不是所属用户，可以看看是不是这个分组的，使用 groups 命令，groups user_name 查看对应用户所属分组。whoami 查看当前用户名。

最好就是在分组里面对其分组添加权限即可，否则就要添加其它用户的权限

## pkill 终止进程

pkill -signal 进程PID或进程名称，要知道有什么信号，使用kill -l

## crontab 定时任务

没有该服务的需要安装

执行命令 `cat /etc/crontab`

```s
[root@123 ~]# cat /etc/crontab 
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
```

参数含义：
第一行SHELL变量指定了系统要使用哪个shell，这里是bash
第二行PATH变量指定了系统执行 命令的路径
第三行MAILTO变量指定了crond的任务执行信息将通过电子邮件发送给root用户，如果MAILTO变量的值为空，则表示不发送任务 执行信息给用户
第四行的HOME变量指定了在执行命令或者脚本时使用的主目录（这里未定义）

命令格式：
星号（*）：代表所有可能的值，例如month字段如果是星号，则表示在满足其它字段的制约条件后每月都执行该命令操作。
逗号（,）：可以用逗号隔开的值指定一个列表范围，例如，“1,2,5,7,8,9”
中杠（-）：可以用整数之间的中杠表示一个整数范围，例如“2-6”表示“2,3,4,5,6”
正斜线（/）：可以用正斜线指定时间的间隔频率，例如“0-23/2”表示每两小时执行一次。同时正斜线可以和星号一起使用，例如*/10，如果用在minute字段，表示每十分钟执行一次。

命令 `crontab -e` 调用系统的vim来进行编辑定时器任务

## PRM包安装

网络下载包，一般用于离线安装

包全名：操作的包是没有安装的软件包时，使用包全名。而且要注意路径。

包名：操作已经安装的软件包时，使用包名，是搜索/var/lib/rpm/中的数据库。

```s
rpm  -ivh  包全名

选项：

　　-i (install)  安装

　　-v (verbose) 显示详细信息

　　-h (hash) 显示进度

　　--nodeps 不检测依赖性（绝不允许使用）
```

安装信息会有两个百分比，看到第二个一般就是成功了

升级：rpm  -Uvh  包全名
卸载：rpm  -e  包名
查询包是否安装：rpm  -q  包名  rpm  -qa 列出已安装的包
查询包中文件安装位置：rpm  -ql  包名
查询详细信息：rpm  -qi  包名　　-i　查询软件信息（information）　　-p　查询未安装包信息（package

## supervisorctl工具

Supervisord 是用 Python 实现的一款的进程管理工具，supervisord 要求管理的程序是非 daemon 程序，supervisord 会帮你把它转成 daemon 程序，因此如果用 supervisord 来管理进程，进程需要以非daemon的方式启动。
例如：管理nginx 的话，必须在 nginx 的配置文件里添加一行设置 daemon off 让 nginx 以非 daemon 方式启动

命令分为supervisord和supervisorctl两种类型，supervisord用于初始化和启动服务，然后基本都是用supervisorctl来管理进程

```s
supervisord -c ./conf/supervisor.conf  启动服务
supervisorctl -c ./conf/supervisor.conf reload
supervisorctl -c ./conf/supervisor.conf restart 进程名称
supervisorctl -c ./conf/supervisor.conf status 查看状态
```

以上的命令都是显示的指定配置文件的形式

## sed 流编辑器工具

一个非常强大的文本处理工具

sed -n '3,9p' filename 获取3到9行的内容

sed -i 's#${user.home}#/app/svr/rocketmq#g' *.xml

替换文本，`'s/原字符串/新字符串/g'` 格式是这样，g代表全部符号的都替换，比如 `'s/d/123'` 作用于文本 ddd，结果是 123ddd，加了g后就是123123123，其中`/`可以换成其它符号，比如`#`，这样就和文本内容区别开了。`*.xml`是作用的文件，整个功能就是把当前目录xml后缀的文件进行文本替换，`${user.home}`环境变量取值换成固定的`/app/svr/rocketmq`

## journalctl 日志管理

和systemctl类似的很强大的日志查看命令

```s
# follow
journalctl -f

# 显示最近10条
journalctl -n

# 显示最近20条
journal -n 20 

# 显示磁盘占用情况
journal --disk-usage

# 查看一段时间内的
journalctl --since "2015-01-10" --until "2015-01-11 03:00"

# 过滤
journalctl -u 服务名
```

`journalctl -f -u kubelet` 让系统一直打印kubelet服务产生的日志

## ifconfig

如果没有这个包，通过yum search ifconfig，查看这个命令是在哪个包里面，`yum install net-tools.x86_64`安装后就可以使用ifconfig了

## du -sh 查看当前目录大小

用于查看当前目录下所有文件合计大小

## saltstack

saltstack是由python编写的采用c/s架构的自动化运维工具，由master和minion组成，使用ZeroMQ消息队列pub/sub方式通信，使用SSL证书签发的方式进行认证管理
本身是支持多master的。saltstack除了可以通过在节点安装客户端进行管理还支持直接通过ssh进行管理
运行模式为master端下发指令，客户端接收指令执行
采用yaml格式编写配置文件，支持api及自定义python模块，能轻松实现功能扩展

saltstack有一个saltstack master，而很多saltstack minon在初始化时会连接到该master上
初始化时，minion会交换一个秘钥建立握手，然后建立一个持久的加密的TCP连接
通常，命令起始于master的命令行中，master将命令分发minion上
saltstack master可以同时连接很多minion而无需担心过载，这都归功于ZeroMQ
由于minion和master之间建立了持久化连接，所以master上的命令能很快的到达minion上。minion也可以缓存多种数据，以便加速执行

## tail 查看文件

tail -f 实时查看日志文件 tail -f 日志文件log
tail - 100f 实时查看日志文件 后一百行
tail -f -n 100 catalina.out linux查看日志后100行
搜寻字符串
grep ‘搜寻字符串’ filename
按ctrl+c 退出

## 修改用户和用户组

chown www lifang 改用户  chown 用户 要修改的文件
chgrp www lifang 改用户组  chgrp 用户组 要修改的文件



