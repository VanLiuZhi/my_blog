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

## vue-cli3.0

全新的脚手架

### vue-cli3.0 环境变量与模式

vue-cli3.0移除了配置文件目录：config和build文件夹(最外层已经没有这两个文件夹了)

总共提供了四种方式来制定环境变量：

1. 在根目录添加.env文件，配置所有情况下都会用到的配置（不知道这个存在的意义，所有的都需要的也就不需要配置了吧）。
2. 在根目录添加.env.local 文件，配置所有情况下都会用到的配置，与.env的区别是只会在本地，该文件不会被git跟踪。
3. 在根目录添加.env.[mode] 文件，配置对应某个模式下的配置,比如：.env.development来配置开发环境的配置。
4. 在根目录添加.env.[mode].local文件，配置对应某个模式下的配置,与.env.[mode]的区别也只是会在本地生效，该文件不会被git跟踪。

## 权限设计

RBAC设计思想

基于角色的访问控制（Role-Based Access Control）
有两种正在实践中使用的RBAC访问控制方式：隐式(模糊)的方式和显示(明确)的方式。

隐式：假如用于属于管理员，在对账户操作的时候，就去判断用于是否是管理员角色，因为在常规的认知中，管理员一般都是能操作账号的，但是实际是否分配的这样的权限是未知的，这就是隐式的，是一种假设。
显示：就是明确的权限判断


前端的发展到现在，我们引用人类文明发展历程做比喻，划分为4个时代，每一个时代都是技术的革命和进步

1. 原始社会

1994 年的时候，网景公司 (Netscape Communications) 推出了第一款浏览器：NCSAMosaic，当时还没有JavaScript语言，网页是静态的，基于HTML文本描述语言，提交一个表单，等待很久，最后可能返回给你个 “用户名错误”。

总结：这个时候是没有前端的概念的，页面是后端的一部分，也就是网页是由后端代码直接生成的。

2. 石器时代

就在同一年(1994 年)，PHP 出现了，有了将数据嵌入到 HTML 中的形式，这意味着互联网行业出现了钻木取火，不断朝石器时代发展。
这时候的互联网，兴起了数据嵌入模板，模板直接写样式的开发模式，发展成了后来的 MVC 模式：

Model（模型层）：提供/保存数据。
Controller（控制层）：数据处理，实现业务逻辑。
View（视图层）：展示数据，提供用户界面。

该模式至今仍在沿用，网页同样由后端生成，不过不是直接输出了，而是对模块的渲染，编写模板的工作已经属于前端的范畴了，不过由于模板和后端的绑定，编写模板需要了解后端，如现在的Django的模板语言，JSP技术等，此时仍然没有前端的地位，这些工作一般由后端开发人员完成，除非是比较复杂的页面布局，交由专门的人员编写。

总结: 技术开始规范，提出了MVC的开发模式。不过编写模板人员仍然需要了解后端模板语言，或者模板是静态的，写好后又由后端开发人员修改数据，工作重复和繁琐。

3. 铁器时代

1. JavaScript的诞生

1995年，网景工程师Brendan Eich花了10天时间设计了JavaScript语言。起初这种脚本语言叫做Mocha，后改名LiveScript，后来为了借助Java语言创造良好的营销效果最终改名为JavaScript。网景公司把这种脚本语言嵌入到了Navigator 2.0之中，使其能在浏览器中运行。这也是历史遗留问题的开端，Brendan Eich最初只是为了开发一种脚本语言，因而没有面向对象，也没有模块化等特性。

2. ECMA规范 

与此相对的是，1996年，微软发布了VBScript和JScript。JScript是对JavaScript进行逆向工程的实现，并内置于Internet Explorer 3中。但是JavaScript与JScript两种语言的实现存在差别，这导致了程序员开发的网页不能同时兼容Navigator和Internet Explorer浏览器。Internet Explorer开始抢夺Netscape的市场份额，这导致了第一次浏览器战争。

1996年11月，为了确保JavaScript的市场领导地位，网景将JavaScript提交到欧洲计算机制造商协会（European Computer Manufacturers Association）以便将其进行国际标准化。

