# 定义医生类
class Doctor:
    def __init__(self, name, idnumber, address):
        self.name = name
        self.idnumber = idnumber
        self.address = address

    def display(self):
        print("name:{},idnumber:{},address:{}".format(self.name, self.idnumber, self.address))


# 创建对象
d = Doctor("李静", "326", "江苏太仓")
d.display()
