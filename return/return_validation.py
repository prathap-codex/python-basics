s_username = "emc"
s_password = 123

username = input("user name: ")
password = int(input("password:"))


def validation():
    if (s_username == username and s_password == password):
        return True
    else:
        return False


a = validation()
print(a)
