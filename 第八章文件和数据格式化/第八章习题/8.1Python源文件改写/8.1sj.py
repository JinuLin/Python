def example(A, B):
    X = A + B
    Y = X * 2
    if Y > 10:
        print("LARGE")
    return Y


class DEMO:
    def __init__(self, NAME):
        self.name = NAME

    def show(self):
        print(F"NAME: {self.name.lower()}")
