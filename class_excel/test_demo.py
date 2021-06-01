# @Time:2021/5/8 11:12 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import os
from openpyxl import load_workbook

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")


wb = load_workbook(file_path)
sh = wb["login"]

data_result = []
# 拿key
titles = []
for item in list(sh.rows)[0]:
    titles.append(item.value)

# 拿value
values = []
for item in list(sh.rows)[1:]:
    for index in item:
        values.append(index.value)

    # 组合成键值对
    res = dict(zip(titles, values))

    res["check"] = eval(res["check"])
    data_result.append(res)


print(data_result)