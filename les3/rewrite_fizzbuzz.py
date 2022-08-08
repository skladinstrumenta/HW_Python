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
    

import sys
filename = open(sys.argv[1])
filename2 = open(sys.argv[2], 'w')
for line in filename:
    f1, b1, fb1 = map(int, line.split())
    print(fizzbuzz(f1, b1, fb1)+"--строка проверена\n")
    filename2.write(fizzbuzz(f1, b1, fb1)+ '\n')


filename.close()
filename2.close()