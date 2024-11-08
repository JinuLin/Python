# 微实例7.2.2列表类型的操作
"""
列表类型特有的函数或方法：
ls[i] = x：替换列表ls第i数据项为x
ls[i: j] = lt：用列表lt替换列表ls中第i到j项数据（不含第j项，下同）
ls[i: j: k] = lt：用列表lt替换列表ls中第i到j以k为步的数据
del ls[i: j]：删除列表ls第i到j项数据，等价于ls[i: j]=[]
del ls[i: j: k]：删除列表ls第i到j以k为步的数据
ls += lt或ls.extend(lt)：将列表lt元素增加到列表ls中
ls *= n：更新列表ls，其元素重复n次
ls.append(x)：在列表ls最后增加一个元素x
ls.clear()：删除ls中所有元素
ls.copy()：生成一个新列表，复制ls中所有元素
ls.insert(i, x)：在列表ls第i位置增加元素x
ls.pop(i)：将列表ls中第i项元素取出并删除该元素
ls.remove(x)：将列表中出现的第一个元素x删除
ls.reverse(x)：列表ls中元素反转
"""
v_list = list(range(5))
print(v_list)

print(len(v_list[2:]))  # 计算从第3个位置开始到结尾的子串长度

print(2 in v_list)  # 判断2是否在列表v_list中

v_list[3] = "python"  # 修改序号3的元素值和类型
print(v_list)

v_list[1:3] = ["bit", "computer"]
print(v_list)

"""
当使用一个列表改变另一个列表值时，
Python不要求两个列表长度一样，但遵循“多增少减”的原则
"""
v_list[1:3] = ["new_bit", "new_computer", 123]
print(v_list)
v_list[1:3] = ["fewer"]
print(v_list)

"""
与元组一样，列表可以通过for…in语句对其元素进行遍历，基本语法结构如下：
for <任意变量名> in <列表名>:
    语句块
"""
for e in v_list:
    print(e, end=" ")
