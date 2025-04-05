# 微实例6.1.1面向对象和面向过程的区别
"""
面向过程编程
注重过程： 面向过程编程是围绕着一系列的步骤或过程构建的。
它强调的是“怎么做”，即通过定义函数和过程来完成特定任务。
你可以想象它像是按照食谱一步一步地烹饪一道菜。
假设我们要管理一个图书馆的书籍借阅系统，使用面向过程的方式，我们可能会这样做：

"""
# 定义全局变量，模拟数据库
books = {}


# 定义函数，用于添加书籍
def add_book(title, author):
    books[title] = {"author": author, "borrowed": False}


# 定义函数，用于借书
def borrow_book(title):
    if title in books and not books[title]["borrowed"]:
        books[title]["borrowed"] = True
        print(f"{title} has been borrowed.")
    else:
        print("Book not available.")


# 定义函数，用于还书
def return_book(title):
    if title in books and books[title]["borrowed"]:
        books[title]["borrowed"] = False
        print(f"{title} has been returned.")
    else:
        print("Book is not borrowed or does not exist.")


# 使用这些函数来操作书籍
add_book("The Great Gatsby", "F. Scott Fitzgerald")
borrow_book("The Great Gatsby")
return_book("The Great Gatsby")
""""
在这个例子中，我们定义了一系列的函数来执行不同的任务.
如添加书籍、借书和还书。每个函数代表了处理图书的一个具体步骤。
"""
"""
面向对象编程
注重整体：面向对象编程则更加关注“是什么”以及“谁在做”。
它将现实世界中的实体抽象成对象，并且这些对象包含了它们自己的属性（数据）和行为（方法）。
这就像你考虑整个图书馆作为一个整体，而不是单独考虑每一个步骤。
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"{self.title} has been borrowed.")
        else:
            print("Book not available.")

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print("Book is not borrowed.")


# 创建书籍对象
great_gatsby = Book("The Great Gatsby", "F. Scott Fitzgerald")

# 使用对象的方法来操作书籍
great_gatsby.borrow()
great_gatsby.return_book()
"""
在这个面向对象的例子中，Book 类代表了图书馆里的书，
它有自己固有的属性（标题、作者、是否被借出）和行为（借书、还书）。
每本书都是 Book 类的一个实例，拥有自己的状态和可以执行的操作。
"""
