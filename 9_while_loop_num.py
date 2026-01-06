def ten_star_series():

    i = 10
    while (i < 201):
        print(i, end=", ")
        i = i+10


def ten_reverse_natural_numbers():

    i = 10
    while (i >= 1):
        print(i, end=", ")
        i = i-1


def factorial_of_number():
    i = 5
    fact = 1
    while (i >= 1):
        fact = fact * i
        i = i - 1
    print(fact)


ten_star_series()
ten_reverse_natural_numbers()
factorial_of_number()
