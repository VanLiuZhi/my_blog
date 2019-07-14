---
title: Ant front learn
date: 2019-07-14 00:00:00
tags: [javascript, technology]
categories: technology 技术
---

Ant Vue 实现使用总结

<!-- more -->

## 知识补充

- Vue.prototype
当你在main.js里声明了Vue.prototype.a = 1后，因为你的每一个vue组件都是一个Vue对象的实例，所以即使你没有在组件内部使用data(){return{……}}声明a，你依然可以在组件中通过this.a来访问。
当然，你也可以在组件中添加一个变量a，这时你访问的就是你在组件中添加的a，而不再是之前在原型中添加的a了，当然你对组件的a继续修改即不会影响原型中的a和其他组建中的a，就类似于下面这段代码（Form是一个自定义对象类型，Vue也可以看作一个自定义对象类型，而每个.vue文件就是一个对象的实例）


## 权限设计


