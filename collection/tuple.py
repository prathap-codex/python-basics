def tuple_basics():
    a = (1, 2, 3, 4, 5, 6)
    print("third element: ", a[3])
    print("lenth: ", len(a))


def tuple_to_list():
    a = (1, 2, 3, 4, 5, 6)
    b = list(a)
    b.insert(6, 7)
    print("new tuple: ", b)


tuple_basics()
tuple_to_list()
