""""Этот модуль собирает в себя все настройки для работы с объектами
(EN)
This module collects all the settings for working with objects
"""

from datetime import datetime
import traceback
from custom_exceptions import EmailAlreadyExistsException
import dv_rc
from mpl import Employee


def main():
    """
    This function collects all objects for further calling them!
    """
    # rec1 = dv_rc.Recruiter("Artem", 90)
    # rec2 = dv_rc.Recruiter("Darya", 80)
    # dev1 = dv_rc.Developer("Alex", 100, ["Python", "C#", "Java", "PHP"])
    # dev2 = dv_rc.Developer("Serg", 105, ["Python", "JS", "Java"])

    # # Приветствие
    # print(rec1.work())
    # print(dev1.work())

    # # вывод--> Должность : Имя
    # print(rec1)
    # print(rec2)
    # print(dev1)
    # print(dev2)

    # # Сравнивание з/п
    # print(rec1 > rec2)
    # print(rec2 < dev1)
    # print(rec1 >= dev2)
    # print(rec1 == dev1)

    # # высчитывание зп за кол-во отработанных дней
    # print(rec1.check_salary(28))
    # print(rec1.check_salary(26))
    # print(dev1.check_salary(30))
    # print(dev2.check_salary(29))

    # # высчитываем зп за кол-во дней от начала месяца по сегодняшнюю дату
    # print(dev1.check_salary())
    # print(dv_rc.Developer("Anton", 230, ["ppp", "sss"]).check_salary())

    # # Проверка по классу Developer
    # print(dev1 > dev2)

    # # Создане нового обЪекта
    # print((dev1 + dev2).__dict__)
    emp1 = Employee("sasha", 1000, "skladinstrumenta@gmail.com")
    print(emp1.email)


if __name__ == "__main__":
    try:
        main()
    except EmailAlreadyExistsException:
        print("Exception name EmailAlreadyExistsException is found")
        log_message = f"{datetime.now()} \n{traceback.format_exc()}"
        with open("logs.txt", "a+") as lp:
            lp.write(log_message + "\n\n")
