import json

f = open("price2016.csv", 'r', encoding='utf-8')
lister = []
for line in f:
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace(" ", "")
    line = line.replace("\n", "")
    for i in line.split("'"):
        if i != ',':
            lister.append(i)
f2 = open('price2016.json', 'w', encoding='utf-8')
for r in range(1, len(lister)):
    lister[r] = dict(zip(lister[0], lister[r]))
json.dump(lister[1:], f2, sort_keys=True, indent=4, ensure_ascii=False)
print('转换完成')
f2.close()
f.close()
