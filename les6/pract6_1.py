                # ЗАДАНИЕ №1
#Создать словарь оценок предполагаемых студентов 
# (Ключ - ФИ студента, значение - список оценок студентов). 
# Найти самого успешного и самого отстающего по среднему баллу.

names = "Paranichev", "Zelenskiy", "Lisichka", "Perevyazko"
grades = ([7, 10, 9], [10, 10, 9], [8, 8, 8], [3, 5, 7])
mid_grades = (round(sum(i)/len(i), 2) for i in grades)
dict_student = dict(zip(names, mid_grades))

print("Самый успешный студент на потоке с балом", max(dict_student.values()), "студент по фамилии", max(dict_student, key=dict_student.get))

print("Самый отстающий студент на потоке с балом", min(dict_student.values()), "студент по фамилии", min(dict_student, key=dict_student.get))