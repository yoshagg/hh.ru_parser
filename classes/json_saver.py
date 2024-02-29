from classes.abstract_classes.json_save import JSONSave
import os
import json
from classes.vacancy import Vacancy


class JSONSaver(JSONSave):
    """
    Класс для сохранения данных в json-файл
    """
    def __init__(self, file='saved_vacancies.json'):
        self.file = file

    def to_json(self, getted_vac):
        """
        Функция для первичного сохранения в пустой файл
        :param getted_vac: словарь из вакансий
        :return: None
        """
        with open(os.path.abspath(self.file), 'w', encoding='utf=8') as f:
            json.dump(getted_vac, f, ensure_ascii=False, indent=2)

    def add_vacancy(self, getted_vac):
        """
        Функция для добавления вакансий в уже заполненный файл
        :param getted_vac: словарь из вакансий
        :return: None
        """
        getted_vac = json.dumps(getted_vac)
        getted_vac = json.loads(str(getted_vac))
        b = json.load(open(os.path.abspath(self.file), 'r', encoding='utf=8'))
        for key, items in getted_vac.items():
            b[key] = items
        json.dump(b, open(os.path.abspath(self.file), 'w', encoding='utf=8'), ensure_ascii=False, indent=2)

    def read_vacancy(self):
        b = json.load(open(os.path.abspath(self.file), 'r', encoding='utf=8'))
        vacancies_list = []
        for key, item in b.items():
            vacancies_list.append(Vacancy(item['name'],
                                          item['payment_to'],
                                          item['payment_from'],
                                          item['town'],
                                          item['requirement']))
        return vacancies_list

    def delete_vacancy(self, del_vac):
        """
        Функция для удаления вакансии из файла
        :param del_vac: экземпляр класса Vacancy
        :return: None
        """
        del_vac = json.dumps(del_vac.__dict__)
        del_vac = json.loads(str(del_vac))
        name = del_vac['name']
        town = del_vac['town']
        b = json.load(open(os.path.abspath(self.file), 'r', encoding='utf=8'))
        for key, items in list(b.items()):
            if items['name'] == name and items['town'] == town:
                b.pop(key, items)
        json.dump(b, open(os.path.abspath(self.file), 'w', encoding='utf=8'), ensure_ascii=False, indent=2)
