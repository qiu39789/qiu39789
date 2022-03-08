# coding:utf-8

"""
类：class 有属性（类中的变量） 有方法（类中的方法） 类是为了做比较大的功能
类的首字母大写，多单词情况下每个单词首字母大写
self 是类函数中的必传参数，且必须放在第一个参数位置
self 是一个对象，它代表实例化的变量自身
self 可以直接通过点来定义一个类变量
self 中的变量与含有self参数的函数可以在类中的任何一个函数内随意调用
非函数中定义的变量在定义的时候不用self
"""


class Person(object):
    name = "libai"

    def dump(self):
        print(f"{self.name} is my name")


libai = Person()  # 类的实例化
print(libai.name)  #
libai.dump()

"""
类的构造函数 类的一种默认函数，用来将类实例化的同时，将参数传入类中
def _init_(self,a,b)
    self.a = a
    self.b = b
"""


class Test(object):

    def __init__(self, a):
        self.a = a

    def run(self):
        print(self.a)


test = Test(1)
test.run()  # 1

"""
私有函数和私有变量
    无法被实例化后的对象调用的类中的函数与变量
    类内部可以调用私有函数与变量
    只希望类内部业务调用使用，不希望被调用者使用
定义方法
    在变量或函数前添加两个下划线__，变量或函数名后面无需添加
"""


class Teacher(object):
    company = "宇宙公司"

    def __init__(self, name, sex):
        self.name = name
        self.__sex = sex

    def study(self):
        print("公司名称{}".format(self.company))
        print("教师姓名{}".format(self.name))
        print("性别{}".format(self.__sex))


teacher = Teacher("小明", "男")
teacher.study()

"""
封装 使用可对外调用的函数，在这个函数中调用私有属性或方法，就是封装 封装可以保护隐私，明确区分内外 代码如上所示

装饰器 也是一种函数，可以接受函数作为参数，可以返回函数
       接受一个函数，内部进行处理，返回一个新函数，动态的增强函数功能
       将c函数在a函数中执行，在a函数中可以选择执行或不执行c函数，也可以对c函数的结果进行二次加工处理
装饰器的定义规则
    def out(func_args):     外围函数
        def inter(*args, **kwargs):     内嵌函数
            return func_args(*args, **kwargs)
        return inter    外围函数返回内嵌函数
装饰器的用法
    将被调用的函数直接作为参数传入装饰器的外围函数括弧
    将装饰器与被调用函数绑定在一起
    @符号+装饰器函数放在被调用函数的上一行，被调用的函数正常定义，只需要直接调用被执行函数即可
"""


def check_str(fun):
    def inter(*args, **kwargs):
        result = fun(*args, **kwargs)
        if result == 'ok':
            return "result is %s" % result
        else:
            return "result is %s" % result

    return inter


@check_str
def test(data):
    return data


print(test('ok'))

"""
类的常用装饰器
classmethod 将类函数可以不经过实例化而直接被调用
用法：
    @classmethod
    def func(cls, ...):
        do
    cls替代普通类函数中的self，变为cls，代表当前操作的是类
带有classmethod的类函数无法调用普通的self函数，但是self函数可以调用带classmethod的类函数
"""


class Text(object):
    @classmethod
    def add(cls, a, b):
        return a + b

    def test(self):
        return self.add(3, 4)


result = Text.add(1, 2)
print(result)  # 3
new = Text()
new_result = new.test()
print(new_result)  # 7

"""
类的常用装饰器
staticmethod 将类函数可以不经实例化而直接调用，使用该装饰器调用的函数不许传递self或者cls参数
             且无法在该函数内调用其它类函数或类变量
用法：
    @classmethod
    def func(...):
        do
"""


class Test1(object):
    @staticmethod
    def add(a, b):
        return a + b


print(Test1.add(1, 2))  # 3

"""
类的常用装饰器
property 将类函数的执行免去括弧，类似调用属性（变量）
用法：
    @property
    def func(self):
        do
"""


class Test2(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


t1 = Test2('xiaoming')

print(t1.name)  # xiaoming
t1.name = 'libai'
print(t1.name)  # libai

"""
类的继承
    通过继承基类来得到基类的功能
    所以我们把被继承的类称作父类或基类，继承者被称作子类
    代码的重用
父类和子类的关系
    子类拥有父类的所有属性和方法
    父类不具备子类自有的属性和方法
定义子类时，将父类传入子类参数内
子类实例化可以调用自己与父类的函数与变量
"""


class Parent(object):
    def talk(self):
        print("talk")

    def think(self):
        print("think")


class Child(Parent):
    def swimming(self):
        print("child can swimming")


child = Child()
child.think()
child.talk()
child.swimming()

"""
super函数的作用
python子类继承父类的方法而使用的关键字，当子类继承父类后，就可以使用父类的方法
"""


class Parent1(object):
    def __init__(self):
        print("this is parent1")


class Child1(Parent1):
    def __init__(self):
        print("this is child1")
        super(Child1, self).__init__()


c = Child1()  # 不使用super函数前会打印出this is child1 使用会打印出child1和parent1


"""
类的多态：同一个功能的多状态化 就是同一个函数，执行出的结果不相同
多态的用法：子类中重写父类的方法（父类中有个talk函数，子类可以再写个talk函数，但功能不一样，就是多态）
为什么要继承：是为了使用已经写好的类中的函数
为什么要多态：为了保留子类中某个和父类名称一样的函数的功能
"""
"""
类的多重继承
可以让子类继承多个父类
class Child(Parent1, Parent2, Parent3, ...) 从左到右依次继承
"""
"""
类的高级函数
__str__ 如果定义了该函数，当print当前实例化对象的时候，会返回该函数的return信息
__getattr__ 当调用的属性或者方法不存在时，会返回该方法定义的信息
__setattr__ 拦截当前类中不存在的属性与值，对它们可以进行处理
__call__ 本质是将一个类变成一个函数
"""