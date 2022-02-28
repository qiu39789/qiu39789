# coding utf-8

# 1、len在列表和元组中的用法 （len函数只有数字类型无法使用）
import copy

name = ["xiaoming", "libai", "zhangfei"]
names = ("zhangsan", )
print(len(name))
print(len(names))

# 2、列表和元组之间的累加与乘法
name += name
print(name)
names += names
print(names)
names *= 2
print(names)

# 3、in 和 not in 在列表（元组）中的方法
print("libai" in name)
print("zhangsan" not in names)

# 4、append 将一个新元素添加到当前列表中 list.append(new_item) 里面只能加一个参数
new_list = ["555"]
new_list.append("123")
new_list.append([1, 2, "123456"])
new_list.append({"key": "name", "value": "qiu"})
new_list.append(True)
new_list.append(None)
print(new_list)

# 5、insert 将新元素添加到列表指定位置，如果insert传入的位置在列表中不存在，就会将新元素添加到末尾
#    如果传入的位置有元素，那么新元素传入指定位置，原元素向后顺延
students_list = [
    {
        "name": "小高",
        "age": 18,
        "gender": "男"
    },
    {
        "name": "小明",
        "age": 18,
        "gender": "男"
    }
]
xiaofang = {"name": "小芳", "age": 18, "gender": "女"}
students_list.insert(1, xiaofang)
print(students_list)

# 6、count 返回当前列表（元组、字典）某个成员的个数 list.count(item) 查询的元素不存在会返回0
animals = ["小猫", "小狗", "鹦鹉", "小猫", "小猪", "小狗"]
cat = animals.count("小猫")
dog = animals.count("小狗")
bird = animals.count("鹦鹉")
pig = animals.count("小猪")
none = animals.count("其它")
print("我家有很多小动物")
print("小猫有", cat, "只")
print(f"小狗有{dog}只")
print("鹦鹉有{}只".format(bird))
print("小猪有%s只" % pig)
print(f"不明生物有{none}只")

# 7、remove 删除列表中的某个元素 list.remove(item) 若元素不存在会报错，若删除的元素有多个，只删第一个
#    这个方法会在原列表的基础上修改，没有返回值
shops = ["dvd", "烧饼", "面", "苹果"]
shops.remove("dvd")
print(shops)
# 8、内置函数del 完全删除某个变量
del shops
# print(shops)

# 9、reverse 对当前列表顺序进行反转 list.reverse(无参)
list1 = [{"name": "小张"}, {"name": "小强"}, {"name": "小白"}]
print("当前列表顺序为{}".format(list1))
list1.reverse()
print("更改后顺序为{}".format(list1))

# 10、sort 对当前列表按一定规律进行排序 list.sort(key=None,reverse=False) key-参数比较 reverse-排序规则
#     True降序 False升序（默认）
#     列表中的元素类型必须相同，不然报错
sort_list = ["01sdas", "02d", "034545", "04sad"]
sort_list.sort(reverse=False)
print(sort_list)

# 11、clear 清空列表中的数据 list.clear() 函数无参数，无返回值 clear比重新给变量赋予空值更节省性能
sort_list.clear()
print(sort_list)

# 12、copy 将当前列表复制一份相同的列表，新旧列表内容相同，但内存地址不同 list.copy() 无参数，返回一个新列表

# 二次赋值的变量与原始变量享有相同的内存空间，copy出的新列表是独立的，内存空间不同，数据不同步变更，列表中
# 还是列表的情况除外，如下面第二个例子
a = [1, 2, 3]
b = a
print(id(a), id(b))
a.append(4)
print(b, id(b))

# copy为浅拷贝:如果一个列表a中还是列表，b列表在经过copy后，无论修改a或b哪个列表，它们内部的列表数据会同步变化
c = [[1, 2, 3], [4, 5, 6]]
d = c.copy()
c[0].append(7)
print(d, c)  # [[1, 2, 3, 7], [4, 5, 6]] [[1, 2, 3, 7], [4, 5, 6]]

# new_list = copy.deepcopy(list) 深拷贝，在copy后两个列表数据不同步变化
e = [[1, 2, 3], [4, 5, 6]]
f = copy.deepcopy(e)
e[1].append(7)
print(f)  # [[1, 2, 3], [4, 5, 6]]

# 总结：深拷贝内存空间不同，不共享数据；浅拷贝是对最外层的数据创建一个新的空间来存储，而对内层的内存地址进行引用

# 13、extend 将其它列表或元组中的元素导入到当前列表中 list.extend(列表或元组)，无返回值
students = ["xiaoming", "xiaowang"]
new_students = ("libai",)
students.extend(new_students)
print(students)  # ['xiaoming', 'xiaowang', 'libai']

# 14、索引与切片
# 字符串、列表、元组的最大索引是他们的长度-1
# 索引是对单个元素进行访问，切片则对一定范围内的元素进行访问
# 切片通过中阔号内把相隔的两个索引查找出来[0:10]，切片规则为左含右不含
# 索引和切片出的列表为新列表
# 索引和切片的用法在元组上一样，但是不能通过索引/切片修改或删除元素
numberss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numberss[0:3])
print("获取列表完整数据方法1", numberss[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("获取列表完整数据方法2", numberss[0:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("获取除了最后一个元素的列表", numberss[:-1])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("列表的反序", numberss[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("列表的反向获取", numberss[5:-4])  # [6]  先从右往左数-1 -2 -3 -4,-4是7,然后从左往右数，0 1 2 3 4 5是6,这里左不包含往回一个数就是5
print("通过步长获取切片", numberss[0:8:2])  # [1, 3, 5, 7]
print("切片生成空列表", numberss[0:0])  # []

# 列表索引的获取与修改，切片修改
vvv = ["ddd", "fff", "ggg"]
print(vvv[1])
print(vvv.index("ddd"))  # 获取指定元素索引
vvv[2] = "code"
print(vvv)

bbb = [1, 2, 3, 4, 5, 6, 7]
bbb[2:5] = 8, 9, 0
print(bbb)

# 15、pop 通过索引获取并删除元素 list.pop(index) 返回值是被删除的元素
delete = bbb.pop(0)
print(delete, bbb)

# del 直接删除无返回值 del list[index]
del bbb[len(bbb)-1]
print(bbb)

# 16、字符串索引和切片 字符串无法通过索引修改与删除
teacher = "xiaowang"
print(teacher[0])
print(teacher[:2])

# 17、字符串find与index都是获得查询元素开始的索引位置 find找不到元素返回-1,index找不到元素会报错
mmm = 'asd123'
new_mmm = mmm[::-1]
print(new_mmm)
result = new_mmm.find("1ds")
print(result)
