# coding:utf-8

import json

"""
文件的创建与写入
open
功能：生成文件对象，进行创建，读写操作
用法：open(path, mode)
参数说明：path:文件路径 mode:操作模式
返回值：文件对象

文件的操作模式之写入
w 创建文件，如果文件有存在且有内容，那么内容会被覆盖
w+ 创建并读取文件
wb 二进制形式创建文件（写入比特类型）
wb+ 二进制形式创建或追加内容
a 追加内容
a+ 读写模式的追加
ab+ 二进制形式读写追加

文件对象的操作方法之读
函数名     参数      介绍
write    Message  写入信息
writelines Message_list  批量写入
close    无       关闭并保存文件

文件的操作模式之读取
r 读取文件
rb 二进制形式读取文件

文件对象的操作方法之写
函数名     参数      介绍
read    无       返回整个文件字符串
readlines  无    返回文件列表
readline   无    返回文件中的一行
mode      无     文件模式
name     无      返回文件名称
closed   无      文件是否关闭
"""

"""
序列化
可序列化的数据类型：number str list tuple dict(最常见)

json模块
函数名     参数      介绍      返回值
dumps     obj     对象序列化  字符串
loads     str     返序列化    原始数据类型
"""

a = 'str类型'
b = 1
c = 2.1
d = [1, 2, 3]
e = {'name': '小猫', 'age': 18}
print(json.dumps(a))
print(json.dumps(b))
print(json.dumps(d))
print(json.dumps(e))

"""
读yaml文件
"""