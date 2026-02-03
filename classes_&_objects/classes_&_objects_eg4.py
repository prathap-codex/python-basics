class phone():
    chargertype = "c-type"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("brand: ", self.brand)
        print("price: ", self.price)
        print("chargertype: ", self.chargertype)


sumsung = phone("samsung", "10000")
sumsung.display()

iphone = phone("apple", "20000")
iphone.display()

redmi = phone("redmi", "25000")
redmi.display()
