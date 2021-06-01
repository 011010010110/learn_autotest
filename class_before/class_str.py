# @Time:2021/4/14 6:15 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8
# s = 'hello!'
# print(len(s))  # 统计数据长度
# print(s[-1])
# print(s[1:5:2])
# print(s[4:])
# print(s[::-1])
# print(s[-1::-1])
# print(s.split("l",1))
# new = s.replace('l','@',1)
# print(new)
# print(len(s))
# new = s.strip()
# print(new)
# print(len(new))
# s_1='人生苦短'
# s_2='我选Python'
# print(s_1+s_2)
# age=21
# name='刘岳'
# print("{1}毕业以后是{1}岁".format(name,age))
# print("%s毕业以后是%d岁"%(name,age))
# a=[1,0.02,'hello',[1,2,3],True]
# print(a[0:5:2])
# a=[1,0.02,'hello',[1,2,3],True]
# a.append("刘岳")
# print("a列表的值{}".format(a))
# a=[1,0.02,'hello',[1,2,3],True]
# a.insert(2,"刘岳")
# print("a列表的值{}".format(a))
# a = (1,0.02,'hello',[1,2,3],True)
# a[3].pop()
# print(a)
# a=([1],)
# print(type(a))
# a={
#     "class":1702,
#     "name":"刘岳",
#     "sex":"man",
#     "source":[2,3,4,5],
#     "t_age":20,
#     "class1":"python1"
# }
# print(a["source"])

# 定义一个字典a
# a={
#     "class":1702,
#     "name":"刘某人",
#     "sex":"man",
#     "source":[2,3,4,5],
#     "t_age":20,
#     "class112313":"python1"
# }
# res=a.pop("sex")    #a字典使用pop函数删除key为“sex”的键值对，然后把删除后的字典值重新赋值给res
# #预期输出为一个新的字典，与原字典a相比删除了“sex”：“man”这个键值对，即：
# # {
# #   "class":1702,
# #   "name":"刘某人",
# #   "source":[2,3,4,5],
# #   "t_age":20,
# #   "class112313":"python1"
# # }
# print(res)   #但是实际输出的为a里面key为“sex”的value值，即“man”

# #但是以下被注释掉的部分输出了正确的值，这两种写法不一样吗？
# # a.pop("sex")
# # # res=a
# # print(res)

# 定义一个字典a
# a={
#     "class":1702,
#     "name":"刘某人",
#     "sex":"man",
#     "source":[2,3,4,5],
#     "t_age":20,
#     "class112313":"python1"
# }
# a.pop("sex") #pop一个key以后，直接打印这个key所在的字典的变量，就会输出这个变量剩下的字典值
# print(a)

# res=a.pop("sex")  #pop字典里面的key，然后将pop后值赋值给一个新的变量，新变量如果被打印，输出的值就是这个key对应的value
# print(res)

# a={
#     "class":1702,
#     "name":"刘某人",
#     "sex":"man",
#     "source":[2,3,4,5],
#     "t_age":20,
#     "class112313":"python1"
# }
# a["age"]=20
# print(a)

a = {
    "class": 1702,
    "name": "刘某人",
    "sex": "man",
    "source": [2, 3, 4, 5],
    "t_age": 20,
    "class112313": "python1"
}
a["name"] = "liuyue"
print(a)
