# 微实例7.1.3映射类型
"""
映射类型是“键-值”数据项的组合，每个元素是一个键
值对，即元素是(key, value)，元素之间是无序的。键值对
(key, value)是一种二元关系。在Python中，映射类型主要
以字典（dict）体现。
"""
# 创建一个字典
mapping = {
    "apple": 1,
    "banana": 2
}

# 获取长度
print(len(mapping))  # 输出: 2

# 获取值
print(mapping["apple"])  # 输出: 1

# 设置值
mapping["apple"] = 3
print(mapping["apple"])  # 输出: 3

# 添加新键值对
mapping["orange"] = 4
print(len(mapping))  # 输出: 3

# 删除键值对
del mapping["banana"]
print(len(mapping))  # 输出: 2

# 检查键是否存在
print("apple" in mapping)  # 输出: True
print("banana" in mapping)  # 输出: False

# 迭代
for key, value in mapping.items():
    print(f"{key}: {value}")  # 输出: apple: 3, orange: 4
