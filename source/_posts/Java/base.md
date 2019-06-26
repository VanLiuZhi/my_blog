---
title: Java编程思想
date: 2019-04-05 00:00:00
tags: [java, note]
categories: Java
---

Java 编程思想

<!-- more -->

## 名词解释

大部分都是通用的，或者是设计模式，只是第一次接触难免有些生疏晦涩。

构件：其实就是组件，可以按照组件来理解，不过在这个范畴内一般翻译为构件

DAO：数据库访问模型 Data Access Object

DTO：数据传输对象（DTO)(Data Transfer Object)，是一种设计模式之间传输数据的软件应用系统。数据传输目标往往是数据访问对象从数据库中检索数据。数据传输对象与数据交互对象或数据访问对象之间的差异是一个以不具有任何行为除了存储和检索的数据（访问和存取器）。

Bean：它的定义为，描述Java的软件组件模型，EJB是Enterprise Java Bean的缩写。javaBean在MVC设计模型中是model，又称模型层，在一般的程序中，我们称它为数据层，就是用来设置数据的属性和一些行为，然后我会提供获取属性和设置属性的get/set方法JavaBean是一种JAVA语言写成的可重用组件。

JDBC（Java DataBase Connectivity,java数据库连接）是一种用于执行SQL语句的Java API，可以为多种关系数据库提供统一访问，它由一组用Java语言编写的类和接口组成。JDBC提供了一种基准，据此可以构建更高级的工具和接口，使数据库开发人员能够编写数据库应用程序，同时，JDBC也是个商标名。

JPA是Java Persistence API的简称，中文名Java持久层API，是JDK 5.0注解或XML描述对象－关系表的映射关系，并将运行期的实体对象持久化到数据库中。
Sun引入新的JPA ORM规范出于两个原因：其一，简化现有Java EE和Java SE应用开发工作；其二，Sun希望整合ORM技术，实现天下归一。

## 环境变量

配置环境变量，保证 java javac java -version 都能输出正确信息

## 1 基本内容

return 只能返回一个对象，python可以返回多个，面向对象体现更明显，强类型

面向对象部分是Java核心和难点部分，不过语言还是要在实践中学习，而实践又会用框架，等代码感熟练了，慢慢的去看源码的时候，再来体会面向对象更容易掌握，初期可以跳过繁琐的概念，因为看了也记不住。

面向对象集中在7，8，9，10章节，以其它语言的基础可以快速过一遍，先理解11章后的内容

## 2 一切都是对象

对象成员不进行初始化会设定默认值，不过对于局部变量不适应。

面向对象：字段或数据成员，方法，Python中叫做属性。

方法签名，可能在Python中不怎么提及这个概念，由于Java是静态语言，所以方法签名唯一确定方法。

java.lang 是一个类库，每个Java文件都会默认导入它。

main() 方法的参数是一个String对象的数组，以及一个args，一般都要写这两个，否则编译器报错，因为args要用来存储命令行参数。

注释文档：javadoc是JDK安装的一部分，用于提取注释的工具。该工具提取注释，可以生产html文件。可以对工具输出风格做调整，通过编写自己的被称为 “doclets” 的javadoc处理器来实现。javadoc 有特定的语法。

所有的javadoc语法只能在 “/**  */” 注释中出现，“//” 是不可以的。

使用方式：嵌入HTML，使用文档标签。

## 3 操作符

别名对象, 可以强制类型转换
equals()
直接常量可以添加标识符，使表达更加清晰
类型转换操作符 long i = (long) j  将整形j转换成长整形并赋值给i，转换总是截尾，要想四舍五入需要使用round库
提升：对基本类型执行按位运算或算术运算，只要类型比int小（比如char,byte,short），那么在运算之前，会自动转换成int。较大的数据类型决定了结果，比如double和float相乘，结果是double
sizeof：c,c++中用来计算数据占的字节，这导致移植代码很头疼，不同的处理器对数据存储所占的字节是不一样的，而Java不会这样，它的数据类型在所有机器上都是一样的

## 4 控制执行流程

不允许将一个数字作为布尔值使用，应该if(a==0)，for循环语法，for(int i : range(100))

## 5 初始化与清理

构造器：构造器的命名和类名相同，可以带访问修饰符，不能有返回值。

方法重载：构造器也可以方法重载，方法重载要求函数名相同，参数不一样，参数的顺序不一样也是方法重载，但是一般不建议这么做。一般动态语言不需要方法重载。方法重载一定要写的明确，这样编译器在调用方法的时候才知道是调用哪个方法。

缺省构造器：构造器可以不提供，编译器默认创建一个，这个时候构造器没做任何事情

this关键字：通常不需要显示的写出它来，和python不一样，另外它是关键字

垃圾回收：
1.对象可能不被垃圾回收 2.垃圾回收并不等于析构

## 6 访问控制

java后缀的源代码通常称为编译单元，每个编译单元内只能有一个public类。

