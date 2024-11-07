# 微实例3.5.5凯撒密码
plaincode = input("请输入明文：")
for p in plaincode:
    if ord("a") <= ord(p) <= ord("z"):  # 单个字符的Unicode编码范围在a~z当中
        print(chr(ord("a") + (ord(p) - ord("a") + 3) % 26), end='')
        # 原文字符P与密文字符C满足：
        # 加密C=(P+3)mod26
        # 解密P=(C+3)mod26
    else:
        print(p, end='')
