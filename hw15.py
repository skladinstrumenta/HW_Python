class Employee:
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def work(self):
        return "I come to the office."

    # def __call__(self):
    #     return self.salary

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

    def check_salary(self, days):
        return self.salary * days


class Recruiter(Employee):
    def __init__(self, name: str, salary: int):
        super().__init__(name, salary)

    def work(self):
        return "I come to the office and start to hiring."

    def __str__(self):
        return f"{__class__.__name__} : {self.name}"


class Developer(Employee):
    def __init__(self, name: str, salary: int, tech_stack: list):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def work(self):
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
        return Developer(name=self.name + " " + other.name, salary=max(self.salary, other.salary), tech_stack=set(self.tech_stack + other.tech_stack))
        # name = self.name + " " + other.name
        # salary = max(self.salary, other.salary)
        # tech_stack = set(self.tech_stack + other.tech_stack)
        # return name, salary, tech_stack


if __name__ == "__main__":

    rec1 = Recruiter("Artem", 90)
    rec2 = Recruiter("Darya", 80)
    dev1 = Developer("Alex", 100, ["Python", "C#", "Java", "PHP"])
    dev2 = Developer("Serg", 105, ["Python", "JS", "Java"])

    # print(em)
# Приветствие
    # print(rec1.work())
    # print(dev1.work())

# вывод--> Должность : Имя
    # print(rec1)
    # print(rec2)
    # print(dev1)
    # print(dev2)

# Сравнивание з/п
    print(rec1 > rec2)
    print(rec2 < dev1)
    print(rec1 >= dev2)
    print(rec1 == dev1)

# высчитывание зп за кол-во отработанных дней
    # print(rec1.check_salary(28))
    # print(rec1.check_salary(26))
    # print(dev1.check_salary(30))
    # print(dev2.check_salary(29))

# Проверка по классу Developer
    print(dev1 > dev2)

# Создане нового обЪекта
    print((dev1 + dev2).__dict__)
