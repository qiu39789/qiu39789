# coding:utf-8

# 函数就是将一件事情的步骤封装在一起并得到最终结果 函数名代表了这个函数要做的事情 函数体是实现函数功能的流程

# def 定义函数
# def name(args...):
#   函数体
#   返回值

# 函数结果的返回 return
# 将函数结果返回的关键字 return
# 只能在函数体中使用，return支持返回所有的python类型 有返回值的函数可以直接赋值给一个变量
# return代表函数的结束 下面的代码不会再执行

def add(a, b, c=1):
    return a + b + c


result = add(1, 2)
print(result)  # 4
result = add(1, 2, 6)
print(result)  # 9

# 参数规则
# def add(a, b=1, *args, **kwargs) 参数的定义从左到右依次是 必传参数 默认参数 可变元组参数 可变字典参数

# 全局变量 在python脚本最上层代码块的变量 全局变量可以在函数内被读取使用
# 局部变量 在函数体内定义的变量 局部变量无法在函数体外使用
# global  将全局变量可以在函数体内进行修改 用法 global 全局变量名
# 工作中，不建议使用global对全局变量进行修改
name = "libai"


def changename():
    name = "xiaoming"
    print(name)  # xiaoming


changename()
print(name)  # libai

# 递归函数 一个函数不停的将自己执行 避免滥用递归 会导致内存溢出
# def test(a):
#   print(a)
#   return test(a) 通过返回值 直接执行自身函数

# 匿名函数 lambda 定义一个轻量化的函数 即用即删除，很适合需要完成一项功能，但是此功能只在此一处使用
# 定义方法
# 无参数
# f = lambda : value
# f()
# 有参数
# f = lambda x,y: x*y
# f(3,4)

f = lambda: 1
print(f())

f = lambda x, y: x + y
print(f(1, 2))
