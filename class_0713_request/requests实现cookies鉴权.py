# @Time:2021/7/13 5:54 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

"""
Session类：创建一个会话对象。
"""
import requests

# # 第一步 实例化Session对象
# s = requests.Session()
#
# print("登陆之前的cookie：", s.cookies)
# # 第二步 - 登陆，得到cookies鉴权
# login_url = "https://www.ketangpai.com/UserApi/login"
# login_datas = {"email": "2735259470@qq.com",
#                "password": "ly99527..",
#                "remember": 0}
# response = s.post(login_url, data=login_datas)
# print("登陆响应的cookies:", response.cookies)
# print("登陆之后的cookies:", s.cookies)  # 主动会将响应的set-cookies添加到创建的s对象当中
#
# # 第三步 获取用户设置信息
# userinfo_url = "https://openapiv5.ketangpai.com/UserApi/getUserVipSetting"
# res = s.get(userinfo_url)
# print(res.json())

# 第一步：登陆，等到Cookies鉴权
login_url = "https://www.ketangpai.com/UserApi/login"
login_datas = {"email": "2735259470@qq.com",
               "password": "ly99527..",
               "remember": 0}

# 第二步，获取用户信息
userinfo_url = "https://openapiv5.ketangpai.com/UserApi/getUserVipSetting"
res = requests.post(login_url, data=login_datas)

# 主动获取cookies
cookies = res.cookies
print(cookies)

# 第二步，获取用户信息
res = requests.get(userinfo_url, cookies=cookies)
print(res.json())
