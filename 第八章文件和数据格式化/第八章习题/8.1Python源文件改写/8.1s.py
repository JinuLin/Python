def example(a, b):
    x = a + b
    y = x * 2
    if y > 10:
        print("Large")
    return y


class Demo:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name: {self.name.lower()}")
