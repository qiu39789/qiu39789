# coding utf-8

world = "When your mind is simple, your world is simple"
print("定义长度：" + world.zfill(len(world) + 4))
print("获取元素i的个数:{}".format(world.count("i")))
print("判断开头的元素是不是e:", world.startswith("e"))
print("判断结尾的元素是不是e:", world.endswith("e"))
print(f"请找到元素r在哪个位置{world.find('r')}")
print("请把字符串中的元素W去掉:", world.replace("W", ""))
print("请把字符串中的your改成my:", world.replace("your", "my"))
print("请判断字符串是不是由空格组成", world.isspace())
print("判断字符串是不是标题", world.istitle())
print("判断字符串中的字母是不是都是大写", world.isupper())
print("判断字符串中的字母是不是都是小写", world.islower())
