def list_basics():
    a = [1, 2, 3, 4, 5, 6]
    print("numbers: ", a)
    print("length: ", len(a))
    print("first number: ", a[0])
    print("last number: ", a[-1])


def list_even_odd():
    num = [1, 2, 3, 4, 5, 6]
    print("even numbers: ")
    for i in num:
        if (i % 2 == 0):
            print(i)

    print("odd numbers:")
    for i in num:
        if (i % 2 == 1):
            print(i)


def sum_max_min():
    a = [1, 2, 3, 4, 5, 6]
    print("sum: ", sum(a))
    print("maximun: ", max(a))
    print("minimum: ", min(a))


def list_remove_duplicates():
    a = [1, 2, 3, 4, 5, 6, 5, 4, 3]
    unique_a = list(set(a))
    print("without duplicate: ", unique_a)


list_basics()
list_even_odd()
sum_max_min()
list_remove_duplicates()
