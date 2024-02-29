from abc import ABC, abstractmethod


class JSONSave(ABC):
    """
    Абстрактный класс для сохранения данных в json-файл
    """
    @abstractmethod
    def to_json(self, getted_vac):
        """
        Функция для первичного сохранения в пустой файл
        :param getted_vac: словарь из вакансий
        :return: None
        """
        pass

    @abstractmethod
    def add_vacancy(self, getted_vac):
        """
        Функция для добавления вакансий в уже заполненный файл
        :param getted_vac: словарь из вакансий
        :return: None
        """
        pass

    @abstractmethod
    def delete_vacancy(self, getted_vac):
        """
        Функция для удаления вакансии из файла
        :param getted_vac: экземпляр класса Vacancy
        :return: None
        """
        pass
