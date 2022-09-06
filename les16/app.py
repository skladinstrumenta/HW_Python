""""Этот модуль собирает в себя все настройки для работы с объектами
(EN)
This module collects all the settings for working with objects
"""

import dv_rc


if __name__ == "__main__":
    rec1 = dv_rc.Recruiter("Artem", 90)
    rec2 = dv_rc.Recruiter("Darya", 80)
    dev1 = dv_rc.Developer("Alex", 100, ["Python", "C#", "Java", "PHP"])
    dev2 = dv_rc.Developer("Serg", 105, ["Python", "JS", "Java"])

    # Приветствие
    print(rec1.work())
    print(dev1.work())

    # вывод--> Должность : Имя
    print(rec1)
    print(rec2)
    print(dev1)
    print(dev2)

    # Сравнивание з/п
    print(rec1 > rec2)
    print(rec2 < dev1)
    print(rec1 >= dev2)
    print(rec1 == dev1)

    # высчитывание зп за кол-во отработанных дней
    print(rec1.check_salary(28))
    print(rec1.check_salary(26))
    print(dev1.check_salary(30))
    print(dev2.check_salary(29))

    # высчитываем зп за кол-во дней от начала месяца по сегодняшнюю дату
    print(dev1.check_salary())
    print(dv_rc.Developer("Anton", 230, ["ppp", "sss"]).check_salary())

    # Проверка по классу Developer
    print(dev1 > dev2)

    # Создане нового обЪекта
    print((dev1 + dev2).__dict__)
