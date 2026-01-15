class goa:
    name = ""
    drink = ""

    def party(self):
        print("lets party!!!!!")

    def beach(self):
        print("enjoy the beach")


rajesh = goa()
suresh = goa()

rajesh.name = "rajesh"
suresh.name = "suresh"

rajesh.drink = "yess"
suresh.drink = "noo"

print(rajesh.name)
print("drink: ", rajesh.drink)

print(suresh.name)
print("drink: ", suresh.drink)

rajesh.party()
suresh.beach()
