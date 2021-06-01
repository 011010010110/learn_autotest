# @Time:2021/4/26 4:25 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

import os

# # 新建一个目录/文件夹
# os.mkdir("liuyue")
#
# # 跨级新建目录
# os.mkdir("liuyue/june")

# path = os.getcwd()
# print("获取到的当前路径是：",path)
#
# path_2 = os.path.realpath(__file__)
# print("当前路径是：{0}".format(path_2))

# new_path_1=os.getcwd()+"/python01"
# print(new_path_1)
# os.mkdir(new_path_1)

for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
        os.listdir(os.path.join(os.getcwd(), path))
        print("{0}还需要进一步处理".format(path))
    else:
        print(os.path.join(os.getcwd(), path))
