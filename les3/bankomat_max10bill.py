L = [1000, 500, 200, 100, 50, 20, 10]
L2 = L[::-1]
sumbill = 0
sum = 1
l3 = {}
print("Приветсвуем Вас в нашем Банкомате!!!")
print("Банкомат выдаёт купюры кратные номиналу в 10грн")
while sum:
    
    if sum == 1:
        sum = int(input("Введите сумму для снятия: "))
        print('')
    sum_out = str(sum)
    
    if not sum % 10 and sum:
        for i in L2:
            if sum >= i:
                
                if i == 20 or i == 200:
                    if sum > i*10:
                        sum -= i*8
                        l3[i]= 8
                    else:
                        l3[i] = sum//i
                        sum -= (sum//i)*i
                        
                elif i == 1000:
                    l3[i] = sum//i
                    sum -= (sum//i)*i
                        
                else:                   # купюры номиналом 10, 50, 100, 500грн
                    if sum > i*10: 
                        sum -= i*9
                        l3[i]= 9
                    else:
                        l3[i] = sum//i
                        sum -= (sum//i)*i             
        for i in L:
            if i == 100 and sum == 100:
                pass
            elif (i == 50 and sum == 100) or (i == 200 and sum == 400) or (i == 100 and sum == 200):
                l3[i] += 1
                sum -= i
            else:
                if sum >= i:
                    l3[i] += sum//i
                    sum -= (sum//i)*i
            
                
        for key, value in l3.items():
            print("Выдаём", value, "купюр по", str(key)+"грн")
            
        print("\nВаша сумма в размере", sum_out + "грн выдана полностью!\n")  
    else:
        print("""Извините, банкомат выдаёт купюры кратные номиналу в "10грн"
Введите пожалуйста сумму, удовлетворяющую требованиям банкомата\n""")

    

      
    sum = int(input("""Если хотите продолжить - Введите новую сумму 
Если хотите закончить - Введите число "0"
    Введите сумму: """))

print("Спасибо что пользуетесь услугами нашего БАНКОМАТА!")
