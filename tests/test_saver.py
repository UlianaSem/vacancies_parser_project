import pytest

import src.saver
import src.vacancy


@pytest.fixture
def get_saver_for_test():
    return src.saver.JSONSaver(), src.saver.CSVSaver()


def test_get_data__(get_saver_for_test):
    """
    Проверяет корректность получения данных их класса
    """
    src.vacancy.Vacancy('Developer', 100000, 110000, 'www.test.ru', 'Some requirements', 'Some address')

    json, csv = get_saver_for_test

    assert json.get_data__() == '[\n  {\n    "profession": "Developer",\n    "salary_from": 100000,\n    "salary_to": ' \
                                '110000,\n    "vacancy_url": "www.test.ru",\n    "vacancy_requirement": "Some ' \
                                'requirements",\n    "work_address": "Some address"\n  }\n]'
    assert csv.get_data__() == [{'profession': 'Developer', 'salary_from': 100000, 'salary_to': 110000,
                                 'vacancy_requirement': 'Some requirements', 'vacancy_url': 'www.test.ru',
                                 'work_address': 'Some address'}]


def test_get_vacancy_by_salary(get_saver_for_test):
    """
    Проверяет правильность фильтра по зарплате
    :param get_saver_for_test: объект класса JSONSaver и CSVSaver
    """
    json, csv = get_saver_for_test

    json.path_to_file = '../tests/test_vacancies.json'
    csv.path_to_file = '../tests/test_vacancies.csv'

    assert json.get_vacancy_by_salary('Test') == 'Введите хотя бы одно число'
    assert csv.get_vacancy_by_salary('Test') == 'Введите хотя бы одно число'
    assert json.get_vacancy_by_salary('500000') == []
    assert csv.get_vacancy_by_salary('500000') == []
    assert json.get_vacancy_by_salary('200000') == [{'profession': 'Junior backend-разработчик (Python)',
                                                     'salary_from': 100000,
                                                     'salary_to': 200000,
                                                     'vacancy_requirement': 'Высшее или средне специальное образов'
                                                                            'ание в области '
                                                                            'ИТ. Хорошие знания '
                                                                            '<highlighttext>Python</highlighttext>. '
                                                                            'Знание одного '
                                                                            'из фреймворков <highlighttext>Python</hi'
                                                                            'ghlighttext> '
                                                                            '(DRF или FastAPI). \n'
                                                                            'Оптимизация веб-приложений и веб-сайто'
                                                                            'в. Доработка '
                                                                            'функциональности на DRF или FastAPI. '
                                                                            'Работа над '
                                                                            'улучшением функциональности и микрос'
                                                                            'ервисов. ',
                                                     'vacancy_url': 'https://api.hh.ru/vacancies/82129003?host=hh.ru',
                                                     'work_address': 'Нет информации об адресе'}]
    assert csv.get_vacancy_by_salary('200000') == [{'profession': 'Junior backend-разработчик (Python)',
                                                    'salary_from': '100000',
                                                    'salary_to': '200000',
                                                    'vacancy_requirement': 'Высшее или средне специальное образовани'
                                                                           'е в области '
                                                                           'ИТ. Хорошие знания '
                                                                           '<highlighttext>Python</highlighttext>. '
                                                                           'Знание одного '
                                                                           'из фреймворков <highlighttext>Python</hi'
                                                                           'ghlighttext> '
                                                                           '(DRF или FastAPI). \n'
                                                                           'Оптимизация веб-приложений и веб-сайтов.'
                                                                           ' Доработка '
                                                                           'функциональности на DRF или FastAPI. Ра'
                                                                           'бота над '
                                                                           'улучшением функциональности и микросер'
                                                                           'висов. ',
                                                    'vacancy_url': 'https://api.hh.ru/vacancies/82129003?host=hh.ru',
                                                    'work_address': 'Нет информации об адресе'}]


def test_get_vacancy_by_address(get_saver_for_test):
    """
    Проверяет правильность фильтра по адресу
    :param get_saver_for_test: объект класса JSONSaver и CSVSaver
    """
    json, csv = get_saver_for_test

    json.path_to_file = '../tests/test_vacancies.json'
    csv.path_to_file = '../tests/test_vacancies.csv'

    assert json.get_vacancy_by_address('TestTestTest') == []
    assert csv.get_vacancy_by_address('TestTestTest') == []
    assert json.get_vacancy_by_address('Екатеринбург') == [{'profession': 'Junior Python Developer',
                                                            'salary_from': 40000,
                                                            'salary_to': 0,
                                                            'vacancy_requirement': 'Знание <highlighttext>Python</'
                                                                                   'highlighttext> 3. Опыт '
                                                                                   'работы с ORM (Django ORM, Peewee'
                                                                                   '). Навыки работы с '
                                                                                   'БД (PostgreSQL, Mongo). Будет плю'
                                                                                   'сом: Навыки '
                                                                                   'разработки...\n'
                                                                                   'Создание новых интересных фич. По'
                                                                                   'ддержка старой '
                                                                                   'функциональности. Написание тесто'
                                                                                   'в. Оптимизация '
                                                                                   'сервисов под высокие нагрузки. Сте'
                                                                                   'к технологий '
                                                                                   'следующий:',
                                                            'vacancy_url': 'https://api.hh.ru/vacancies/81960961?'
                                                                           'host=hh.ru',
                                                            'work_address': 'Екатеринбург, проспект Ленина, 8'}]
    assert csv.get_vacancy_by_address('Екатеринбург') == [{'profession': 'Junior Python Developer',
                                                           'salary_from': '40000',
                                                           'salary_to': '0',
                                                           'vacancy_requirement': 'Знание <highlighttext>Python</hig'
                                                                                  'hlighttext> 3. Опыт '
                                                                                  'работы с ORM (Django ORM, Peewee).'
                                                                                  ' Навыки работы с '
                                                                                  'БД (PostgreSQL, Mongo). Будет плю'
                                                                                  'сом: Навыки '
                                                                                  'разработки...\n'
                                                                                  'Создание новых интересных фич. П'
                                                                                  'оддержка старой '
                                                                                  'функциональности. Написание тест'
                                                                                  'ов. Оптимизация '
                                                                                  'сервисов под высокие нагрузки. '
                                                                                  'Стек технологий '
                                                                                  'следующий:',
                                                           'vacancy_url': 'https://api.hh.ru/vacancies/81960961?ho'
                                                                          'st=hh.ru',
                                                           'work_address': 'Екатеринбург, проспект Ленина, 8'}]
