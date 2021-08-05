# @Time:2021/7/30 3:26 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import unittest
import os
from ddt import ddt, data

from class_0730_apiauto.handle_requests import send_requests
from class_0730_apiauto.handle_excle import Test_Handel_Excel

he = Test_Handel_Excel(os.path.join(os.path.dirname(os.path.abspath(__file__)), "api_cases.xlsx"), "注册")
cases = he.test_all_datas()
he.close_file()


# for item in cases:
#     print(item)

@ddt
class TestRegister(unittest.TestCase):

    @data(*cases)
    def test_register_ok(self, case):
        # case = cases[0]
        expected = eval(case["expected"])
        # 测试数据发送请求
        response = send_requests(case["method"], case["url"], case["request_data"])

        self.assertNotEqual(response.json()["code"], expected["code"])
        self.assertNotEqual(response.json()["msg"], expected["msg"])

