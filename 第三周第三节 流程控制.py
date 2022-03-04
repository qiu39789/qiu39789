# coding:utf-8

# or and 为python中的或和且

# if else elif 跳过

# 通过for关键字对列表，元组，字典中的每个元素安照一定序列顺序进行遍历（循环）
# for item in iterable:
# iterable:可循环的数据类型，如字符串列表元组和字典 item:iterable中的每一个成员
# for 循环是语句，没有返回值，但在特定情况下有返回值
users = {"name": "libai", "age": 18}
for i in users:
    print(i, users[i])
# 字典利用items内置函数进行for循环 -> 将字典转成伪列表，每个key,value转成元组
# for key,value in dict.items():
# items()无参数 key：for循环体中获取的字典当前元素的key value: for循环体中对应当前key的value的值
# 返回值：items返回一个伪列表
new_users = users.items()
print(new_users)  # dict_items([('name', 'libai'), ('age', 18)])
for key, value in new_users:
    print(key, value)

# python的内置函数 range 返回的是一个一定范围的可迭代对象，元素为整型，他不是列表，无法打印信息，但可循环
# for item in range(start, stop, step=1):
#   print(item)
# start 开始的数字，类似索引的左边。 stop 结束的数字，类似索引的右边。左含右不含
# step 跳步，类似索引中的第三个参数
# 返回值：返回一个可循环以整型为主的对象

# else在for循环中的使用
# else语句只有在for循环正常退出后执行 且 循环没有报错，没有中途停止
for item in range(3):
    print(item)  # 0 1 2 只传一个数那就是从0开始
for item in range(1, 3):
    print(item)  # 1 2
else:
    print("循环结束了")

# 嵌套for循环
a = [1, 2, 3]
b = [4, 5, 6]
for i in a:
    for j in b:
        print(i + j, " ", end='')

# while循环 以一定条件为基础的循环，条件满足则无限循环，条件不满足退出循环

# continue 停止当前循环，直接执行下一次循环
count = 1
while count < 5:
    print(count)
    continue
    count += 1    # 无限循环1
# break 使循环正常停止，这时如果配合了else语句，else语句不会执行
count = 1
while count < 5:
    print(count)
    count += 1
    break  # 1
# 在while循环中，break语句优先于while逻辑体的判断
