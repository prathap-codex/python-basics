class calculater:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        print("num1: ", self.num1)
        print("num2: ", self.num2)
        print("add: ", self.num1 + self.num2)

    def sub(self):
        print("num1: ", self.num1)
        print("num2: ", self.num2)
        print("sub: ", self.num1 - self.num2)

    def mul(self):
        print("num1: ", self.num1)
        print("num2: ", self.num2)
        print("mul: ", self.num1 * self.num2)

    def div(self):
        print("num1: ", self.num1)
        print("num2: ", self.num2)
        print("div: ", self.num1 / self.num2)


sum1 = calculater(5, 7)
sum1.add()
