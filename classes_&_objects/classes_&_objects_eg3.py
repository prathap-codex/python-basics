class student:
    def __init__(self):
        self.name = "ajay"
        self.regno = "5745"

    def display(self):
        print("name: ", self.name)
        print("regno: ", self.regno)


s1 = student()
s2 = student()

s1.name = "gowri"
s1.regno = "1"

s2.name = "prathap"
s2.regno = "2"

s1.display()
s2.display()


# next example

class fruit:
    def __init__(self, col):
        self.colour = col


apple = fruit("red")
print(apple.colour)
