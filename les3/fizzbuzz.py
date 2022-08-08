def fizzbuzz(f, b, fb):
    fblist = []
    for i in range(1, fb+1):
        if not i % f and not i % b:
            fblist.append("FB")
        elif not i % f:
            fblist.append("F")
        elif not i % b:
            fblist.append("B")
        else:
            fblist.append(str(i))
    return " ".join(fblist)
    print("строка проверена \n")

    
import sys
filename = open(sys.argv[1])
for line in filename:
    f1, b1, fb1 = map(int, line.split())
    print(fizzbuzz(f1, b1, fb1))

filename.close()