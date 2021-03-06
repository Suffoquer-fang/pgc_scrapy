## 小学期实践第二周周报

学号：2017011462 &emsp;&emsp; 姓名：方言

学号：2017011335 &emsp;&emsp; 姓名：何仲凯



### 本周项目进展

1. 完成`爱奇艺视频`信息爬取。

2. 阿里云建立数据库，基本完成设计了数据库表结构。

    具体分为以下几个表：

   - videoitem：主要记录一个视频的各项信息，如`url, title, type...`等。其中，`tags, directors, actors`为多个值组成的列表。
   - tagitem：记录每一个`tag`对应的视频id列表。
   - peopleitem：记录每一个`director`或`actor`对应的视频id列表。

   后两个表，本质上是用于搜索的倒排索引。我们考虑到后续可能要针对视频信息进行搜索，数据库原生支持的`LIKE`模糊搜索可以实现搜索的目的，但是其效率不够高，因此考虑建立倒排索引提高效率。

   

3. 搭建起`scrapy`爬虫完整流程，并且完成对`腾讯视频`和`爱奇艺视频`的视频信息爬取，数据已经在阿里云上持久化入库。

4. 增加了去重过滤器，目前暂定的去重准则是根据`url`进行去重，用于避免重复视频的爬取。考虑到可能会有视频信息的更新，因此之后会修改成对于视频信息完整内容的`Hash`值进行去重。



### 遇到的困难

1. 优酷视频和爱奇艺视频没有提供便利的`sitemap`，因此只能寻找相关api，并且从视频播放页提取相关信息，效率较低，且信息不一定能够正确提取。
2. 小组一名组员目前身处大陆以外地区，针对某些视频网站爬取，有一些大陆未上映的影片的视频信息，导致和大陆地区爬取结果不相同产生一定冲突。



### 下周计划

1. 完成多个网站具体信息的解析和爬取（分工）
2. 搭建完整爬虫自动更新的流程。
3. 建立倒排索引并进行与搜索相关的处理。



### 分工情况

方言：阿里云数据库搭建，整体爬虫框架搭建，数据库表结构设计，腾讯视频信息爬取。

何仲凯：数据库表结构设计，去重过滤器，爱奇艺视频信息爬取。