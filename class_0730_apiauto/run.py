# @Time:2021/8/5 7:59 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from HTMLTestRunner import HTMLTestRunner

import unittest

EndResult = unittest.TestLoader().discover(r"class_0730_apiauto")
print("1111")

with(open("report.html", "wb"))as fs:
    runner = HTMLTestRunner(fs, title="单接口测试报告")
    runner.run(EndResult)
