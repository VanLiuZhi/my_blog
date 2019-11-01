---
title: svn 版本控制工具
date: 2018-10-22 00:00:00
tags: [web, note, svn]
categories: 操作系统
---

SVN版本控制

<!-- more -->

## 命令

1. 查看日志

svn log --search liuzhi -l 100  -v .
svn log --search liuzhi -l 100  查看特定用户的提交日志和修改文件(注意这里的100条是全部的提交记录，是在这100条中过滤用户)

```s
参数: 
--search liuzhi 筛选结果，这里筛选用户
-l 筛选条数
-v 查看修改文件，后面的参数为查看的目录，在项目根目录执行就可以看到所有的文件修改日志
```

其它用法

svn log -r 4:5;  #只看版本4和版本5的日志信息;
svn log test.c -v;  #查看文件test.c的日志修改信息;
svn list http://svn.test.com/svn  #查看目录中的文件;