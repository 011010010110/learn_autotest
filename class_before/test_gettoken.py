# @Time:2021/3/25 2:57 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from jsonpath import jsonpath
import pytest
import requests


class Test_Recharge():
    # def test_setUp(self):
    #     pass
    #
    # def test_tearDown(self):
    #     pass

    def test_recharge(self):
        url = 'http://www.testingedu.com.cn:8000/index.php?m=Home&c=User&a=do_login&t=0.6533599798088903'
        payload = {
            "username": "13800138006",
            "password": "123456",
            "verify_code": "1111"
        }
        res = requests.post(url, json=payload)
        print(res.json())


if __name__ == '__main__':
    pytest.main(['-vs', 'test_gettoken.py'])
