# coding:utf-8

"""
字符串内置函数
capitalize() -> 字符串首字母大写，其他字母小写，只对字母生效
casefold() lower() -> 字符串字母小写，只对字母生效
upper() -> 字符串字母大写，只对字母生效
swapcase() -> 字符串所有字母大小写转换

zfill(width) -> 为字符串定义长度，如果不满足，缺少的部分用0填充
count(item) -> item是需要查询字符串中个数的元素
startwith(item) -> 判断字符串开头是否是某元素
endwith(item) -> 判断字符串结尾是否是某元素
find(item) index(item) -> 都是返回想寻找的成员的位置，返回整型，只返回第一次出现的地方
                          find找不到元素返回-1,index找不到元素会报错
                          find其他用法：find(item,startindex,endindex)
                          startindex是开始索引，默认为0,endindex是结束索引，默认为字符串长度
strip(item) -> item代表想要去掉的位于字符串开头或结尾的元素，不填默认去掉头或结尾的空格
lstrip(item) -> 只去掉开头
rstrip(item) -> 只去掉结尾
replace(old, new, max) -> 将字符串中旧元素替换为新元素，并可指定替换的数量
                          old是被替换的元素，new是新元素，max可选，代表替换几个，默认全部替换
isspace() -> 判断字符串是否是一个由空格组成的字符串，全是空格才返回True,只有一部分有空格返回False
istitle() -> 判断字符串是否是一个标题类型，只用于英文，标题类型就是Hellow Word这种每个首字母大写，其它字母小写的
isupper() -> 判断字符串中的字母是否都是大写，只判断字符串中的字母，无视其它字符 HELLOW哈哈WORLD 返回True
islower() -> 判断字符串中的字母是否都是小写，只判断字符串中的字母，无视其它字符

字符串编码格式
    常见编码格式
        gbk中文编码 ascii英文编码 utf-8国际通用编码格式
字符串格式化
    message = "你好，今天是%s,您的手机号码%s已欠费"
    print(message % ('星期一', 123456)) 传入的数据类型也可以是列表，元组或者字典
字符串格式化函数-format
    "hello{0}，你今天看起来{1}".format('小明','不错') 传入的数据类型也可以是列表，元组或者字典
    0,1可以不写，直接大括号也行
python3.6新加格式化方法 f-strings
    print(f"hello,{name}")  要提前定义好变量
格式化字符
    %d %u %c %f %s %o %x %e等
字符串转义字符
    \n 换行
     \t tab间隔符
      \b 退格
       \r 回车
        \' 转义单引号
         \" 转义双引号
          \\ 转义斜杠
                       还有其它的
字符串转义无效字符
    在字符串前加r使转义字符无效
"""
print("abC".capitalize())
name = "xiao Ming"
new_name = name.capitalize()
print("初始名：", name, "新名：", new_name)
print("初始名：%s新名：%s" % (name, new_name))
#  ===========================================================
message = "How do you Do? 123123#"
print(message.casefold())
print(message.lower())
print(message.upper())
print(message.swapcase())
#  ===========================================================
message1 = "asd123"
print(message1.zfill(10))  # 0000asd123
#  ===========================================================
message2 = "asd123dd我是谁，我吃饭了"
print(message2.count("d"))
print(message2.count("我"))
#  ===========================================================
info = "this is a simple!"
print(info.startswith("thi"))  # True
print(info.endswith("a"))  # False

print(info.startswith("this is a simple!"))  # True
print(info == "this is a simple!")  # True
#  ===========================================================
test = "my name is eee"
print(test.find("e"))
print(test.find("z"))  # 找不到元素返回-1
print(test.index("e"))
text = "everyone"
print(text.find("e", 2))  # 2
#  ===========================================================
strip = "   hellow word! hello python    "
print(strip.strip())
new_strip = "hellow word! hello python"
print(new_strip.strip("h"))
textt = "****python****"
print(textt.strip("*"))
#  ===========================================================
listlist = ('666666666666666'
            '55555555555555'
            '44444444444444')
print(listlist.replace("66", "*").replace("5", "%").replace("444", "^", 2))
#  ===========================================================
message = "你好，今天是%s,您的手机号码%s已欠费"
print(message % ('星期一', 1232344))
print("hello{}，你今天看起来{}".format('小明', '不错'))
print(f"hello,{name}")
#  ===========================================================
print('%c' % 10000)
print('%c' % "a")
print('%f' % 3.14)
print('%f' % 3)
print('%d' % 10.00)
print('%d' % 2.10)
print('%d' % 2.90)
#  ===========================================================
print("\thellow word my \nname is xxx")
print("\nhellow word my\tname is xxx")
print("hellow word my \'name\' is xxx")
print("hellow word my \\name\\ is xxx")
print(r"hellow word my \\name\\ is xxx")
print(r"\thellow word my \nname is xxx")
