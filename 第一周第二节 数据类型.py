# coding:utf-8

# python数据类型
"""
数字（整型int、浮点型float）、
字符串str、 字符串不可改变（指内存地址）
布尔bool、
    int 0 -> False 非0 -> True
    float 0.0 -> False 非0.0 -> True
    str "" -> False 非空 -> True
    经常用0,1替代False和True
空None、
    不属于任何数据类型，就是空类型
    固定值：None
    属于False范畴
    如果不确定数据类型可用None
列表list   []、 列表在创建后进行修改内存地址不会改变
元组tuple  ()、
    元组占用资源比列表小因为列表可变，元组创建后不可变，其他和列表一样
    如果元组中只有一个元素并且元素后没有加逗号，那么type出来就是那个元素本身的类型
字典dict   {}、
    字典是由多个键key及对应的值value所组成的数据类型
    key支持字符串，数字和元组，不支持列表
    value支持所有python的数据类型
    字典中的key是唯一的
    内置函数的用法和列表元组一样，max和min会找key

内置函数
type()查看数据类型
id()查看内存地址
len()查看字符串长度   ==> 可用来限制字符串长度，如设置密码
in/not in 成员运算符：判断数据中是否有想要的成员

max函数返回数据中最大的成员
max(数据) ==> print(max("今天是1月3日!")) 返回的最大值是月
因为中文符号>字母>数字>英文符号 中文按拼音首字母算
min函数返回数据中最小的成员
min(数据) ==> print(max("今天是1月3日!")) 返回的最小值是!
因为英文符号最小

"""
count = 1000
result = type(count)
print(result)
value = 3.1415
print(type(value))
print(type(50))
print(type(6.0))  # float
print(type(0.00))  # float
#  ========================================================
title = "春游"
class_count = 51
boys = 28
girls = 23
if __name__ == "__main__":
    print(title)
    print("班级共有", class_count, "人")
    print("男生有", boys, "人")
    print("女生有", girls, "人")
    text = "五大三"
    print("文字是:", text)
    print("文字是%s，标题是%s" % (text, title))
    print("123" + str(123))
    print(type(int(2.1)))
    abcd = int(2.6)  # 并非四舍五入，直接去掉小数点后的数字
    print(abcd)
#  ========================================================
name = "小明"
print(id(name))
name = "李白啊"
print(id(name))

print(len(name))
#  ========================================================
score = "今日已获取43积分！"
print("积分" in score)
print("43" not in score)
info = "python is a good code"
print(max(info))
print(".", min(info), ".")  # 最小值是空格
#  ========================================================
a = None
print(bool(a))
a = True
print(type(a))
#  ========================================================
str_array = ["qwe", "qwe", "df"]
int_array = [1, 3, 2, 4]
float_array = [1.1, 1.2]
list_array = [[1, 2, 3], [4, 5, 6]]
mix_array = [1, "::", True, None]
print(1 in [1, 2, 3, 4])
print(max([1, 2, 3, 4]))   # max min在列表中使用，列表元素不能是多类型
print(min([1, 2, 3, 4]))
none_list = [None, None, None]
print(bool(none_list))  # 列表非空为True
print(bool([]))  # 列表空为False
#  ========================================================
#  元组
print("元组")
list_tuple = ([1, 2, 3], [4, 5, 6])  # 元组中可以嵌套列表但是创建完成后不可修改
tuple_list = ([1, 2, 3])
print(type(tuple_list))
tuple_list1 = ([1, 2, 3], )
print(type(tuple_list1))
#  ========================================================
#  字典
person = {"name": "小米", "age": 18}

"""
赋值运算符
=  +=  -+  *=  /=  %=  **=（幂）  //=（整除）
"""
a, b, c = 1, 2, 3
# a /= b
# print(a)  # 0.5
a //= b
print(a)  # 0

"""
b kb mb gb
1024相差量

字符串和数字做乘法
    字符串无法和字符串做乘法
    字符串只可以和数字做乘法
    列表和元组也可以和数字做乘法但是做完乘法的列表和元组已经不是原来的了
    字典不支持乘法
"""
name = "李白"
print(name * 3)  # 李白李白李白
print([1, 2, 3] * 3)

"""
比较运算符
    ==  ！=  >  <  >=  <=  <>（判断是否不等于，python3已弃用）
身份运算符
    is（判断存储单元是否相同）  is not（判断存储单元是否不同）

"""

#  定义超长字符串的方法
info1 = """
11111111111111111111111111111111111111111111111
qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
qweqwewqew
"""
info2 = ('11111111111111111111111111111111111'
         '111111111111111111111111111'
         'qwwwwwwwwwwwwwwwwwwwwwwwww')
print(info1)
print(info2)
