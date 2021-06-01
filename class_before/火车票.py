# @Time:2021/3/25 4:38 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from pip._vendor.distlib.compat import raw_input

x = raw_input("请输入:")

if float(x) < 1.2:
    print("你输入的身高是" + x + "，免票")
elif float(x) < 1.5 and x > 1.2:
    print("你输入的身高是" + x + "，半票")
else:
    print("你输入的身高是" + x + ",全票")
# print(x)
