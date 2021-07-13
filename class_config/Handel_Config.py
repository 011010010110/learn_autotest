# @Time:2021/6/1 4:01 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from configparser import ConfigParser
import os


class HandleConfig(ConfigParser):
    def __init__(self, file_path):
        super.__init__()
        self.read(file_path, encoding="utf-8")


# 获取绝对路径
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"conf.ini")
conf = HandleConfig(file_path)

if __name__ == "__main__":
    conf = HandleConfig( "conf.ini")
    conf.get("log", "name")
