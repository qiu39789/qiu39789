# coding:utf-8

"""
捕获通用异常：无法确定是哪种异常的情况下使用的捕获方法
try:
    代码块
except Exception as e:
    异常代码块
捕获具体异常：确定是哪种异常的情况下使用的捕获方法
try:
    代码块
except 具体异常类型 as e:
    异常代码块
"""
# ZeroDivisionError: division by zero
try:
    abc = 1 / 0
    print(abc)
except ZeroDivisionError as e:
    print("出错，0不能被整除")
try:
    abc = 1 / 0
    print(abc)
except Exception as e:
    print("报错内容为：%s" % e)
"""
捕获多个异常-方法一：当except代码块有多个的时候，当捕获到第一个后，不会继续往下捕获
try:
    代码块
except 具体异常类型 as e:
    异常代码块
except Exception as e:
    异常代码块
    
捕获多个异常-方法二：捕获到哪种抛出哪种
try:
    代码块
except (具体异常类型, Exception) as e:
    异常代码块
"""

"""
常见异常类型
Exception 通用异常类型（基类）
ZeroDivisionError 不能整除0
AttributeError 对象没有这个属性
IOError 输入输出操作失败
IndexError 没有当前的索引
KeyError 没有这个键值（字典之类的）
NameError 没有这个变量
SyntaxError 语法错误
SystemError 解释器的系统错误
ValueError 传入的参数错误
"""
"""
异常中的finally 
1、无论是否发生异常，一定会执行的代码块
2、在函数中，即使在try或except中进行了return也依然会执行finally语法块
3、try语法至少要伴随except或finally中的一个
"""
"""
自定义抛出异常函数-raise
将信息以报错的形式抛出
用法：
    raise 异常类型(message)   参数 message错误信息  无返回值
"""