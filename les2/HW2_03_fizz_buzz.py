fizz = int(input("Input first number: "))
buzz = int(input("Input second number: "))
fb = int(input("Input third number: "))
for i in range(1,fb+1):
    if not i % fizz  and not i % buzz:
        print("FB", end=" ")
    elif not i % fizz:
        print("F", end=" ")
    elif not i % buzz:
        print("B", end=" ")
    else:
        print(i, end=" ")
