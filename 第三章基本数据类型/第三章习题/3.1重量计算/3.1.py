earth = eval(input("请输入你现在的体重（kg）："))
for i in range(10):
    earth += 0.5
moon = earth * (16.5 / 100)
print("你十年后在地球的体重为{}，月球上的体重为{}".format(earth, moon))
