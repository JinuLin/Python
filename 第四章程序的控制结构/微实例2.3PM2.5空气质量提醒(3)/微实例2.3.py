# 微实例4.2.3PM2.5空气质量提醒(3)
PM = eval(input("请输入PM2.5数值："))
if 0 <= PM <= 35:
    print("空气质量优质，快去户外运动！")
elif 35 <= PM <= 75:
    print("空气质量良好，适度户外运动！")
else:
    print("空气污染，请小心！")

"""
多分支结构：if-elif-else
if<条件1>:
<语句1>
elif<条件2>:
<语句2>
...
else:
<语句N>
"""