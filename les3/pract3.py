                    # Задание 1
# l = list(range(10))
# i = 0
# sum1 = 0

# while i < len(l):
#     sum1 += l[i]
#     i += 1
# print(sum1)


# for id in l:
#     sum1 += id
# print(sum1)                
                
                
                
                # Задание 2
# import sys
# filename = sys.argv[0]
# # далее открываем файл на чтение (опция 'r')
# f = open(filename, 'r') # в файле теперь file descriptor
# for line in f: # для каждой строки в файле
#     print(line)
# f.close() # закрытие файла


                #Задание 3
import sys
print(open(sys.argv[0]).read()[::-1])