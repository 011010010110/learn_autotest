# @Time:2021/5/7 5:47 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8
"""
datas = [
    {"user": "python27", "passwd": "lemonban", "check": {"code": 0, "msg": "登录成功"}},
    {"user": "python27", "passwd": "lemonban11", "check": {"code": 1, "msg": "账号或密码不正确"}},
    {"user": "python25", "passwd": "lemonban", "check": {"code": 1, "msg": "账号或密码不正确"}},
]

按行读取数据
    sh.rows = 所有行的数据。list(sh,rows)返回的是一个列表，列表当中的成员是每一行的数据元组

"""

import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "login_cases.xlsx")

from openpyxl import load_workbook
wb = load_workbook(file_path)

sh = wb["login"]

"""
1、先拿到表头数据
2、然后去获取除去表头的每一行的数据，每一行都是一个字典
3、获取到每一行数据以后，再通过角标去获取每一个单元格数据
4、把单元格数据用键值对的方式赋值给titles，构成字典，key为titles，value为单元格数据
"""

# 1、拿到字典的key值，也就是表头
titles = []
for item in list(sh.rows)[0]:  # 遍历第一行中的每一列
    titles.append(item.value)  # 像titles中添加数据
# print(titles)

# 2、把key和value组合到一起，形成一个字典，再把字典放到列表中
# print(list(sh.rows))  # 每一行是个元组，元组里面放的是每一行的单元格
data_list = []
for item in list(sh.rows)[1:]:  # 不要表头，使用切片去掉表头，然后遍历每一行
    value_dict = {}  # 每一行是一个字典value
    # print(item)
    for index in range(len(item)):  # 获取每一行单元格数据，当index在item长度里面时候就去循环
        # print(index, item[index], item[index].value)
        # 把单元格数据用键值对的方式赋值给上面获取到的titles，构成字典，key为titles，value为单元格数据
        value_dict[titles[index]] = item[index].value
    # print(value_dict)

    data_list.append(value_dict)
print(data_list)

