# coding:utf-8
import sys

from animal.cat import action as cat_action  # 通过as重命名就不用担心重名的问题
from animal.dog import action as dog_action
from animal.dog.action import jump as dog_jump  # 导入具体函数
from animal.cat.action import jump as cat_jump
import animal.main
from animal import main
import datetime
import time
import os

"""
包就是文件夹，包中还可以有包，也就是子文件夹
每个py文件都是一个模块，每个放py文件的文件夹就是包
__init__.py是每一个python包里必须存在的文件

包的导入 import：将python中的某个包（或模块）导入到当前的py文件中
用法：import package   package为被导入的包（或模块）的名字  这个只会拿到对应包下__init__中的功能或当前模块下的功能

模块的导入 from..import..
功能：通过从某个包找到对应的模块
用法：from package import module   package为来源的包名 module为包中的目标模块
"""

print(cat_action.run())
print(dog_action.run())
print(dog_jump())
print(cat_jump())
print(animal.main.animal())
print(main.animal())

"""
python中的时间包1 datetime

可百度时间格式字符，查找所有时间格式字符
"""
print(datetime.datetime.now())  # 获取当前时间
before_one_day = datetime.timedelta(days=1)  # 获取一天前
yestoday = datetime.datetime.now() - before_one_day
print(yestoday, type(yestoday))

yestoday_str = yestoday.strftime('%Y-%m-%d %H:%M:%S')
print(yestoday_str, type(yestoday_str))

str_date = '2022-10-10 13:20:23'
data_obj = datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
print(data_obj, type(data_obj))

"""
python中的时间包2 time
时间戳的部分 跳过了
可百度时间格式字符，查找所有时间格式字符
"""
# time.sleep(2)  # 程序暂停执行2秒
print(time.localtime())
str_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(str_time)
ptime = time.strptime('2022-03-09 14:07:12', '%Y-%m-%d %H:%M:%S')
print(ptime)

"""
os包
函数名     参数      介绍      返回值
getcwd     无    返回当前的路径  字符串
listdir    path  返回指定路径下所有的文件或文件夹   返回一个列表
makedirs   path   创建多级文件夹  无
removedirs path  删除多级文件夹   无
rename    oldname newname 给文件或文件夹改名 无
rmdir      path   只能删除空文件夹    无

os.path模块
函数名     参数      介绍      返回值
exists   path    文件或路径是否存在  bool类型
isdir    path     是否是路径    bool类型
isabs    path    是否是绝对路径  bool类型
isfile   path    是否是文件    bool类型
join    Path,path*  路径字符串合并  字符串
split   Path     以最后一层路径为基准切割  列表
"""
print(os.getcwd())  # 返回当前路径
print(os.listdir('/home/jimmy/文档/qiu39789'))

"""
sys模块
函数名     参数      介绍      返回值
modules   无    py启动时加载的模块   列表
path      无    返回当前py的环境路径  列表
exit     arg     退出程序       无
getdefaultencoding  无  获取系统编码   字符串
platform    无    获取当前系统平台   字符串
version(属性)  无   获取python版本  字符串
argv     *args    程序外部获取参数   列表
"""
print(sys.getdefaultencoding())  # utf-8
print(sys.platform)
