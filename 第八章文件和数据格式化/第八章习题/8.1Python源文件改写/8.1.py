import keyword

stopwords = '\t\n\r: ()'
functionwords = '.('
word = []
output = ''
lastAvailable = ['from', 'import']
last = False


def readFile(path):
    file = open(path, 'r', encoding='utf-8')
    r = file.read()
    return r[1:]


def parse(st):
    global word
    global output
    global last
    for i in st:
        if i in stopwords:
            wd = ''.join(word)
            res = isKeyWord(wd)
            if not res:
                if i not in functionwords and last == False:
                    wd = wd.upper()
            if wd in lastAvailable:
                last = True
            else:
                last = False
            output += wd
            output += i
            word = []
        else:
            word.append(i)


def isKeyWord(s):
    if s in keyword.kwlist:
        return True
    return False


def outPutFile():
    file = open('8.1sj.py', 'w', encoding='utf-8')
    file.write(output)


string = readFile('8.1s.py')
parse(string)
outPutFile()
