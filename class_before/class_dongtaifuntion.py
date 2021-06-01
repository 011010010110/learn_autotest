# 动态参数/不定长参数
# def make_sadwich(*args):
#     all=""
#     for item in args:
#         all+=item
#         all+=","
#     print("你的三明治包括了"+all)
# make_sadwich("生菜","火腿","培根","牛肉")


# 关键参数  key-value **kwargs  key word
# def kw_function(**kwargs):
#     print(kwargs)

# kw_function(x=1,y=2)

# def add_all_num(a,*L):
#     print("输入的数据为",L)#元组
#     sum=0
#     for i in L:
#         sum += i
#     print("和为",sum)
#     print("a的值为",a)
# add_all_num(1,2,3,4,5)

# 混用
def add_all_num(a=7, *L, **kwargs):
    sum = 0
    for i in L:
        sum += i
    print("和为：", sum)
    print("a的值为", a)
    print("kwargs的值为", kwargs)


add_all_num(1, 2, 3, 4, 5, 6, x=1, y=2)
