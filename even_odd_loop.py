def even_numbers():
    for i in range(1, 11):
        if (i % 2 == 0):
            print(i)


def odd_count():
    count = 0
    for i in range(1, 11):
        if (i % 2 == 1):
            count = count+1
    print("count of odd num: ", count)


def even_numbers_and_count():
    count = 0
    for i in range(1, 11):
        if (i % 2 == 0):
            print(i)
            count = count + 1
    print("count off even number: ", count)


even_numbers()
odd_count()
even_numbers_and_count()
