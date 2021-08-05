# @Time:2021/8/5 5:56 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from HTMLTestRunner import HTMLTestRunner
import unittest

result = unittest.TestLoader().discover(r"class_0730_apiauto")

with (open("report.html", "wb"))as fs:
    runner = HTMLTestRunner(fs, title="单接口自动化测试报告")
    runner.run(result)
