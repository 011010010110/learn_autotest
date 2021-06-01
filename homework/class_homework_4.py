# @Time:2021/5/6 8:19 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

# 2、自动贩卖机：只接受1元、5元、10元的纸币，最多不超过10元，饮料只有橙汁、椰汁、矿泉水、早餐奶，
# 售价分别是：3.5元、4元、2元、4.5元，写一个函数来表示贩卖机的功能：用户投钱和选择饮料，并通过判断之后，给用户吐出饮料和找零。
def fanmaiji():
    drinks = {"1":3.5,"2":4,"3":2,"4":4.5}
    total = 0  # 存放购买的总金额
    while True:
        choose = input("请输入你要选的饮料：1为橙汁，2为椰汁，3为矿泉水，4为早餐奶 q:退出")

        if choose in drinks.keys():
            total += drinks[choose]
        elif choose == "q":
            print("退出选择")
            break
        else:
            print("不存在该饮料，请重新选择！")

    pay = 0  # 用户投币金额
    while True:

        money = (input("请投币,只支持 1、5、10金额的金币，按q退出"))
        if money == "1" or money == "5" or money=="10":
            pay += int(money)
            if pay>total:
                print("您一共购买了{0}元饮料，您支付{1}元,找零{2}元".format(total, pay,pay - total))
            elif pay<total:
                print("您一共购买了{0}元饮料，您支付{1}元,还需要支付{2}元".format(total, pay, total-pay))
                break
            else:
                print("您一共购买了{0}元饮料，您支付{1}".format(total, pay))
                break
        elif money == "q":
            print("结束投币")
        else:
            print("该面额暂不支持")

fanmaiji()

