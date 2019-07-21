---
title: Spring
date: 2019-04-05 00:00:00
tags: [java, note]
categories: Java编程
---

Spring 基础概念

<!-- more -->

## 应用服务器

SpringBoot已经内置了Servlet容器，包括tomcat，jetty，Undertow

## Spring基础

IoC 控制反转：Spring所倡导的开发方式就是如此，所有的类都会在spring容器中登记，告诉spring你是个什么东西，你需要什么东西，然后spring会在系统运行到适当的时候，把你要的东西主动给你，同时也把你交给其他需要你的东西。所有的类的创建、销毁都由spring来控制，也就是说控制对象生存周期的不再是引用它的对象，而是spring。对于某个具体的对象而言，以前是它控制其他对象，现在是所有对象都被spring控制，所以这叫控制反转。
IoC的一个重点是在系统运行中，动态的向某个对象提供它所需要的其他对象。这一点是通过DI（Dependency Injection，依赖注入）来实现的。比如对象A需要操作数据库，以前我们总是要在A中自己编写代码来获得一个Connection对象，有了 spring我们就只需要告诉spring，A中需要一个Connection，至于这个Connection怎么构造，何时构造，A不需要知道。在系统运行时，spring会在适当的时候制造一个Connection，然后像打针一样，注射到A当中，这样就完成了对各个对象之间关系的控制。A需要依赖 Connection才能正常运行，而这个Connection是由spring注入到A中的，依赖注入的名字就这么来的。
`Spring的IoC容器就是实现控制反转和依赖注入`

- JavaBean
JavaBean 是一种JAVA语言写成的可重用组件。为写成JavaBean，类必须是具体的和公共的，并且具有无参数的构造器。JavaBean 通过提供符合一致性设计模式的公共方法将内部域暴露成员属性，set和get方法获取。众所周知，属性名称符合这种模式，其他Java 类可以通过自省机制(反射机制)发现和操作这些JavaBean 的属性。

- POJO
POJO（Plain Ordinary Java Object）简单的Java对象，实际就是普通JavaBeans，是为了避免和EJB混淆所创造的简称。
使用POJO名称是为了避免和EJB混淆起来, 而且简称比较直接. 其中有一些属性及其getter setter方法的类,没有业务逻辑，有时可以作为VO(value -object)或dto(Data Transform Object)来使用.当然,如果你有一个简单的运算属性也是可以的,但不允许有业务方法,也不能携带有connection之类的方法

- RMI
RMI(Remote Method Invocation，远程方法调用)是用Java在JDK1.2中实现的，它大大增强了Java开发分布式应用的能力。Java作为一种风靡一时的网络开发语言，其巨大的威力就体现在它强大的开发分布式网络应用的能力上，而RMI就是开发百分之百纯Java的网络分布式应用系统的核心解决方案之一。其实它可以被看作是RPC的Java版本。但是传统RPC并不能很好地应用于分布式对象系统。而Java RMI 则支持存储于不同地址空间的程序级对象之间彼此进行通信，实现远程对象之间的无缝远程调用。

## Spring properties 配置文件

通过配置文件，可以修改框架配置，或为框架提供数据，比如生成一个随机数，和框架配合后可以很方便的获取一个随机数，而不需要写更多的代码

在配置中这么写:
shiyanlou.springboot=Hello_shiyanlou

在控制器对象中通过注解定义shiyanlou，变量shiyanlou的值就是配置中的值Hello_shiyanlou

    @Value("${shiyanlou.springboot}")
    private String shiyanlou;


## 模板引擎

freemarker
Thymeleaf
velocity

## 注解

@SpringBootApplication注解相当于同时使用@EnableAutoConfiguration、@ComponentScan、@Configurations三个注解  

@EnableAutoConfiguration用于打开SpringBoot自动配置，而其余注解为Spring注解，这里不再赘述

@RestController相当于同时使用@Controller和@ResponseBody注解

@Configuration表示该类为配置类，该注解可以被@ComponentScan扫描到

// 通过@ImportResource加载xml配置文件 配置文件放在资源目录下，注解作用于主函数入口
@ImportResource(value = "classpath:config.xml")

@Transactional 用于事务的注解

# IDEA 插件

