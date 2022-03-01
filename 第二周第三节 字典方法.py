# coding:utf-8

# 字典中每一个key一定是唯一的，字典中数据量没有限制，字典中的value可以是任何python的内置数据类型的对象
# 和自定义的对象，key不支持列表

# 字典没有索引的概念
user = {"name": "李白", "age": 18}
user["top"] = 178
print(user)
user["name"] = "小明"
print(user)

# 1、update 添加新的字典，如果新字典中有和原字典相同的key，新字典的value会覆盖旧的 dict.update(new_dict)
new_user = {"name": "小王", "age": 19, "top": 198, "gender": "男"}
user.update(new_user)
print(user)

# 2、setdefault 获取某个key的value，如key不存在于字典中，将会添加key并将value设为默认值
#    dict.setdefault(key, value)  key是需要获取的key value 如果key不存在，这个value就是存入字典的默认值
#    如果不填value参数，且找不到key,那么该函数返回值为None
value = user.setdefault("name")
print(value)
value1 = user.setdefault("beforename", "曾用名")
print(value1)
print(user)  # {'name': '小王', 'age': 19, 'top': 198, 'gender': '男', 'beforename': None}

# 3、keys 无需传参，返回一个key集合的伪列表，出来的列表是无法操作的，所以叫伪列表，用list()可以让它变成真列表
print(user.keys())  # dict_keys(['name', 'age', 'top', 'gender', 'beforename'])
print(list(user.keys()))  # ['name', 'age', 'top', 'gender', 'beforename']

# 4、values 无需传参，返回一个values集合的伪列表
print(list(user.values()))

# 5、字典+中括号内传key,不进行赋值操作 即为获取，如果key不存在则会报错
print(user["gender"])

# 6、get 获取当前字典中指定key的value dict.get(key, default=None)
#    key是需要获取value的key  default key不存在则默认返回此值，默认是None
print(user.get("gender"))

# 7、clear 清空字典中的所有数据 dict.clear() 无参数和返回值 clear比重新赋值空字典更节省性能
my_dict = {"name": "小猫", "age": 18}
my_dict.clear()
print(my_dict)  # {}

# 8、pop 删除字典中指定的key,并将key对应的value值返回，如果key不存在则报错 dict.pop(key)
users = {"name": "李白", "age": 20, "gender": "男"}
print(users.pop("name"))
print(users)

# 9、del (1)删除字典中指定的key del dict["key"] (2)删除整个字典 del dict
del users["age"]
print(users)
del users
# print(users)  报错：因为变量不存在

# 10、copy 将当前的字典复制出一个新的字典 dict.copy() 无参数，返回一个一样的但是内存地址不同的字典
dict1 = {"name": "小华"}
dict2 = dict1.copy()
dict2["name"] = "康康"
print(dict2, dict1)

# 11、in 与 not in 判断key在不在字典中
dict3 = {"a": 1, "b": "qwe", "c": [1, 2, 3]}
print("b" in dict3)

# 12、popitem 删除当前字典里末尾一组键值并将key和value返回 返回值用元组包裹，索引0为key 1为value 字典为空报错
print(dict3.popitem())  # ('c', [1, 2, 3])

# 13、数据类型与布尔值的关系
#     每一种数据类型，自身的值都有表示True与False
# int float 非0为True 0为False 字符串 列表 元组 字典 长度非0为True 0为False None为False not None为True
