# coding:utf-8

import re
# print(re.match('www', 'www.runoob.com').group())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配


# line = "Cats are smarter than dogs"
#
# searchObj = re.search(r'(.*?) are (.*?) .*', line)
#
# if searchObj:
#     print("searchObj.group() : ", searchObj.group())
#     print("searchObj.group(1) : ", searchObj.group(1))
#     print("searchObj.group(2) : ", searchObj.group(2))
# else:
#     print("Nothing found!!")


# phone = "2004-959-559 # 这是一个国外电话号码"
# # 删除字符串中的 Python注释
# num = re.sub(r'#.*$', "", phone)
# print("电话号码是: ", num)
# # 删除非数字(-)的字符串
# num = re.sub(r'\D', "", phone)
# print("电话号码是 : ", num)

s1 = 'adkkdk'
s2 = 'abc123efg'

an = re.search('^[a-z]+$', s1)
print(an)
if an:
    print('s1:', an.group(), '全为小写')
else:
    print(s1, "不全是小写！")

an = re.match('[a-z]+$', s2)
print(an)
if an:
    print('s2:', an.group(), '全为小写')
else:
    print(s2, "不全是小写！")
