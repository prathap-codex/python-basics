def sum_and_average():
    a = []
    print("enter ten values")
    for i in range(10):
        num = int(input("enter value"+str(i+1)+(": ")))
        a.append(num)
    print(a)

    sum = 0
    for i in a:
        sum = sum+i
    print("sum of ten values: ", sum)

    avg = sum / len(a)
    print("avg of ten values: ", avg)


def numbers_and_sum():
    a = []
    for i in range(int(input())):
        a.append(i+1)
    print("natural numbers: ", a)

    sum = 0
    for i in a:
        sum = sum + i
    print("sum of total values: ", sum)


sum_and_average()
numbers_and_sum()
