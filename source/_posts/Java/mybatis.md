---
title: mybatis 配置使用总结
date: 2019-07-25 00:00:00
tags: [java, note]
categories: Java编程
---

mybatis 学习笔记和基础概念，在spring boot中的使用配置总结

<!-- more -->

## 基础

总共有两种使用方式：1. 无配置文件注解版，这种模式就不需要XML文件了；2. 使用传统的XML文件

2 类型的使用流程总结

流程：

1. 添加依赖

2. 配置spring boot

    整体概述：
    配entity，是一个包，包含实体类
    配mapper，映射文件
    mybatis设置，例如map-underscore-to-camel-case-repository
    src：要有一个实体类，一个DAO接口类(mapper类) -> 由XML做映射


Spring Boot 会自动加载 spring.datasource.* 相关配置，数据源就会自动注入到 sqlSessionFactory 中，sqlSessionFactory 会自动注入到 Mapper 中。
在启动类中添加对 mapper 包扫描 `@MapperScan`

spring boot配置文件

```
mybatis:
  mapper-locations: classpath:/mybatis/mapper/*.xml
  config-location:  classpath:/mybatis/config/mybatis-config.xml
```

配置包括，mapper映射文件，和mybatis配置文件，配置文件是和数据库相关的。这里都是xml相关，mapper映射文件，映射会有多个，映射是接口类的装配，在映射文件中，必须`<mapper namespace="com.yukong.chapter5.repository.UserMapper">`的形式指明接口类是哪一个。

在mybatis的xml配置文件中

```
<typeAliases>
    <package name="com.yukong.chapter4.entity"/>
</typeAliases>
```

这个指明了实体类的包路径，这样在映射xml中就不用写全名了。mybatis配置文件不是必须的，不显示的指定配置参数，那就使用默认的。

接下来就是src源文件了，包括entity实体类包，和mapper接口类包，实体类描述了表的字段，接口类方法描述了对表的操作CURD，具体的操作实现由xml映射文件来实现。

至此，整个配置流程就完成了，需要手动创建数据库，然后就可以使用了。

操作实例：

```java
@Autowired
    private UserMapper userMapper;

@Test
public void save() {
    User user = new User();
    user.setUsername("zzzz");
    user.setPassword("bbbb");
    user.setSex(1);
    user.setAge(18);
    Assert.assertEquals(1, userMapper.save(user));
}
```

通过注解自动装配userMapper，然后给实体类实例赋值，调用userMapper的save方法保存数据

