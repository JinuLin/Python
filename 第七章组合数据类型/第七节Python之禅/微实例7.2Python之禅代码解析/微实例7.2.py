# 微实例7.7.2Python之禅代码解析
"""
在Python安装目录找到Lib/this.py
本工程下已经复制了this.py文件
观察源码，十分有趣
在1~22行是一个字符串s，但是并非原文。
第24~29行，对密文进行了解析。
可以看到
23行创建了一个空字典d，
第26行对字典d进行了填充，
将i+c对应的字符替换为(i+13)%26+c，
即将编号循环了13。
chr(65)代表了字符'A',chr(97)代表字符'a'。
因此23~26行建立了字母a-z与A-Z的一个13位循环移动。
27~30行，对字符串s进行解密。
即是凯撒密码的扩展，位移量为13，对应表如下：
密文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
原文：N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
密文：a b c d e f g h i j k l m n o p q r s t u v w x y z
原文：n o p q r s t u v w x y z a b c d e f g h i j k l m
"""
"""
this.py程序如下：
"""
s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
