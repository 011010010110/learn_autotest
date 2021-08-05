# @Time:2021/7/30 3:30 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import requests


def handle_header(token=None):
    headers = {"X-Lemonban-Media-Type": "lemonban.v2",
               "Content-Type": "application/json"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers


def send_requests(method, url, data=None, token=None):
    """

    :param method:
    :param url:
    :param data: 字典形式的传参
    :param token:
    :return:
    """
    headers = handle_header(token)
    method = method.upper()
    if method == "GET":
        res = requests.get(url, data, headers=headers)
    else:
        res = requests.post(url, json=data, headers=headers)
    return res


if __name__ == '__main__':
    login_url = "http://api.lemonban.com/futureloan/member/login"
    login_datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}
    res = send_requests("POST", login_url, login_datas)
    token = res.json()["data"]["token_info"]["token"]

    recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
    recharge_data = {"member_id": 200119, "amount": 2000}
    res = send_requests("post", recharge_url, recharge_data, token)
    print(res.json())
