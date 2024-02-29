from classes.abstract_classes.api import API
import requests


class HeadHunterAPI(API):
    """
    Класс для подключения к сайту hh.ru и поиска там вакансий
    """

    def get_vacancies(self, keyword, quantity):
        url_hh = 'https://api.hh.ru/vacancies'
        vacancies_hh = requests.get(url_hh, params={'text': keyword, 'currency': 'RUR', 'host': 'hh.ru'}).json()
        vacancy = {}
        for i in range(0, quantity):
            try:
                vacan = {
                    'name': vacancies_hh['items'][i]['name'],
                    'payment_to': vacancies_hh['items'][i]['salary']['to'],
                    'payment_from': vacancies_hh['items'][i]['salary']['from'],
                    'town': vacancies_hh['items'][i]['area']['name'],
                    'requirement': vacancies_hh['items'][i]['snippet']['requirement']
                }
            except TypeError:
                vacan = {
                    'name': vacancies_hh['items'][i]['name'],
                    'payment_to': 0,
                    'payment_from': 0,
                    'town': vacancies_hh['items'][i]['area']['name'],
                    'requirement': vacancies_hh['items'][i]['snippet']['requirement']
                }
            vacancy[vacancies_hh['items'][i]['id']] = vacan
        return vacancy
