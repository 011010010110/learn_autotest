# @Time:2021/5/6 12:14 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8
# 1）创建一个名为User的类：其中包括属性first_name和last_name，还有其他几个自我介绍通常会储存的属性，
# 自己定义，均需要放在初始化函数里面
# 2）在类User中定义一个名为describe_user()的方法，打印用户信息
# 3）在定义一个名为greet_user()的方法，他向用户发出个性化问候，并对每个实例调用上面两个方法。

class User():
    def __init__(self,first_name,last_name,age,sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print("姓{0},名{1},年龄{2},性别{3}".format(self.first_name,self.last_name,self.sex,self.age))

    def greet_user(self):
        print(self.first_name+self.last_name+"你好")

u1 = User("liu","yue","22","man")
u1.describe_user()
u1.greet_user()