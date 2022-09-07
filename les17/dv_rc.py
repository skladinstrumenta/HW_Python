"""Этот модуль включает в себя методы решения задачи с объектами связаннными
с классами DEVELOPER и RECRUITER
(EN)
This module includes methods for solving a problem with related objects.
with classes DEVELOPER and RECRUITER
"""
from mpl import Employee


class Recruiter(Employee):
    """В этом подклассе от родителя EMPLOYEE
    можно перезадачить объекты для работы конкретно с данной вакансией
    оприраясь на на родительский класс. В данном случае мы переделываем 
    структуру приветствия метода WORK
    (EN)
    In this subclass from parent EMPLOYEE
    you can reassign objects to work specifically with this vacancy
    leaning on on the parent class. In this case, we redo
    WORK method greeting structure
    """

    def __init__(self, name: str, salary: int):
        super().__init__(name, salary)

    def work(self):
        """
        Этот метод переопределяет метод WORK, 
        из родительского класса EMPLOYEE,
        и возвращает строку, которую говорят рекрутеры
        (EN)
        This method overrides the WORK method,
        from parent class EMPLOYEE,
        and returns the string that the recruiters say

        Returns:
            work: "I come to the office and start to hiring." -> string
        """

        return "I come to the office and start to hiring."

    def __str__(self):
        return f"{__class__.__name__} : {self.name}"


class Developer(Employee):
    """
    В этом подклассе от родителя EMPLOYEE
    можно переопределить и добавить методы 
    для работы конкретно с данной вакансией 
    оприраясь на родительский класс.
    В данном случае мы добавляем в изначальные аргументы
    параметр 'tech_stack' отвечающий за технические способности
    данного сотрудника. При помощи изменений в данном классе
    мы можем сравнить объектов данной специальности по этому параметру.  
    (EN)
    In this subclass from parent EMPLOYEE
    you can override and extend methods to work specifically 
    with this vacancy relying on the parent class.
    In this case, we add to the initial arguments
    parameter 'tech_stack' responsible for technical abilities
    this employee. With changes in this class
    we can compare objects of a given specialty by this parameter.
    """

    def __init__(self, name: str, salary: int, tech_stack: list = None):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def work(self):
        """
        Этот метод переопределяет метод WORK, 
        из родительского класса EMPLOYEE,
        и возвращает строку, которую говорят разработчики
        (EN)
        This method overrides the WORK method,
        from parent class EMPLOYEE,
        and returns the string that the developers say

        Returns:
            work: "I come to the office and start to coding." -> string
        """

        return "I come to the office and start to coding."

    def __str__(self):
        return f"{__class__.__name__} : {self.name}"

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __add__(self, other):
        return Developer(name=self.name + " " + other.name,
                         salary=max(self.salary, other.salary),
                         tech_stack=set(self.tech_stack + other.tech_stack))
