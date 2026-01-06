def example_one():
    for i in range(1, 6):
        for j in range(1, 3):
            print(j, "apple")


def schedule_making():
    for i in range(1, 3):
        print("week:", i)
        for j in range(1, 4):
            print("  day: ", j)


def pramid_star():
    for i in range(5):
        print(" ")
        for i in range(1, i+1):
            print("*", end=" ")


def pramid_number():
    for i in range(1, 6):
        print(" ")
        for j in range(1, i+1):
            print(j, end=" ")


example_one()
schedule_making()
pramid_star()
pramid_number()
