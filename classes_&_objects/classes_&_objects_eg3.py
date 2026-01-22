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


# next example

class student:
    def __init__(self, na, re):
        self.name = na
        self.regno = re

    def student2(self, na, re):
        self.name = na
        self.regno = re


s1 = student("gowri", "1")
s2 = student("prathap", "2")


print(s1.name)
print(s1.regno)

print(s2.name)
print(s2.regno)
