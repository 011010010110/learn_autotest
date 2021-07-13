# @Time:2021/5/8 6:23 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import os

import class_excel_logger
from HTMLTestRunner import HTMLTestRunner


import unittest

_result = unittest.TestLoader().discover(r"class_excel_logger")

with(open("report.html", "wb"))as fs:
    runner = HTMLTestRunner(fs, title="数据驱动测试报告")
    runner.run(_result)
