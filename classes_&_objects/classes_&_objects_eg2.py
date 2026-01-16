class laptop:
    price = ""
    processor = ""
    ram = ""

    def hp(self):
        print("hp is balanced laptop")

    def dell(self):
        print("dell is average laptop")

    def lenovo(self):
        print("levono is excellent laptop")


hp = laptop()
dell = laptop()
lenovo = laptop()

hp.price = "1000"
dell.price = "2000"
lenovo.price = "3000"

hp.processor = "amd"
dell.processor = "ryzan"
lenovo.processor = "amd"

hp.ram = "16"
dell.ram = "32"
lenovo.ram = "64"

print("hp price: ", hp.price)
print("processor: ", hp.processor)
print("ram: ", hp.ram)


print("dell price: ", dell.price)
print("processor: ", dell.processor)
print("ram: ", dell.ram)

print("lenovo price: ", lenovo.price)
print("processor: ", lenovo.processor)
print("ram: ", lenovo.ram)

hp.hp()
dell.dell()
lenovo.lenovo()
