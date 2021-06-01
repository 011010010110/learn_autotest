# @Time:2021/5/6 4:15 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

"""
定义测试类，继承unittest.Testcase
在测试类当中，以test_开头，定义测试函数
每一个test_开头的函数，就是一个测试用例
编写用例：
    1、测试数据
    2、测试步骤
    3、断言：测试结果与预期结果对比
       AssertionError:断言失败
       assert 表达式(True表示通过，False表示失败)
       self.assertXXXX()

    4、前置后置(fixture) —— 前置条件、后置工作
        1)setUp、teardown —— 类下面的每一个用例执行之前，会执行setUp
                            在每一个用例执行之后，会执行teardown
                            setUp——>测试用例——>teardown

        2)setUpClass、teardownClass —— 类里面的第一个用例执行之前，执行setUpClass
                                        类里面的第一个用例执行之后，执行teardownClass


AssertionError:断言失败，是unittest框架识别测试用例失败的标识之一。

表达用例 —— 收集用例 —— 执行用例 —— 生成报告

"""

import unittest
from class_0506.login import login_check
import ddt

datas = [
    {"user": "python27", "passwd": "lemonban", "check": {"code": 0, "msg": "登录成功"}},
    {"user": "python27", "passwd": "lemonban11", "check": {"code": 1, "msg": "账号或密码不正确"}},
    {"user": "python25", "passwd": "lemonban", "check": {"code": 1, "msg": "账号或密码不正确"}},
    # {"user": "", "passwd": "lemonban11", "check": {"code": 1, "msg": "所以的参数不能为空"}},
    # {"user": "Python6", "passwd": "", "check": {"code": 1, "msg": "所以的参数不能为空"}}
]


@ddt.ddt
class TestLogin(unittest.TestCase):

    @ddt.data(*datas)
    def test_login(self, case):  # 定义case函数来接收数据
        res = login_check(case["user"], case["passwd"])  # 拆包
        self.assertEqual(case["check"], res)

