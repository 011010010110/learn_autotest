# @Time:2021/4/30 9:28 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

# # 1、输出一个直角三角形
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print("")  # print语句会自动换行

# 2、输出一个等腰三角形，每个边都是五个*
# for i in range(1, 6):  # 控制行数
#     # 这个for循环控制空格输出
#     for x in range(1, 6 - i):
#         print(" ", end="")
#
#     # 这个for循环控制*输出
#     for y in range(1,i + 1):
#         print("*", end="")
#     print("")
#
# # 3、99乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print("{0}*{1}={2}".format(i, j, i * j), end="")
#     print("")

# 4、经典冒泡排序，利用for循环完成a=[1,7,4,89,43,2]的冒泡排序。
# 概念：相邻两个元素对比，一般最多比较n-1趟
a = [1, 7, 4, 89, 43, 2]
for i in range(0, len(a) - 1):
    for j in range(i + 1, len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)