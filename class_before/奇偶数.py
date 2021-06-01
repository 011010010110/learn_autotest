# @Time:2021/3/25 4:51 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8
"""
for循环
"""
# 偶数
a = 0
for i in range(0, 100):
    if i % 2 == 0:
        print(i)
        a += i
print('\n偶数是：', a, '\n')

# 奇数
b = 0
for i in range(0, 100):
    if i % 2 != 0:
        print(i)
        b += i
print('\n奇数是：', b)

"""
while循环
"""
a = 100
s = 0

while a > 0:
    a = a - 1
    if a % 2 == 0:
        print(a)
        s += a
print('\n偶数和是：', s)

print('\n')

b = 100
u = 0
while b > 0:
    b = b - 1
    if b % 2 != 0:
        print(b)
        u += b
print('\n奇数和是：', u)

