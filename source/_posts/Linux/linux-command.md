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

拷贝文件夹下的数据 scp -r /test/ root@ip:/root/test

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

解压命令 tar zxf filename

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