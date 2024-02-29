

class Vacancy:
    """
    Класс для работы с вакансией
    """
    def __init__(self, name=None, payment_to=0, payment_from=0, town=None, requirement=None):
        self.name = name
        try:
            self.payment_to: int = payment_to
        except AttributeError:
            self.payment_to: int = 0
        try:
            self.payment_from: int = payment_from
        except AttributeError:
            self.payment_from: int = 0
        self.town = town
        self.requirement = requirement
        if self.payment_to is None and self.payment_from is None:
            self.salary = 0
        elif self.payment_from is None:
            self.salary = self.payment_to
        elif self.payment_to is None:
            self.salary = self.payment_from
        else:
            self.salary = (self.payment_from + self.payment_to) / 2

    def __lt__(self, other):
        return self.salary < other.salary

    def __str__(self):
        return f'''Название вакансии: {self.name}
Средняя зарплата: {int(self.salary)}
Город: {self.town}
Описание: {self.requirement[0:100]}'''
