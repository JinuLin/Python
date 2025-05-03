# 微实例8.5.1CSV格式和HTML展示
"""
HTML方式通过浏览器展示CSV格式数据集
"""
seg1 = '''
<!DOCTYPE HTML>
<html lang="zh-CN">
<head>
    <meta charset="utf-8">
    <title>2016年7月部分大中城市新建住宅价格指数</title>
</head>
<body>
<h2 style="text-align: center;">2016年7月部分大中城市新建住宅价格指数</h2>
<table style="border: 1px solid; width: 70%; margin: 0 auto;">
'''
seg3 = "</table>\n</body>\n</html>"


def fill_data(locls):
    seg = (
        '<tr>\n'
        '    <td style="text-align: center;">{}</td>\n'
        '    <td style="text-align: center;">{}</td>\n'
        '    <td style="text-align: center;">{}</td>\n'
        '    <td style="text-align: center;">{}</td>\n'
        '</tr>\n'
    ).format(*locls)
    return seg


# ==== 数据读取 ====
fr = open("price2016.csv", "r", encoding='utf-8')
ls = [line.strip().split(",") for line in fr]
fr.close()

# ==== 生成 HTML ====
with open("price2016.html", "w", encoding='utf-8') as fw:
    fw.write(seg1)

    # 表头行（带缩进）
    fw.write('<tr style="background-color: orange;">\n')
    fw.write(
        '    <th style="width: 25%;">{}</th>\n'
        '    <th style="width: 25%;">{}</th>\n'
        '    <th style="width: 25%;">{}</th>\n'
        '    <th style="width: 25%;">{}</th>\n'.format(*ls[0])
    )
    fw.write('</tr>\n')

    # 数据行（带缩进）
    for row in ls[1:]:
        fw.write(fill_data(row))

    fw.write(seg3)
