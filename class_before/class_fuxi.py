# -*- encoding: utf-8 -*-
# -*- python vsersion: 3.9 -*-
'''
@作者    :刘岳
@时间    :2021/04/22 01:56:04
@邮箱    :liuyue@soyoung.com
'''

# 练习：求1-100的整数合，将该功能封装为一个函数
# 思路：
# 1、实现要求功能
# 2、封装成函数
# 3、函数具有复用性
# def add_num(n, m, k):
#     sum = 0
#     for i in range(n, m):
#         sum += i
#     print("最后的结果为{0}".format(sum))


# add_num(1,101,1)
# add_num(m=101,n=1,k=1)

# def add_numm(n, m=1, k=2):  # 形参/位置参数
#     sum = 0
#     for i in range(m, n, k):
#         sum += i
#     # print(sum)
#     return sumπ

# add_numm(10)  # 10赋值给了n
# add_numm(10, 4)  # 10赋值给了m，4赋值给了k
# add_numm(10, k=4)  # 10赋值给m，4赋值给k，n有默认值为1

# def add_numm(n, m=1, k=2):  # 形参/位置参数
#     sum = 0
#     for i in range(m, n, k):
#         sum += i
#     return sum


# def add_num(n,m=1,k=2):
#     for i in range(m,n,k):
#         sum=0
#         sum+=i
#     return sum +10
# print(add_num(10,k=4))
# def add_num(a,b):
#     return(a+b)
# print(add_num(1,3)+10)
# def add_num(a,b):
#     print(a+b)
# add_num(1,3)+10
