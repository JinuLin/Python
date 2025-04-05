# 微实例4.4.3循环保留字：break和continue
# continue
for s in "PYTHON":
    if s == "T":
        continue
    print(s, end="")
print("\n")
# 用于跳出当前当次循环，即跳出循环体下面尚未执行的语句，但不跳出当前循环。

for s in "PYTHON":
    if s == "T":
        continue
    print(s, end="")
else:
    print("正常退出")
print("\n")

# break
for s in "PYTHON":
    if s == "T":
        break
    print(s, end="")
print("\n")
# break可以直接跳出当前循环，而不再判断当前的语句，但是只跳出所在层的循环，外层循环依旧进行

for s in "PYTHON":
    if s == "T":
        break
    print(s, end="")
else:
    print("正常退出")
print("\n")