代码组织：当编译一个java后缀文件时，文件的每个类都会生成.class文件。

关于package语句，必须是文件中除注释外的第一句代码。包命名规则全部使用小写字母，包括中间的字也是如此。导包用的星号如果两个包包含同一个类，那么这肯定是有问题的，但是只要不写调用的代码编译器是不会报错的，这种情况应该用完整路径来引用对象。

理解编译单元，默认包，friendly权限是java的默认权限，也称作包（package）访问权限

public private

1. 默认包：同一个包下的两个类，可以做到A类访问B类的未修饰方法，如果C类和A类不属于同一个包，那么C类的方法要修饰为public，A类才能访问到。这种默认的机制保护了包下的类，但是最好做修饰，在IDEA中，你不对类的方法做修饰，会有告警级别的提示，因为默认的包访问权限可以方便包，对不属于同一个包的访问做保护，但是最好考虑清楚，然后合理运用private。

2. 另外即使使用了private修饰，仍然可以在当前类定义新的方法去访问private，所有不能因为在类中某个对象的引用是private，就认为其他的对象无法拥有该对象的public引用

protected: 受保护的

一个类继承了另一个包中的类，那么唯一可访问的成员就是源包的public成员。（如果继承在同一个包中，就可以访问所有的拥有包访问权限的成员）。基类的创建者希望某个成员，把他的访问权限给予派生类而不是所有类，这时候就可以使用protected，protected也提供包访问权限，同意包内的其它类可以访问protected元素。这是为了在拥有包访问权限下，为了让跨包继承类也能访问的一种做法，否则就要用public来修饰。

`访问权限的控制常被称为是具体实现的隐藏`

类的访问权限：一个包下的类，要遵守他的文件名定义规则，然后只能有一个public类，可以把public去掉，这样该类就只有包访问权限，其它包即使导入他，也不能访问，通过也很少这么做。另外当不用public修饰类时，类命可以不和文件名一致。

再次强调，类前面不加修饰，权限就是包访问权限，当前包内的其它类可以访问，跨包不行。

## 7 复用类

组合，继承，代理

每一个非基本类型对象都有一个toString方法，类似python的 `__str__`

初始化，继承的基类初始化的时候，默认会调用基类的构造方法，构建过程是从基类“向外”扩散的，当然这只能调用默认不带参数的构造器，带参数的构造器需要显示的调用super方法。

```java
class Cleanser {
    Cleanser(int i) {
        System.out.println(i);
    }
    Cleanser() {
        System.out.println("123");
    }
}

public class Detergent extends Cleanser {
    Detergent() {
        // super(321)
        System.out.println("abc");
    }
    public static void main(String[] args) {
        Detergent x = new Detergent();
        System.out.println("Testing base class");
    }
}
```

如果去掉Cleanser类的默认构造函数，IDEA会警告，因为找不到满足条件的构造函数，编译代码会去调用需要传递参数的构造函数导致报错。注释部分为显示调用。

名称屏蔽：如果Java的基类拥有某个已被多次重载的方法名称，那么在导出类中重新定义该方法名称并不会屏蔽在基类中的任何版本，这一点与C++不同`（如果C++要这么做需要屏蔽基类方法，另外本书比较旧了，不排除c++做了改动）`

```java
class Homer {
    char doh(char c) {
        System.out.println("doh(char)");
        return 'd';
    }

    float doh(float f) {
        System.out.println("doh(float)");
        return 1.0f;
    }
}

class Milhouse {
}

class Bart extends Homer {
    void doh(Milhouse m) {
        System.out.println("doh(Milhouse)");
    }
}

public class Hide {
    public static void main(String[] args) {
        Bart b = new Bart();
        b.doh(1);
        b.doh('x');
        b.doh(1.0f);
        b.doh(new Milhouse());
    }
}
// doh(float)
// doh(char)
// doh(float)
// doh(Milhouse)
```

向上转型：基类A，有一个方法，参数类型为A的引用，导出类B，调用A的方法，传递参数为B的实例，这似乎和强类型语言Java违背，但在继承中是可以的，你需要认识到B对象同样也是一种A对象，这种将B的引用转换为A的引用的动作，称为向上转型。父类引用变量可以引用子类对象。

final:

1. 允许空白final，但是在构造函数中必须进行初始化。
2. final 参数，可以用来修饰参数。被修饰的参数不能在方法中去修改它。
3. 修饰方法，防止方法被继承类修改。
4. 类修饰，那么该类无法被继承。类方法都会隐式的指向final。

private 和 final: 类中的private方法都隐式的指定为final。可以对private添加final，但这并不能给该方法增加任何额外的意义。 “覆盖”只有在某方法是基类的接口的一部分才会出现，即`必须能将一个对象向上转型`为它的基本类型并调用相同的方法。如果某方法为private，它就不是基类接口的一部分，用private修饰的方法在基类中同名方法不是方法覆盖，而是生成一个新的方法。

继承与初始化

