# @Time:2021/5/6 11:40 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8
# class_0730_apiauto RobotOne:   #第一代
#     def __init__(self,year,name):
#         self.year = year
#         self.name = name
#
#     def walking_on_palnt(self):
#         print(self.name+"只能在地上行走,不能避开障碍物")
#
#     def robotinfo(self):
#         print("{0}年生产的机器人{1},产自CN".format(self.year,self.name))
#
#
# class_0730_apiauto RobotTwo():  #第二代
#     def __init__(self,year,name):
#         self.year = year
#         self.name = name
#
#     def walking_on_palnt(self):
#         print(self.name+"可以在地上平稳的行走")
#
#     def walking_around_block(self):
#         print(self.name+"可以避开障碍物")
#
#     def robotinfo(self):
#         print("{0}年生产的机器人{1},产自CN".format(self.year, self.name))

class RobotOne:   #第一代
    def __init__(self,year,name):
        self.year = year
        self.name = name

    def walking_on_palnt(self):
        print(self.name+"只能在地上行走,不能避开障碍物")

    def robotinfo(self):
        print("{0}年生产的机器人{1},产自CN".format(self.year,self.name))


class RobotTwo(RobotOne):  #第二代
    # 继承上面的RobotOne类
    def walking_on_palnt(self):
        print(self.name+"可以在地上平稳的行走")

    def walking_around_block(self):
        print(self.name+"可以避开障碍物")

#实例化参数
r2 = RobotTwo("1002", "xxxx")
r2.robotinfo()
r2.walking_on_palnt()

# r1 = RobotOne("111","sss")
# r1.robotinfo()