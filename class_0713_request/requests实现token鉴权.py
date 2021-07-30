# @Time:2021/7/13 5:54 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import requests

headers = {'X-Lemonban-Media-Type': 'lemonban.v2'}

login_url = "http://api.lemonban.com/futureloan/member/login"
login_datas = {"mobile_phone": "13845467789", "pwd": "1234567890"}
# 拿token
res = requests.post(login_url, json=login_datas, headers=headers)
#

# 提取token
res_dict = res.json()
token = res_dict["data"]["token_info"]["token"]
member_id = res_dict["data"]["id"]
# print(token)

# 第二步，充值   将token添加到请求头中，
headers["Authorization"] = "Bearer {}".format(token)
recharge_url = "http://api.lemonban.com/futureloan/member/recharge"
recharge_data = {"member_id": member_id, "amount": 2000}
res = requests.post(recharge_url, json=recharge_data, headers=headers)
print(res.json())