```java
class Insect {
    private int i = 9;
    protected int j;
    Insect() {
        System.out.println("i = " + i + ", j= " + j);
        j = 39;
    }
    private static int x1 = printInt("static Insecr.x1 initialized");
    static int printInt(String s) {
        System.out.println(s);
        return 47;
    }
}

public class Beetle extends Insect {
    private int k = printInt("Beetle.k initialized");
    public Beetle () {
        System.out.println("k = " + k);
        System.out.println("j = " + j);
    }
    private static int x2 = printInt("static Beetle.x2 initialized");
    public static void main(String[] args) {
        System.out.println("Beetle constructor");
        Beetle b = new Beetle();
    }
}
//static Insecr.x1 initialized
//static Beetle.x2 initialized
//Beetle constructor
//i = 9, j= 0
//Beetle.k initialized
//k = 47
//j = 39
```

理解以上输出结果。

1. 每个类的编译代码都存在于它自己的独立文件夹中。
2. 该文件只在需要使用程序代码时才会被加载。
3. 一般来说类的代码在初次使用时才会加载，这通常指加载发生于创建类的第一个对象之时（但是访问static域或static方法时，也会加载。构造器也是static方法，它没有显示的表示出来，更准确的说，类是在其任何static成员被访问时才加载的）
4. 按照继承先加载对象，继承最顶层的类先被加载，然后是下面的类。然后创建对象，基本类型设置为默认值，对象的引用设置为null（通常是将对象内存二进制设置为零），然后是构造器调用。

## 8 多态

在面向对象程序设计语言中，多态是继数据抽象和继承之后的第三种基本特征。

“封装”通过合并特征和行为来创建新的数据类型。“实现隐藏”则通过将细节“私有化”把接口和实现分离开来。多态的作用是消除类型之间的耦合关系。

方法调用绑定：在程序执行前就把方法同相关联的方法主体关联起来称为前期绑定，与之相对的就是后期绑定，就是在运行时根据对象类型进行绑定。所有编译器需要有一种机制在运行时判断对象类型。Java除了static和final（private也是final）之外，其它都是后期绑定。使用final就可以告诉编译器关系动态绑定，一定程度优化代码，不过完全没有这个必要。
Java中的所有方法都是通过动态绑定来实现多态的。

同样注意私有方法，确定你是要覆盖还是重载。

多态存在的三个必要条件
1. 继承
2. 重写
3. 父类引用指向子类对象

当使用多态方式调用方法时，首先检查父类中是否有该方法，如果没有，则编译错误；如果有，再去调用子类的同名方法。

协变返回类型: 在Java1.4及以前，子类方法如果要覆盖超类的某个方法，必须具有完全相同的方法签名，包括返回值也必须完全一样。Java5.0放宽了这一限制，只要子类方法与超类方法具有相同的方法签名，或者子类方法的返回值是超类方法的子类型，就可以覆盖。

"协变返回(covariant return)"，仅在subclass（子类）的返回类型是superclass（父类）返回类型的extension（继承）时才被容许。

## 9 接口

接口和内部类为我们提供了一种将接口与实现分离的更加结构化的方法

抽象类或抽象方法：abstract定义抽象方法，如果一个类包含一个抽象方法，必须修饰为抽象类。在C++中，这相当于虚函数，纯虚函数。

接口使得抽象的概念更向前迈进了一步，接口产生一个完全抽象的类，允许创建者确定方法名，列表参数，返回类型，不提供方法体。

接口中的方法默认是public的，接口类默认是包访问权限。

通过关键字implements(实现)来像继承一样声明当前类是哪个接口的实现。

```java
interface B {

}
interface A extends B {

}
// 接口继承
```

```java
class A implements B
// 普通的实现
```

```java
class A implements B, C, D
// 实现来自多个接口
```

```java
class A extends B implements C, D {}
// 实现了多继承，也避免了钻石继承问题
```

接口适配：允许一个接口有多个不同的实现

接口的域：由于接口的任何域都是final和static，历史代码会用接口来做常量，Java SE5 后，一般用枚举enum来代替了

嵌套接口：接口可以嵌套在类中，可能这种运用有点少见，要知道可以这么做，遇到了可以来看看书

## 10 内部类

将一个类的定义放在另一个类的定义中，称为内部类（暂时跳过这一章节）

## 11 持有对象

容器类：基本类型是List，set，Queue和Map，这些对象类型也称为集合类，但由于Java的类库使用了Collection这个名字来指代该类库的一个特殊子集，所有更广泛的称为容器


## 15 泛型

## 20 注解

包含三种标准注解和四种元注解

标准注解：
1. Override
2. Deprecated
3. SuppressWarnings

元注解：
1. Target
2. Retention
3. Documented
4. Inherited

注解是一种标记，基本注解用来决定注解到什么地方，什么时候发挥作用。我们需要读取注解的工具，也就是`创建与使用注解处理器`

注解处理器是一个单独的类