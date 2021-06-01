# @Time:2021/6/1 4:01 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from configparser import ConfigParser


class HandleConfig(ConfigParser):
    def __init__(self, file_path):
        super.__init__()
        self.read(file_path, encoding="utf-8")


conf = HandleConfig("conf.ini")
conf.get("log", "name")
