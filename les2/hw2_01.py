                # First level (IF)

age = int(input("please input your age: "))                  
if age >= 18:
    print("Поздравляю, Вы совершеннолетний")
    if age <= 21:
        print("но сигареты вам ещё не продадут")
    else:
        pass
    if age == 25 or age ==45:
        print("Вам в этом году нужно менять фотографию в паспорте")
        if age != 25:
            print("И обратите внимание на ветхость вашего паспорта, может пора поменять на пластиковый?")
        else:
            pass
    else:
        print("В этом году  Вам не придёться менять фотку в паспорте")         
else:
    print("Вы не достигли совершеннолетия")
    if 18 > age > 16:
        print("Но вы уже получили паспорт")
    else:
        print("Я вам даже больше скажу, молодой человек, у вас ещё даже паспорта нету!")
                                    
