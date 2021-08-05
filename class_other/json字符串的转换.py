# @Time:2021/8/4 7:28 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

"""
null
互相转换
None
"""
import json

# json转换成字典
ss = '{"flag":null,"mobile":"12ed3445"}'
ss_dict = json.loads(ss)
print(ss_dict)

# 字典转换成json
ss = {"flag": None, "mobile": "12ed3445"}
ss_json = json.dumps(ss)
print(ss_json)
