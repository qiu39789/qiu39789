# coding utf-8

student = ["小花", "小白", "小可", "小糊涂", "小新", "小蓝", "小伟", "小玲", "小撒", "小丽", "小航"]
print(len(student))
print(student.count("小糊涂"))
student.remove("小糊涂")
print(student)
print("小雨" in student)
student.insert(7, "小雨")
print(student)
student.append("小刘")
print(student)