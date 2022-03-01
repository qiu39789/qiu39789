# coding:utf-8

str_list = ["e_ying", "d_shi", "a_wo", "f_xiong", "b_men", "c_dou"]
num_list = [6, 1, 2, 3, 4, 5]
str_list.sort()
num_list.sort()
print(str_list, num_list)
str_list.reverse()
num_list.reverse()
print(str_list, num_list)
new_list = str_list.copy()
print(new_list)