1997年6月，ECMA以JavaScript语言为基础制定了ECMAScript标准规范ECMA-262。JavaScript是ECMAScript规范最著名的实现之一，除此之外，ActionScript和JScript也都是ECMAScript规范的实现语言。自此，浏览器厂商都开始逐步实现ECMAScript规范。

该规范一直沿用至今，我们经常听到的ES6, 全称 ECMAScript 6.0，是 JavaScript 的一个版本标准，2015.06 发布，增加了面向对象，模块化等支持，使得JavaScript 语言可以用来编写复杂的大型应用程序

3. 动态网页

到了 1998 年前后，Ajax（Asynchronous Java And XML：异步的 Java 和 XML）得到了相对的应用，并且在之后逐渐被使用到各个页面上，从而促进了 Web 从 1.0 的静态网页，纯内容展示向 Web 2.0 模式迈进。

这时候，前端不再是后端的模板，它可以独立得到各种数据。相对于 Web 1.0 的时代，Web 2.0 由石器时代迈向了铁器时代！

在 Web 2.0 的时代中，在 2006 年的时候，用于操作 DOM 的 jQuery 出现了，它快速地风靡了全球。大量的基于 jQuery 的插件构成了一个庞大的生态系统，从而稳固了 jQuery 作为 JS 库一哥的地位。

jQuery 的影响是源远流长的，很少有人直接操作原生接口。

总结：JavaScript诞生，并由ECMA协会统一了规范和标准，避免了混乱的开端，ECMAScript是一个很重要的标准。提出了AJAX技术，网页从静态向动态发展。用于操作DOM的jQuery成为主流，降低了对DOM的操作难度。

4. 工业时代

伴随着信息时代、大数据时代的到来，jQuery 在大量的数据操作中的弊端体现出来了，它在对 DOM 进行大量的操作中，会导致页面的加载缓慢等问题（这也和DOM的设计，历史原因相关），这时，有些前端开发人员逐渐觉得力不从心了。

1999年，W3C发布了HTML 4.0.1版本，在之后的几年，没有再发布更新的Web标准。随着Web的迅猛发展，旧的Web标准已不能满足Web应用的快速增长，委员会开始起草新的web标准HTML5，2008年1月22日，第一份正式草案发布。
HTML5草案发布不久，Google在2008年12月发布了Chrome浏览器，加入了第二次浏览器大战当中。Chrome使用了Safari开源的WebKit作为布局引擎，并且研发了高效的JavaScript引擎V8。谷歌 V8 引擎发布，终结微软 IE 时代。

Chrome的发布，其JavaScript引擎V8的高效执行引起了Ryan Dahl的注意。2009年，Ryan利用Chrome的V8引擎打造了基于事件循环的异步I/O框架——Node.js诞生，谷歌也推出了自己的前端框架AngularJS，此后，2011 年 React 诞生。
2014 年 Vue.js 诞生。

新框架衍生出了新的MVVM开发模式

何为 MVVM 模式？

Model：提供/保存数据。
View：视图
View-Model：简化的 Controller，唯一的作用就是为 View 提供处理好的数据，不含其它逻辑。

如果说，Angular、React、Vue 等 MVVM 模式的出现，以及 Webpack 的前端工程化构建，加速了数据驱动前端工程化的发展。那么，Node 这个基于 V8 引擎的服务端 JavaScript 运行环境的诞生，可媲美 Ajax 对于前端的贡献。

Node 是前端的第二次飞跃，它使 JS 在服务端语言中也有了一席之地。

总结：前端开始飞速发展，百花齐放。三大框架Angular、React、Vue并立而行至此，前端正式进入工业时代，开发更加工程化和规范化，JavaScript也不再是以往被人调侃的“玩具语言”，也不再局限于web开发，被运用于服务端，游戏，桌面，APP等。



当前主流

我们回顾了前端的发展历程，提到了很多概念，JavaScript，应该由三部分组成

JavaScript分为 ECMAScript，DOM，BOM。

