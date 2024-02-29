from abc import ABC, abstractmethod

class API(ABC):
    """
    Абстрактный класс для подключения к API сайтов
    """

    @abstractmethod
    def get_vacancies(self, keyword, quantity):
        pass
