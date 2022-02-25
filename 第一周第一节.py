# coding:utf-8  头注释

import os

"""（三个单引号或双引号）
注释
"""
print('1111111')
"""
两种方法，自己熟的是拼接字符串，下面的好用
"""
# result = input("请输入一些内容")
# result1 = input("请输入")
# print("结果1是%s，结果2是%s" % (result, result1))

# 变量占用内存
"""
建议变量命名：
dog_exits
username
is_sleep
"""
a, b, c = 1, 2, 3
print(a, b, c)

price = 8.9
weight = 5
money = price * weight
print("香蕉总金额为：%s" % money)  # 这里无视了类型
print("香蕉总金额为：" + str(money))

user_name = "小红"  # 这是一个姓名变量
age = 20  # 这是一个年龄变量
if __name__ == "__main__":  # 一般放最下面
    print("姓名：%s 年龄：%s" % (user_name, age))
