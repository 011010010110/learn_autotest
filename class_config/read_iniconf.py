# @Time:2021/6/1 3:25 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from configparser import ConfigParser

# 1、实例化
conf = ConfigParser()

# 2、读取配置文件
conf.read("conf.ini", encoding="utf-8")

# 3、读取某一项配置：get  /只能是一项  /全部都是字符串
conf.get("log", "name")

# 读取出来为布尔值
val = conf.getboolean("log", "file_ok")
print(type(val))

# 获取当前section
conf.sections()