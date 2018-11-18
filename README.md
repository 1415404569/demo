# search_html
1. 安装mysql数据库，并安装navicat数据库可视化工具或使用以下命令创建数据库并导入ioc.sql

   * **一、mysql创建数据库实例**
   * **使用用户名和密码登陆mysql，在命令行界面输入一下命令**
   * **1、show databases      //显示数据库**
   * **查看需要创建的数据库是否已经存在。**
   * **2、create database ioc//创建数据库ioc**
   * **3、use ioc//进入ioc数据库**
   * **二、通过sql文件将数据表导入到mysql数据库**
   * **1、在cmd命令窗口进入到mysql安装目录，默认为：C:\Program Files\MySQL\MySQL Server 5.5\bin>**
   * **2、输入以下命令：**
   * **mysql -D mrbs -u root -p < d:\\tables.my.sql     //d:\\tables.my.sql为要导入的sql文件及所在目录。注意需要将表格导入到哪个数据库就要用这个数据库的用户名和密码登陆，通过用户名和密码区分数据库。**
   * **3、提示输入root的密码，输入完密码后即会按照导入文件tables.my.sql将相关表格在mysql中root用户对应的数据库中创建。**
   * **三、通过sql文件导入数据（不是创建数据库结构）**
   * **在mysql命令行界面输入**
   * **mysql>use student        //student为导入表的数据库；在数据库中先创建student表**
   * **mysql>source d:\sample-data.sql    //d:\sample-data.sql为需要导入的数据文件。**

2. 安装python3 的环境，建议安装pycharm 软件

   * 安装pytho3 请参考：https://blog.csdn.net/random_w/article/details/78897365

   * 安装pycharm请参考：https://blog.csdn.net/hq_nuan/article/details/83653677

   * 在pycharm中部署项目zhl-project：

     * 先把venv给删了

     * file -> settings

     * ![20180629125949909](C:\Users\lenovo\Desktop\20180629125949909.png)

     * ![20180629130034993](C:\Users\lenovo\Desktop\20180629130034993.png)

     * ![20180629130048180](C:\Users\lenovo\Desktop\20180629130048180.jpg)

     * 地址加上venv ![20180629130105691](C:\Users\lenovo\Desktop\20180629130105691.jpg)

     * 重新配项目环境

       再点“+”![20180629130136128](C:\Users\lenovo\Desktop\20180629130136128.jpg)

     * 手动添加django ![2018062913014967](C:\Users\lenovo\Desktop\2018062913014967.jpg)

     * 等一会显示成功 

3. 然后输入：python manage.py runserver 开启服务，然后直接打开index.html前端页面搜索哈希值，会相应在search_result.html显示信息

