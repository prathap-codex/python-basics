def dict_basics():
    a = {
        "name": "gowri",
        "age": 18,
        "location": "canada"
    }
    a["grade"] = "A"
    print("student grade: ", a["grade"])
    print("student detail: ", a)


def dict_loop():
    a = {
        "name": "gowri",
        "age": 18,
        "location": "canada"
    }
    print("keys: ")
    for key in a:
        print(key)

    print("values: ")
    for value in a.values():
        print(value)

    print("keys & values: ")
    for key, value in a.items():
        print(key, ":", value)


def dict_student_marks():
    marks = {
        "python": 99,
        "java": 77,
        "html": 88,
        "c++": 66
    }
    total = sum(marks. values())
    average = total / len(marks)

    print("total: ", total)
    print("average: ", average)


dict_basics()
dict_loop()
dict_student_marks()
