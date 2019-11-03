---
title: 计算机基础知识补充
date: 2019-10-20 00:00:00
tags: [technology]
categories: technology 技术
---

计算机基础知识补充，基础是重中之重

<!-- more -->

## 补码

这里只讨论整数

- 正数的原码和反码，补码是一样的

- 负数的反码等于原码保留符号位，其余位取反；补码为保留符号位，其余位取反加1

两个整数相加，无论正负，可以转换成两个数的补码相加，相加的结果进位超出的去掉，计算时最高位不考虑符号位的问题，以此把减法变加法

48 + (-29) = 19

原码:
48   00011 0000
-29  1001  1101

补码:
48   0011  0000
-29  1110  0011

两个补码相加  0001 0011  10进制为19，用加法在不用考虑符号位的情况下，实现了减法，

`在计算机系统中，数值一律用补码来表示和存储。原因在于，使用补码，可以将符号位和数值域统一处理；同时，加法和减法也可以统一处理。此外，补码与原码相互转换，其运算过程是相同的，不需要额外的硬件电路`

## 左移右移

计算规则: 符号位要参与移动运算，除了`负数右移`往最高位补1外，其余情况均在空位处补0，在不考虑符号位，只看绝对值的情况下，左移是扩大数值2倍，右移是缩小数值两倍，不过这是近似的结果，而且位移导致符号位是不确定的，

运算符号写法 `<< or >>`，`>>>` 三个的代表无符号右移动，没有`<<<`。`>>>`移动时，最高位均补0，正数不断右移动最小值0，负数最小值1

## 异或

如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0。和与运算相反

## 浮点数

记住，在各种编程语言中，计算得到的浮点数都是精度不准确的，所以不要轻易返回浮点数

## 哈希

哈希是摘要算法

https://www.cnblogs.com/aspirant/p/11470928.html

一、何为加载因子？
加载因子是表示Hsah表中元素的填满的程度.若:加载因子越大,填满的元素越多,好处是,空间利用率高了,但:冲突的机会加大了.反之,加载因子越小,填满的元素越少,好处是:冲突的机会减小了,但:空间浪费多了.


冲突的机会越大,则查找的成本越高.反之,查找的成本越小.因而,查找时间就越小. 

因此,必须在 "冲突的机会"与"空间利用率"之间寻找一种平衡与折衷. 这种平衡与折衷本质上是数据结构中有名的"时-空"矛盾的平衡与折衷.

二、HashMap中的加载因子
HashMap默认的加载因子是0.75，最大容量是16，因此可以得出HashMap的默认容量是：0.75*16=12。容量超过12就要进行再哈希，重新计算哈希表，原来的要删除

用户可以自定义最大容量和加载因子。


HashMap 包含如下几个构造器：

HashMap()：构建一个初始容量为 16，负载因子为 0.75 的 HashMap。

HashMap(int initialCapacity)：构建一个初始容量为 initialCapacity，负载因子为 0.75 的 HashMap。

HashMap(int initialCapacity, float loadFactor)：以指定初始容量、指定的负载因子创建一个 HashMap。

## RTTI

RTTI（Run-Time Type Identification)，通过运行时类型信息程序能够使用基类的指针或引用来检查这些指针或引用所指的对象的实际派生类型。
