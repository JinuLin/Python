import keyword

stopwords = '\t\n\r: (),.{}'
functionwords = '('  # 简化功能字符检测
word = []
output = ''
lastAvailable = ['from', 'import']
last = False


def readFile(path):
    file = open(path, 'r', encoding='utf-8')
    r = file.read()
    return r  # 移除切片保留首字母


def parse(st):
    global word
    global output
    global last
    for i in st:
        if i in stopwords:
            wd = ''.join(word)
            res = isKeyWord(wd)
            if not res:
                if wd.lower() == 'self' or (output and output[-1] in ['.', '=', '{']):
                    pass
                else:
                    if i not in functionwords and last is False:
                        wd = wd.upper()
            output += wd
            output += i
            word = []
        else:
            word.append(i)


def isKeyWord(s):
    return s in keyword.kwlist  # 简化判断逻辑


def outPutFile():
    with open('8.1sj.py', 'w', encoding='utf-8') as file:
        file.write(output)


string = readFile('8.1s.py')
parse(string)
outPutFile()
