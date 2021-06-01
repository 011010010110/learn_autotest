# # a = 1  #全局变量
# def add(b):
#     a=5  #局部变量
#     print(a+b)
# add(10)
# print(a)

# global
a = 1


def add(b):
    global a  # 声明a为全局变量
    a = b + 5  # 赋值运算
    print(a + b)


add(1)
