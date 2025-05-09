d = {}
digits = '0123456789'
path = 'd.txt'


def readFile(p, arg):
    try:
        file = open(p, arg, encoding='UTF-8')
        # 测试文件编码是否合法
        if arg == 'r':
            file.read(1)
            file.seek(0)
    except (FileNotFoundError, UnicodeDecodeError):
        # 编码错误或文件不存在时，创建新 UTF-8 文件
        file = open(p, 'w', encoding='UTF-8')
        print(f"检测到文件编码错误或不存在，已创建新的 UTF-8 文件: {p}")
    return file


def readWords():
    try:
        file = readFile(path, 'r')
    except UnicodeDecodeError:
        # 备份原始文件
        import shutil
        shutil.copy(path, f"{path}.bak")
        print(f"已备份原文件 -> {path}.bak")
        file = readFile(path, 'w')

    while True:
        line = file.readline()
        if not line:
            break
        word = line.split(' ', 2)
        d[word[0]] = word[1][:-1]
    file.close()


def writeFile(word, dsp):
    file = readFile(path, 'a')
    file.write('{} {}\n'.format(word, dsp))
    file.close()


def modifyFile(word, dsp):
    file = readFile(path, 'r')
    line = file.readlines()
    flen = len(line) - 1
    for i in range(flen):
        if word in line[i]:
            file.close()
            line[i] = '{} {}\n'.format(word, dsp)
            file = readFile(path, 'w')
            file.writelines(line)
            break
    file.close()


def editMode():
    print('*' * 50)
    print('*' * 50)
    while True:
        word = input("(按数字键退出)请输入您想添加或修改的单词:")
        if word in digits:
            print('*' * 50)
            print('*' * 50)
            return
        if word in d:
            print(f'该单词已存在于单词库,当前解释是：{d[word]}')
        else:
            print('您添加的是一个新单词')
        print('---------------------------------')
        description = input('请输入您的解释:\n')
        try:
            d[word] += ',%s' % description
            modifyFile(word, d[word])
        except KeyError:
            d[word] = '%s' % description
            writeFile(word, d[word])
        print('----------添加完成--------------')


def searchMode():
    print('*' * 50)
    print('*' * 50)
    while True:
        word = input("(按数字键退出)想查的单词:")
        if word in digits:
            print('*' * 50)
            print('*' * 50)
            return
        print('---------------------------------')
        try:
            print(d[word])
        except KeyError:
            print('对不起，这个单词没有收录')
        print('---------------------------------')


def interface():
    readWords()

    def switch(op):
        func_dic = {
            1: lambda: searchMode(),
            2: lambda: editMode(),
            3: lambda: exit()
        }
        return func_dic[op]()

    while True:
        print('----------欢迎使用英汉词典----------')
        print('1.查询单词\n2.添加单词\n3.退出\n')
        option = int(input('请输入您的选择：'))
        switch(option)


interface()
