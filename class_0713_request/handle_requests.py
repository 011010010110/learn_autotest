# @Time:2021/7/14 6:43 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

"""
基于项目做定制化封装

1、鉴权：token
2、项目通用请求头
3、请求体格式：application/json

"""
import requests


def __handle_header(token=None):  # 私有化
    """
    处理请求头。加上项目中必带的请求头。如果有token，加上token
    :param token:token值
    :return:headers字典
    """
    headers = {"X-Lemonban-Media-Type": "lemonban.v2",
               "Content-Type":"application/json"}
    if token:
        headers["Authorization"] = "Bearer {}".format(token)
    return headers


def send_requests(method, url, data=None, token=None):
    # 得到请求头
    headers = __handle_header(token)
    # 根据请求类型，调用请求方法
    method = method.upper()  # 小写字母转写大写
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
