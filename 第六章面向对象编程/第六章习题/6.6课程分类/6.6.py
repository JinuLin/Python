# 定义课程类
class Course:
    totalCredit = 0

    def __init__(self, courseId, courseName, credit, courseNature):
        self.courseId = courseId
        self.courseName = courseName
        self.credit = credit
        self.courseNature = courseNature
        Course.totalCredit += credit

    def display(self):
        print("《{}》课程编号为{}，{}学分，{}".format(self.courseName, self.courseId, self.credit, self.courseNature))

    @classmethod
    def displayCredit(cls):
        print("总学分为：", cls.totalCredit)


# 创建对象
c1 = Course(1, "Python程序开发", 4, "必修")
c2 = Course(2, "MySQL数据库技术", 2, "选修")
c1.display()
c2.display()
c1.displayCredit()
Course.displayCredit()
print("总学分为：", Course.totalCredit)
