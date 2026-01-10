def set_basics():
    a = {1, 2, 3, 4, 5, 6, 6}
    a.add(7)
    a.remove(3)
    print("final value: ", a)


def set_operations():
    a = {1, 2, 3}
    b = {3, 4, 5}
    print("union: ", a | b)
    print("intersection: ", a & b)
    print("diffrence: ", a - b)


def set_remove_duplicates():
    a = {1, 2, 2, 3, 3, 4, 4, 5}
    unique = list(set(a))
    # set_can_automatically_remove_duplicates
    print("original: ", a)
    print("unique: ", unique)


set_basics()
set_operations()
set_remove_duplicates()
