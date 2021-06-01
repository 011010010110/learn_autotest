# 写函数，检查传入列表的长度，如果大于2，那么仅仅保留两个长度的内容，并将新内容返回
def check_list(a):
    if len(a) > 2:
        new_list = a[0:2]
    else:
        new_list = a
    return new_list


# a = [1,3]
# now_list=check_list(a)
# print(now_list)
L = [1, 2, 2]
now_list = check_list(L)
print(now_list)
