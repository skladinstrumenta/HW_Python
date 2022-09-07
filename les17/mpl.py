"""Этот модуль включает в себя методы решения задачи с объектами связаннными
с классом EMPLOYEE
(EN)
This module includes methods for solving a problem with related objects.
with class EMPLOYEE
"""

from calendar import Calendar as cl
from datetime import date as dt

from custom_exceptions import EmailAlreadyExistsException


class Employee:
    """Этот родительский класс предназначен для работы с объектами
    в базовых показаниямиб, в нём мы можем работать:
    - с приветсвием сотрудников;
    - с сравнениями объктов опирающихся на это класс;
    - высчитывания зароботной платы отработанных дней по календарю.
    Первоначально класс обретает от импортированного класса datetime.date
    сегодняшнюю дату, из которого берёт переменные year, month, lastday
    (EN)
    This parent class is designed to work with objects
    in the basic indicationsb, in it we can work:
    - greeting employees;
    - with comparisons of objects based on this class;
    - Calculation of the salary of worked days according to the calendar.
    Initially the class derives from the imported class datetime.date
    today's date, from which it takes the variables year, month, lastday
    """
    today = dt.today()
    year, month, lastday = today.year, today.month, today.day

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name: str, salary: int, email):
        self.name = name
        self.salary = salary
        self.email = email
        self.validate()
        self.save_email()

    def validate(self):
        """
        This method checks for a destination E-mail with a list,
        which we already have, and if there is such an E-mail in the list,
        then the method throws us an exception we created with the name
        EmailAlreadyExistsException
        Raises:
            EmailAlreadyExistsException: This email already exists
        """
        try:
            with open("emails.txt") as fp:
                if self.email.lower() in fp.read():
                    raise EmailAlreadyExistsException(
                        "This email already exists")
        except FileNotFoundError:
            pass

    def save_email(self):
        """
        This method saves the E-mail sent to us in the emails.txt file,
        if it doesn't repeat, thanks to the 'VALIDATE' method!
        """
        with open('emails.txt', "a+") as fp:
            fp.write(f"{self.email.lower()}\n")

    def work(self):
        """Эта функция возвращает строку, которую говорят все работники
        (EN)
        The function returns a string that all employies say

        Returns:
            work: "I come to the office." -> string
        """
        return "I come to the office."

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def check(self):
        """Эта функция берёт из модуля "calendar" класс "Calendar",
        из него достаёт списки недель по дням (от ПН до ВС),
        потом в каждом списке удаляет выходные дни,
        и в итоге возвращает количество отработанных дней
        (EN)
        This function takes the "Calendar" cls from the "calendar" module,
        from it gets lists of weeks by day (from Monday to Sunday),
        then in each list removes weekends,
        and finally returns the number of days worked

        Returns:
            check: worked days -> integer
        """
        list_weeks = cl().monthdayscalendar(self.year, self.month)
        ld = self.lastday
        new_list = []
        for i in list_weeks:
            if ld not in i:
                new_list.extend(i[:-2])
            else:
                for n in i[:-2]:
                    if n <= ld:
                        new_list.append(n)
                    else:
                        break
                break

        work_day = list(set(new_list))

        # Получаем окончательный список из дат рабочих дней
        if 0 in work_day:
            work_day.remove(0)

        # Получаем число количества отработанных дней
        len_workday = len(work_day)
        return (len_workday)

    def check_salary(self, days=None):
        """Эта функция возвращает нам зарплату сотрудника 
        за отработанные им дни.
        (EN)
        This function returns the employee's salary for the days he worked

        Args:
            days : integer. Defaults to None.

        Returns:
            check_salary: salary by working day
        """
        if days == None:
            days = self.check()
        return self.salary * days
