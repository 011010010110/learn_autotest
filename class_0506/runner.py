# @Time:2021/5/7 10:00 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8



from class_0506.test_login import TestLogin
from class_0506.test_register import TestDemo

# 从start_directory这个目录下开始，搜索所有的测试用例，并且加载到测试套件中。
# 1、从指定目录搜索
# 2、文件过滤规则：以文件名匹配：test*.py
# 3、在文件当中过滤用例：继承了unittest.TestCase用例类，类当中以test_开头的函数

import unittest
s = unittest.TestLoader().discover(r"/Users/liuyue/Desktop/刘岳/tokendemo")
# print(type(s))
# print(s)

# 用text方式呈现测试报告
# runner = unittest.TextTestRunner()
# runner.run(s)  # 这里的参数为上面的参数

# 用HTML方式呈现测试结果
from HTMLTestRunner import HTMLTestRunner

# 创建一个HTML文件，以写的模式打开，支持中文
with open("report.html", "wb") as fs:
    # 运行测试用例，将结果写入html中
    runner = HTMLTestRunner(fs, title="自动化测试报告")
    runner.run(s)



















# 1、实例化测试套件TestCase
# s = unittest.TestSuite()

# # 添加一个用例，只能添加一个
# s.addTest(TestLogin("test_login_ok"))  #addTest("用例名")添加一个测试用例
#
# # 添加多个用例,可以写多个，需要写成列表形式
# s.addTests([TestLogin("test_login_ok"),TestLogin("test_login_wrong_passwd")])
