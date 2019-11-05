---
title: Spring IOC 源码分析
date: 2019-11-01 00:00:00
tags: [java, note]
categories: Java
---

Spring IOC 源码分析

<!-- more -->

## Ioc 设计理念

IoC也称为依赖注⼊(dependency injection, DI)。它是⼀个对象定义依赖关系的过程，也就是说，对象只通过构造函数参数、⼯⼚⽅法的参数或对象实例构造或从⼯⼚⽅法返回后在对象实例上设置的属性来定义它们所使⽤的其他对象。

然后容器在创建bean时注⼊这些依赖项。这个过程基本上是bean的逆过程，因此称为控制反转(IoC) 在Spring中，构成应⽤程序主⼲并由Spring IoC容器管理的对象称为bean。

bean是由Spring IoC容器实例化、组装和管理的对象。IoC容器设计理念: 通过容器统⼀对象的构建⽅式，并且⾃动维护对象的依赖关系。