# @Time:2021/5/6 4:15 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8


import unittest
from random import random

from ddt import ddt, data
import os

from class_excel_logger.handle_excel import Test_Handel_Excel
from class_0506.login import login_check
from class_excel_logger.my_logger import mylogger

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")
exc = Test_Handel_Excel(file_path, "login")
cases = exc.test_all_datas()
# cases = exc.test_read_titles()
exc.close_file()


@ddt
class TestLogin(unittest.TestCase):

    @data(*cases)
    def test_login(self, case):  # 定义case函数来接收数据
        mylogger.info("==============================开始测试==============================")
        mylogger.info("测试数据为：{}".format(case))
        res = login_check(case["user"], case["passwd"])  # 拆包
        # 断言:实际结果与预期结果相对比
        try:
            self.assertEqual(eval(case["check"]), res)
        except AssertionError:
            mylogger.exception("断言失败，用例不通过")
            raise
        else:
            mylogger.info("断言成功，用例通过")
        mylogger.info("==============================测试结束==============================")
