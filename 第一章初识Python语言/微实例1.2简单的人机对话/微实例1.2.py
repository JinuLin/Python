# 微实例1.1.2简单的人机对话
name = input("输入姓名:")  # input输入数据
print("{}同学，学好Python，前途无量！".format(name))
print("{} 大侠，学好Python，大展拳脚！".format(name[0]))  # 0指前面输入的数据当中的第一个数值（可以是字符、数字）
print("{} 哥哥，学好Python，人见人爱！".format(name[1:]))  # 1:指前面输入的数据当中的第二个数值以后的数据（可以是字符、数字）
