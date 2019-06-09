---
title: Java IDEA
date: 2019-04-05 00:00:00
tags: [java, note]
categories: Java
---

IDEA 使用

<!-- more -->

## IDEA 工具使用

ntellig idea 使用@Resource或者@Autowire报错，出现红色波浪线；

虽然不影响使用，但是看着很不爽，所以还是解决了下：

报错提示：Could not autowire. No beans of '' type found. less... (Ctrl+F1)  Checks autowiring problems in a bean class.

解决方法：Settings - Editor - Inspections - Spring - Spring Core - Code - Autowiring for Bean Class 修改成告警级别