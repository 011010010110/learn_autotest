# @Time:2021/7/13 1:22 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

"""
1、接口地址
2、请求方法
3、请求参数
4、响应数据

get:param
没有请求体，parma就是追加在url后面的查询参数
接口地址？key=value1&key=value2....
get请求不一定有请求参数

post: data,json
请求体
data：字典。对应的默认body格式：application/x-www-form-urlencoded
json：字典。对应的默认body格式：application/json

"""

import requests

# requests.Response
url = "http://api.lemonban.com/futureloan/member/resister"
data = {"mobile_phone": "18600001111", "pwd": "123456789"}
headers = {'X-Lemonban-Media-Type': 'lemonban.v2'}

res = requests.post(url, json=data, headers=headers)

# 响应状态码
print(res.status_code)
# 响应投
print(res.headers)
# 响应体
body = res.text
print(body)

# 响应体转换为pyhton字典
body_j = res.json()
print(body_j)
print(type(body_j))

