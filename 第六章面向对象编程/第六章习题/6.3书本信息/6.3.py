# 定义Book类
class Book:
    def __init__(self, book_id, book_name, pub_id, price):
        self.bookId = book_id
        self.bookName = book_name
        self.pubId = pub_id
        self.price = price

    def display(self):
        print("《{}》书编号为{}，出版社编号{}，价格{}".format(self.bookName, self.bookId, self.pubId, self.price))


# 创建对象
b1 = Book(1, "高等数学", 3, 39.6)
b2 = Book(2, "民间艺术", 8, 27.9)
b1.display()
b2.display()
