a = int(input("Python: "))
b = int(input("HTML: "))
c = int(input("Java: "))

# Invalid marks check
if (a < 0 or a > 100) or (b < 0 or b > 100) or (c < 0 or c > 100):
    print("Invalid score")

# Pass condition
elif a >= 35 and b >= 35 and c >= 35:
    print("Pass")

# Fail condition
else:
    print("Fail")
