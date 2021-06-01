# @Time:2021/5/8 10:33 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

# zip:打包函数

import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")

from openpyxl import load_workbook
wb = load_workbook(file_path)

sh = wb["login"]

data_result = []  # 存储excel所有数据

# 拿key
titles = []
for item in list(sh.rows)[0]:
    titles.append(item.value)

for item in list(sh.rows)[1:]:  # 遍历数据行
    values = []
    for index in item:  # 获取每一行的数据
        values.append(index.value)
    res = dict(zip(titles, values))  # titles和每一行数据通过键值对打包成字典
    res["check"] = eval(res["check"])  # 将上面生产字典中的check的字符串，转换成字典对象
    data_result.append(res)  # 追加

print(data_result)

wb.close()
