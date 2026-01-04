n = int(input("numbers of terms: "))

cube = []

for i in range(1, n+1):
    cube.append(i**3)

for i in range(n):
    print("number is: ", i+1, "and the cube of the ", i+1, "is: ", cube[i])