Lombok plugin
GsonFormat
FindBugs-IDEA
CodeGlance	右侧文档结构图
.ignore	git 文件提交过滤
Maven Helper maven插件，打开该pom文件的Dependency Analyzer视图


    Ctrl+Alt+O 优化导入的类和包 
    Alt+Insert 生成代码(如get,set方法,构造函数等) 或者右键（Generate） 
    fori/sout/psvm + Tab 
    Ctrl+Alt+T 生成try catch 或者 Alt+enter 
    CTRL+ALT+T 把选中的代码放在 TRY{} IF{} ELSE{} 里 
    Ctrl + O 重写方法 
    Ctrl + I 实现方法 
    Ctr+shift+U 大小写转化 
    ALT+回车 导入包,自动修正 
    ALT+/ 代码提示 
    CTRL+J 自动代码 
    Ctrl+Shift+J，整合两行为一行 
    CTRL+空格 代码提示 
    CTRL+SHIFT+SPACE 自动补全代码 
    CTRL+ALT+L 格式化代码 
    CTRL+ALT+I 自动缩进 
    CTRL+ALT+O 优化导入的类和包 
    ALT+INSERT 生成代码(如GET,SET方法,构造函数等) 
    CTRL+E 最近更改的代码 
    CTRL+ALT+SPACE 类名或接口名提示 
    CTRL+P 方法参数提示 
    CTRL+Q，可以看到当前方法的声明
    Shift+F6 重构-重命名 (包、类、方法、变量、甚至注释等) 
    Ctrl+Alt+V 提取变量



    Ctrl＋Shift＋Backspace可以跳转到上次编辑的地 
    CTRL+ALT+ left/right 前后导航编辑过的地方 
    ALT+7 靠左窗口显示当前文件的结构 
    Ctrl+F12 浮动显示当前文件的结构 
    ALT+F7 找到你的函数或者变量或者类的所有引用到的地方 
    CTRL+ALT+F7 找到你的函数或者变量或者类的所有引用到的地方
    Ctrl+Shift+Alt+N 查找类中的方法或变量 
    双击SHIFT 在项目的所有目录查找文件 
    Ctrl+N 查找类 
    Ctrl+Shift+N 查找文件 
    CTRL+G 定位行 
    CTRL+F 在当前窗口查找文本 
    CTRL+SHIFT+F 在指定窗口查找文本 
    CTRL+R 在 当前窗口替换文本 
    CTRL+SHIFT+R 在指定窗口替换文本 
    ALT+SHIFT+C 查找修改的文件 
    CTRL+E 最近打开的文件 
    F3 向下查找关键字出现位置 
    SHIFT+F3 向上一个关键字出现位置 
    选中文本，按Alt+F3 ，高亮相同文本，F3逐个往下查找相同文本 
    F4 查找变量来源
    CTRL+SHIFT+O 弹出显示查找内容
    Ctrl+W 选中代码，连续按会有其他效果 
    F2 或Shift+F2 高亮错误或警告快速定位 
    Ctrl+Up/Down 光标跳转到第一行或最后一行下
    Ctrl+B 快速打开光标处的类或方法 
    CTRL+ALT+B 找所有的子类 
    CTRL+SHIFT+B 找变量的类
    Ctrl+Shift+上下键 上下移动代码 
    Ctrl+Alt+ left/right 返回至上次浏览的位置 
    Ctrl+X 删除行 
    Ctrl+D 复制行 
    Ctrl+/ 或 Ctrl+Shift+/ 注释（// 或者/…/ ）
    Ctrl+H 显示类结构图 
    Ctrl+Q 显示注释文档
    Alt+F1 查找代码所在位置 
    Alt+1 快速打开或隐藏工程面板
    Alt+ left/right 切换代码视图 
    ALT+ ↑/↓ 在方法间快速移动定位 
    CTRL+ALT+ left/right 前后导航编辑过的地方 
    Ctrl＋Shift＋Backspace可以跳转到上次编辑的地 
    Alt+6 查找TODO



    SHIFT+ENTER 另起一行 
    CTRL+Z 倒退(撤销) 
    CTRL+SHIFT+Z 向前(取消撤销) 
    CTRL+ALT+F12 资源管理器打开文件夹 
    ALT+F1 查找文件所在目录位置 
    SHIFT+ALT+INSERT 竖编辑模式 
    CTRL+F4 关闭当前窗口 
    Ctrl+Alt+V，可以引入变量。例如：new String(); 自动导入变量定义 
    Ctrl+~，快速切换方案（界面外观、代码风格、快捷键映射等菜单



    alt+F8 debug时选中查看值 
    Alt+Shift+F9，选择 Debug 
    Alt+Shift+F10，选择 Run 
    Ctrl+Shift+F9，编译 
    Ctrl+Shift+F8，查看断点
    F7，步入 
    Shift+F7，智能步入 
    Alt+Shift+F7，强制步入 
    F8，步过 
    Shift+F8，步出 
    Alt+Shift+F8，强制步过
    Alt+F9，运行至光标处 
    Ctrl+Alt+F9，强制运行至光标处 
    F9，恢复程序 
    Alt+F10，定位到断点



    Ctrl+Alt+Shift+T，弹出重构菜单 
    Shift+F6，重命名 
    F6，移动 
    F5，复制 
    Alt+Delete，安全删除 
    Ctrl+Alt+N，内联
