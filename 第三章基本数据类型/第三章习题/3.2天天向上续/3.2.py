dayup = 1
dayfactor = 0.01
for i in range(365):
    if i % 7 not in [0, 1, 2]:
        dayup *= (1 + dayfactor)
    else:
        dayup = dayup
print("连续学习365天后能力值是： {:.2f}。".format(dayup))
