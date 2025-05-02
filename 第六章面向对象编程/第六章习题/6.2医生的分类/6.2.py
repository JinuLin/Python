# 定义医生类
class Doctor:
    def __init__(self, name, idnumber, address):
        self.name = name
        self.idnumber = idnumber
        self.address = address

    def display(self):
        print("name:{},idnumber:{},address:{}".format(self.name, self.idnumber, self.address))


# 定义子类
class Specialist(Doctor):
    def __init__(self, name, idnumber, address, speciality):
        super().__init__(name, idnumber, address)
        self.speciality = speciality

    def display(self):
        print("我是{}专业的医生".format(self.speciality))
        super().display()


class NonSpecialist(Doctor):
    def display(self):
        print("我是非专业医生")
        super().display()


# 创建对象
# d = Doctor("李静","326","江苏太仓")
# d.display()
s = Specialist("王海", "491", "江苏南京", "眼科")
n = NonSpecialist("姜平", "287", "江苏苏州")
s.display()
n.display()
