# @Time:2021/4/29 4:25 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8
import os

try:
    os.mkdir("刘岳")
except OSError as e:  # 把错误存储到e变量中
    print("错误为：{0}".format(e))
    file = open("error.txt", "a+")
    file.write(str(e))
    file.close()
