# @Time:2021/5/7 3:08 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from ddt import ddt, data
import unittest


@ddt
class TestDemo(unittest.TestCase):

    @data(*[1, 2, 4])
    def test_add(self, case):
        print("111")
        print(case)
