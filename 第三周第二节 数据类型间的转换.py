# coding:utf-8

"""
# 将自身数据类型变成新的数据类型，并拥有新的数据类型的所有功能的过程即为类型转换
# 字符串和数据之间转换的要求
# str -> number 要求字符串必须全是数字组成

字符串和数字之间的转换函数：

整型转字符串用str()
浮点型转字符串用str()
字符串转整型用int()
字符串转浮点型用float()
"""
int_str = "123"
float_str = "3.14"
print(int(int_str))  # 123
print(float(float_str))  # 3.14
# print(int(float_str)) 报错
print(float(int_str))  # 123.0
new_number = 456
print(str(new_number), type(str(new_number)))

"""
字符串与列表之间的转换
1、字符串转列表的函数 split 将字符串以一定规则切割转成列表
  string.split(sep = None, masplit = -1) 
  sep:默认切割的规则符号，默认为空格，如果字符串无空格则不分割生成列表
  maxsplit:根据切割符号切割的次数，默认-1无限制
  返回值，返回一个列表
2、列表转字符串的函数 join 将列表按照一定规则转成字符串
  "sep".join(iterable)
  sep:生成字符串用来分割列表每个元素的符号
  iterable:非数字（一个数字也不行）类型的列表或元组或集合（列表元组和集合中的成员只能是字符串）
  返回值：返回一个字符串
"""
info = "my name is libai"
info_list = info.split()
print(info_list)  # ['my', 'name', 'is', 'libai']
a = "abc"
a_list = a.split()
print(a_list)  # ['abc']
b = "a,b,cd"
print(b.split(','))  # ['a', 'b', 'cd']
c = "a|b|c|d|e"
print(c.split('|', 1))
# ===================================================================
test = ['a', 'b', 'c']
new_test = "|".join(test)
print(new_test)  # a|b|c
print("|".join(('str', 'numb')))

# sorted可以给任意数据类型排序，并返回一个列表
sort_str = 'abcdxtywf'
new_list = sorted(sort_str)
print(new_list)  # ['a', 'b', 'c', 'd', 'f', 't', 'w', 'x', 'y']
print(''.join(new_list))  # abcdftwxy

# 比特类型（二进制的数据流--bytes） 一种特殊的字符串，字符串前+b标记
bt = b'my name is libai'
print(type(bt))
print(bt.replace(b'libai', b'xiaobai'))  # b'my name is xiaobai'

# encode 将字符串转成比特 string.encode(encoding='utf-8', errors='strict')
#        参数：encoding:转换成的编码格式如ascii,gbk,默认utf-8
#              errors:出错时的处理方法，默认strict,直接抛出错误，也可以选择ignore忽略错误
#              返回值：返回一个比特类型
# decode 将比特转成字符串 bytes.decode(encoding='utf-8', errors='strict')
#        参数：encoding:转换成的编码格式如ascii,gbk,默认utf-8
#              errors:出错时的处理方法，默认strict,直接抛出错误，也可以选择ignore忽略错误
#              返回值：返回一个字符串类型
vvv = 'hello 李白'
by = vvv.encode()
print(by, type(by))
new_vvv = by.decode()
print(new_vvv, type(new_vvv))

# 元组、列表、集合间的转换
"""
列表转集合 set
列表转元组 tuple
元组转集合 set
元组转列表 list
集合转列表 list
集合转元组 tuple
"""