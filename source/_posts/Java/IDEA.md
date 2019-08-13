---
title: Java IDEA
date: 2019-04-05 00:00:00
tags: [java, note]
categories: Java
---

IDEA 使用技巧补充总结

<!-- more -->

## IDEA 工具使用

ntellig idea 使用@Resource或者@Autowire报错，出现红色波浪线；

虽然不影响使用，但是看着很不爽，所以还是解决了下：

报错提示：Could not autowire. No beans of '' type found. less... (Ctrl+F1)  Checks autowiring problems in a bean class.

解决方法：Settings - Editor - Inspections - Spring - Spring Core - Code - Autowiring for Bean Class 修改成告警级别

## 热部署

静态语言不像动态语言，要实现热部署要程序和IDEA配合才行

引入依赖

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-devtools</artifactId>
</dependency>
```

依赖的作用：

默认禁用缓存选项。比如模板引擎将缓存编译完的模板，以避免重复解析模板文件。
自动重启。只要classpath下的文件有变动，应用就会自动重启。
在运行一个完整的、打包过的应用时，开发者工具（devtools）会被自动禁用。
如果应用使用 java -jar 或特殊的类加载器启动，都会被认为是一个产品级的应用（production application），从而禁用开发者工具。
只要classpath下文件有变动，应用就会重启。一些比如静态assets、视图模板文件等资源 文件的变动，应用不会重启。
`唯一触发重启的方式就是更新classpath`
IDEA本身提供了热部署功能，但是限制性比较大，只能对静态资源的修改、方法内的修改才能进行热更新，
对于方法参数或者方法类的修改不能进行热部署，但是像devtools,jrebel 都能够对类的修改进行重新加载。

总结：

添加spring-boot-devtools依赖
修改classpath下的Java文件，然后更新classpath，这时应用就会自动重启。
修改classpath下的页面文件，然后更新classpath，但是访问页面可以看到效果（即重新加载）。
IDEA更新classpath的方法：【Build】->【Build Project】，如果你设置了自动编译，那就可以省略这一步了（可能因为IDEA版本的原因，有需要手动操作）。

1. spring-boot-devtools 热部署是对修改的类和配置文件进行重新加载，所以在重新加载的过程中会看到项目启动的过程，其本质上这个时候只是对修改类和配置文件的重新加载，所以速度极快；
2. spring-boot-devtools 对于前端使用模板引擎的项目，能够自动禁用缓存，在页面修改后，只需要刷新浏览器器页面即可；
3. 为什么在 idea 中 spring-boot-devtools 没有热部署？ 因为在Idea 中自动编译默认是停用的，启用路径 build -> compile -> buildProjectAutomatically
4. 为什么在 idea 中启用自动编译依然没有热部署？ idea监测到项目runninng 或者 debuging 会停用自动编译，所以还需要手动biild [Ctrl + F9] 或者 [ctrl +  b]

全自动设置方式，打开运行时编译：

1. build -> compile -> buildProjectAutomatically
2. 快捷键Ctrl + Shift + Alt + /，选择Registry
3. 勾选 Compiler autoMake allow when app running