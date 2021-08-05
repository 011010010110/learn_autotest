# @Time:2021/8/5 7:03 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import unittest
import os
import requests
from ddt import ddt, data

from class_0730_apiauto.handle_requests import send_requests
from class_0730_apiauto.handle_excel import Test_Handel_Excel

he = Test_Handel_Excel(os.path.join(os.path.dirname(os.path.abspath(__file__)), "api_cases.xlsx"), "注册")
cases = he.test_all_datas()
he.close_file()
for item in cases:
    print(item)


@ddt
class TestRegister(unittest.TestCase):

    @data(*cases)
    def test_register_ok(self, case):
        # case = cases[0]
        expect = eval(case["expected"])
        response = send_requests(case["method"], case["url"], case["request_data"])
        # 断言
        self.assertEqual(response.json()["code"], expect["code"])
        self.assertEqual(response.json()["msg"], expect["msg"])

        # self.assertNotEqual(response.json()["code"], expect["code"])
        # self.assertNotEqual(response.json()["msg"], expect["msg"])
