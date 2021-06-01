# 1、设置一个登陆程序，不同的用户名和对应的密码存储在一个字典里，输入正确的用户名和密码去登陆，
#    字典为：userinfo = {"root":"123","user":"123456","admin":"111"}
# 2、首先输入用户名，如果用户名不存在或者为空，一直提示输入正确的用户名
# 3、当用户名正确的时候，提示去输入密码，如果密码和用户名不正确，则提示密码错误请重新填写
# 4、如果输入错误密码超过三次，中断程序执行
# 5、当输入错误密码时，提示还有几次机会
# 6、当用户名和密码都正确时候，提示登陆成功


userinfo = {"root":"123","user":"123456","admin":"111"}
count = 4  #记录输入次数
while True:
    username = input("请输入用户名：")
    if username in userinfo.keys():    #判断username是否在字典的key
        while count > 0:
            passwd = input("请输入密码：") 
            if passwd in userinfo.values():
                print("登陆成功")
                break
            else :
                count-=1
                print("账号或者密码错误！请重新填写,您还有{0}次输入机会".format(count))
                # break
        break
    #通过判断用户名是否在字典的key里面或者为空
    # elif username not in userinfo.keys() or username == ""
    elif len(username) == 0:    #通过判断账号长度来确定用户是否输入了账号
            print("请输入正确正确用户名")
    else :
        print("账号或者密码错误!请重新填写")
