from classes.headhunter_api import HeadHunterAPI


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    :return: словарь найденных вакансий по запросу пользователя
    """
    quantity = int(input('Введите количество вакансий для поиска:'))
    keyword = str(input('Введите ключевое слово:'))
    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies(keyword, quantity)
    print(f'Найдено {len(vacancies)} вакансий')
    return vacancies


def choice_command():
    """
    Функция для выбора действий пользователя
    :return: команда пользователя
    """
    command = int(input('Выберите действия:\n'
                        '1 - найти другие вакансии\n'
                        '2 - вывести найденные вакансии в терминале\n'
                        '3 - отсортировать по зарплате\n'
                        '4 - удалить вакансию из файла\n'
                        '5 - выйти\n'))
    return command
