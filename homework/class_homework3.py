# 输入num为四位数，对其按照如下的规则进行加密：
# 1）每一位分别加5，然后分别将其替换为该数除以10后取余的结果
# 2）将该数的第1位和第4位互换，第二位和第三位互换
# 3）最后合起来作为加密后的整数输出

num = input("请输入4位数：")  # input:从控制台获取数据，获取的数据为字符串
new_num = ''  # 定义一个新的字符串函数
if len(num) == 4:
    for item in num:
        # print(item)  #分别打印输入的字符串
        # print(int(item))  #强转成整型
        integers = int(item) + 5  # 强转成整型并且加五
        remainders = integers % 10  # 取余操作
        # print(remainders)
        new_num += str(remainders)  # new_num这个字符串函数对强转成str的remainders函数进行字符串的拼接

    # 第二条要求就是倒序输出，可以采用切片实现
    last_result = new_num[::-1]  # 切片倒序输出
    print("加密后的解果为：", last_result)
else:
    print("您输入的数字不是四位！")
