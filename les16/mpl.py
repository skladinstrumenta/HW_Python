"""Этот модуль включает в себя методы решения задачи с объектами связаннными
с классом EMPLOYEE
(EN)
This module includes methods for solving a problem with related objects.
with class EMPLOYEE
"""

from calendar import Calendar as cl
from datetime import date as dt


class Employee:
    """Этот родительский класс предназначен для работы с объектами
    в базовых показаниямиб, в нём мы можем работать:
    - с приветсвием сотрудников;
    - с сравнениями объктов опирающихся на это класс;
    - высчитывания зароботной платы отработанных дней по календарю.
    (EN)
    This parent class is designed to work with objects
    in the basic indicationsb, in it we can work:
    - with greetings from employees;
    - with comparisons of objects based on this class;
    - calculation of wages for days worked according to the calendar.
    """
    today = dt.today()
    year = list(map(int, (str(today).split("-"))))[0]
    month = list(map(int, (str(today).split("-"))))[1]
    lastday = list(map(int, (str(today).split("-"))))[2]

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def work(self):
        # """
        # """
        """Эта функция возвращает строку, которую говорят все работники
        # (EN)
        # The function returns a string that all employies say

        _summary_

        Returns:
            _type_: string
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
        return self.salary() != other.salary()

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
