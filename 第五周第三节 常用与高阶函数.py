# coding:utf-8

import hashlib
import base64
import logging
import random
"""
hashlib包   难破解 不可逆
常用加密方法
函数名     参数      介绍      返回值
md5       byte    MD5加密   hash对象
sha1      byte      加密    hash对象
sha256      byte      加密    hash对象
sha512      byte      加密    hash对象
"""
str = '123'

print(str.encode('utf-8'))

"""
base64包    通用型  可解密
常用加密方法
函数名            参数      介绍      返回值
encodestring   byte     base64加密   byte
decodingstring   byte     base64解密   byte
encodebytes  byte     base64加密   byte
decodingbytes   byte     base64解密   byte
"""

"""
日志模块
日志的等级
debug   可替代print
info    程序行为信息，比如程序执行到哪了
warnning 程序可能存在的风险
error   程序报错
critical 非常严重程序错误，较少使用

logging模块的使用
logging.basicConfig
参数名    作用
level   日志输出等级
format  日志输出格式
filename  存储位置
filemode  输出模式

format具体格式
格式符              含义
%(levelname)s   日志级别名称
%(pathname)s   执行程序的路径
%(filename)s   执行程序名
%(lineno)d   日志的当前行号
%(asctime)s   打印日志的时间
%(message)s   日志信息
format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
logging.info('123')
logging.error('123')

"""
python中的虚拟环境工具
Virtualenv
pyenv
"""
"""
python常用内置函数
函数名     参数        介绍      返回值
abs      Number    返回数字绝对值  正数字
all     List        判断列表内容是否全是true   Bool
help    object      打印对象的用法   无
enumerate iterable   迭代时记录索引  无
input   Str          命令行输出消息  Str
isinstance  Object,type   判断对象是否是某种类型 Bool
type     Object       判断对象的类型
vars    instance   返回实例化的字典信息  dict
dir     object     返回对象中所有可用方法和属性 List
hasattr Obj,key    判断对象中是否有某个属性  Bool
setattr Obj,key,value  为实例化对象添加属性和值   无
getattr  obj,key    通过对象获取属性     任何类型
any     Iterable    判断内容是否有true值  Bool
"""

"""
python的随机模块random
random.random 随机返回0-1之间的浮点数
random.uniform 产生一个a,b区间的随机浮点数
random.randint 产生一个a,b区间的随机整数
random.choice 返回对象中的一个随机元素（比如返回列表）
random.sample 随机返回对象中指定的元素（比如随机返回列表中的多少个元素）
random.randrange 获取区间内的一个随机数
"""
print(random.random())

"""
生成迭代器
iter(iterable)   iterable可迭代的数据类型
迭代器的使用
nex(iterator)    iterator迭代器对象


"""

"""
python高级函数
filter 对循环根据过滤条件进行过滤
filter(func,list) func:对list每个item进行条件过滤的定义 list:需要过滤的列表
map
reduce
"""
