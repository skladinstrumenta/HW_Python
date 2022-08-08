                # EXERCISE 1.

# number = int(input("Input number: "))
# if number % 2:
#     print("число", number, "нечётное")
# else:
#     print("число", number, "чётное")


                # EXERCISE 2.

# number = int(input("Input number: "))
# if (number % 2) and (not number % 3) and (not number % 5) and (number % 10):
#     print(number)
# else:
#     print("число не удовлетворяет требованиям")



                # EXERCISE 3

# number = int(input("Input number: "))
# for i in range(1, number+1):
#     if not number % i:
#         print(i)

                
                # EXERCISE 4 / РАЗРЯДЫ И ИХ МНОЖИТЕЛИ

number = input("Input number: ")
lennumber = len(number)
for i in number:
    lennumber -= 1
    print(i+"*10^"+str(lennumber))
 