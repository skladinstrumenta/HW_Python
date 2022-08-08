            # ЗАДАНИ №2
# Создать структуру данных для студентов из имен и фамилий, можно случайных. 
# Придумать структуру данных, чтобы указывать, 
# в какой группе учится студент (Группы Python, FrontEnd, FullStack, Java). 
# Студент может учиться в нескольких группах. Затем вывести:

# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

dict1 = {
"Paranichev Aleksandr":["Python", "FullStack"], 
"Podolyak Michail":["FullStack", "FrontEnd", "Java"],
"Arestovich Alexey":["Python","FullStack", "FrontEnd", "Java"],
"Frank Lampard":["FrontEnd", "Java"],
"Lisichka Pavel":["FrontEnd", "FullStack"],
"Zelenskiy Vladimir":["Python", "Java"], 
"Perevyazko Sergey":["FrontEnd"]
}

    # студентов, которые учатся в двух и более группах

def one_more(dict):
    l1 = list(keys for keys, values in dict.items() if len(values) > 1)
    return "\n".join(l1)
print("\nСтуденты которые учатся в двух и более группах:\n" + one_more(dict1))

    # студентов, которые не учатся на фронтенде

def not_frontend(dict):
    l1 = list(keys for keys, values in dict.items() if "FrontEnd" not in values)
    return "\n".join(l1)
print("\nСтуденты, которые не учатся на Фронтенде:\n" + not_frontend(dict1))

    # студентов, которые изучают Python или Java

def Pa_Ja(dict):
    l1 = list(keys for keys, values in dict.items() if "Python" in values or "Java" in values)
    return "\n".join(l1)
print("\nСтуденты, которые изучают Python или Java:\n" + Pa_Ja(dict1))