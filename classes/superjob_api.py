import requests

from classes.abstract_classes.api import API
import os


class SuperJobAPI(API):
    """
    Класс для подключения к сайту superjob.ru и поиска там вакансий
    """

    def get_vacancies(self, keyword, quantity):
        secret_key = {'X-Api-App-Id': os.getenv('SJ-API-KEY')}
        url_sj = 'https://api.superjob.ru/2.0/vacancies/'
        vacancies_sj = requests.get(url_sj, headers=secret_key, params={'keyword': str(keyword)}).json()
        vacancy = {}
        for i in range(0, quantity):
            try:
                vacan = {
                    'name': vacancies_sj['objects'][i]['profession'],
                    'payment_to': vacancies_sj['objects'][i]['payment_to'],
                    'payment_from': vacancies_sj['objects'][i]['payment_from'],
                    'town': vacancies_sj['objects'][i]['town']['title'],
                    'requirement': vacancies_sj['objects'][i]['candidat']
                }
            except TypeError:
                vacan = {
                    'name': vacancies_sj['objects'][i]['profession'],
                    'payment_to': 0,
                    'payment_from': 0,
                    'town': vacancies_sj['objects'][i]['town']['title'],
                    'requirement': vacancies_sj['objects'][i]['candidat']
                }
            vacancy[vacancies_sj['objects'][i]['id']] = vacan
        return vacancy
