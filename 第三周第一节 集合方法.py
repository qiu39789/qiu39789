# coding:utf-8

"""
集合set是一个无序的不重复元素序列 常用来对两个列表进行交并差的处理性 集合和列表一样，支持所有数据类型
集合无法通过索引获取元素
集合无获取元素的任何方法
集合只是用来处理列表或元组的一种临时类型，它不适合存储与传输
"""
"""
集合和列表的区别
列表有序，集合无序
列表内容可重复，集合不可重复
列表用于数据的使用，集合用于对数据交并差的获取
列表有索引，集合无索引
列表符号[1,2,3] 集合符号{1,2,3}
"""
"""
创建集合的方式
a_set = set() 空集合
b_set = set([1,2,3]) 传入列表或元组
c_set = {1,2,3} 传入元素
d_set = {} 错误的创建方式，会被认为是字典
"""
a_list = ["python", "python", "java", "C#"]
b_set = set(a_list)
print(b_set)  # {'python', 'java', 'C#'} 由于集合的内容不可重复，所以可以用集合给列表去重

# 1、add set.add(item)将集合中添加一个元素，如果集合中已存在该元素则函数不执行，无返回值
b_set.add("PHP")
b_set.add(None)
b_set.add(True)
print(b_set)  # {'python', 'PHP', True, 'java', None, 'C#'} 由于集合的无序性，所以打印出来的顺序是无序的

# 2、update 加入一个新的集合（或列表，元组，字符串），如新集合内的元素在原集合中存在则无视，无返回值
c_set = set(["python"])
c_set.update(a_list)
print(c_set)  # {'python', 'C#', 'java'}

# 3、remove 删除集合中的某个元素，如果不存在会报错
c_set.remove("java")
print(c_set)  # {'python', 'C#'}

# 4、clear 清空当前集合中的所有元素
c_set.clear()
print(c_set)  # set()

# 5、del 完全删除集合对象
del c_set

# 6、差集：有所有属于a且不属于b的元素组成的集合叫做a与b的差集
#    difference 返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合（方法的参数）中
#    a_set.difference(b_set) 返回值是a_set与b_set的差集
drivers = ['xiaoming', 'xiaoli', 'xiaozhu', 'xiaowang']
testers = ['xiaozhu', 'zhangsan', 'wangwu', 'xiaoli']
drivers_set = set(drivers)
testers_set = set(testers)
new_set = drivers_set.difference(testers_set)
print(new_set)  # {'xiaoming', 'xiaowang'}

# 7、交集：a,b两个集合分别拥有的相同的元素集，称为a与b的交集
#    intersection 返回两个或更多集合中都包含的元素，即交集
#    a_set.intersection(b_set...) 返回值是a_set与b_set的交集
students = ['xiaoli']
students_set = set(students)
new_set1 = drivers_set.intersection(testers_set, students_set)
print(new_set1)  # {'xiaoli'}
print(list(new_set1))  # ['xiaoli']

# 8、并集：a,b两个集合中所有的元素（去掉重复）即为a与b的并集
#    union 返回多个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次
#    a_set.union(b_set...) 返回原始集合与对比集合的并集
new_set2 = drivers_set.union(testers_set, students_set)
print(new_set2)
print(list(new_set2))  # ['xiaowang', 'xiaoli', 'xiaozhu', 'zhangsan', 'wangwu', 'xiaoming']

# 9、 isdisjoint 判断两个集合是否包含相同的元素，没有相同的元素返回True,有相同元素返回False
#     a_set.isdisjoint(b_set) 返回值为True或False
n_set = set(['小王', '小红', '小明'])
m_set = set(['小白', '小黑', '小李'])
o_set = set(['小王', '小莉', '小萌'])
result = n_set.isdisjoint(m_set)
result1 = n_set.isdisjoint(o_set)
result2 = m_set.isdisjoint(o_set)
print(result, result1, result2)
