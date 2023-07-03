import os
import time
from abc import ABC, abstractmethod

import requests


class API(ABC):
    """
    Абстрактный класс для работы с API сайтов
    """

    @abstractmethod
    def get_vacancies(self, profession):
        """
        Абстрактный метод для получения словаря с данными о вакансиях
        :param profession: название должности
        """
        pass


class SuperJobAPI(API):
    """
    Класс для работы с API сайта SuperJob
    """

    URL = 'https://api.superjob.ru/2.0/vacancies/'
    HEADERS = {
        "X-Api-App-Id": os.getenv('SUPERJOB_API_KEY')
    }

    def get_vacancies(self, profession: str):
        """
        Получает и возвращает словарь с данными о вакансиях
        :param profession: название должности
        :return: словарь с данными о вакансиях
        """
        profession = profession.strip()

        vacancies_list = []
        page, pages = 0, 1
        params = {
            "keyword": profession,
            "count": 100,
            "page": page
        }

        while page < pages:
            time.sleep(1)

            vacancies = requests.get(self.URL, headers=self.HEADERS, params=params).json()

            vacancies_list.extend(vacancies['objects'])
            pages = vacancies['total'] // 100
            page += 1

        return vacancies_list

    @staticmethod
    def formate_data(vacancies: list):
        """
        Возвращает данные о вакансиях в требуемом формате
        :return: список словарей с данными о вакансиях
        """
        vacancies_for_return = []

        validator = SuperJobVacancyDataValidator()

        for vacancy in vacancies:
            address = validator.validate_address(vacancy['address'])
            profession = validator.validate_profession(vacancy['profession'])
            salary_from = validator.validate_salary(vacancy['payment_from'], vacancy['currency'])
            salary_to = validator.validate_salary(vacancy['payment_to'], vacancy['currency'])
            url = validator.validate_url(vacancy['link'])
            requirements = validator.validate_vacancy_requirement(vacancy['candidat'])

            vacancies_for_return.append({'profession': profession,
                                         'salary_from': salary_from,
                                         'salary_to': salary_to,
                                         'url': url,
                                         'requirements': requirements,
                                         'address': address
                                         })

        return vacancies_for_return


class HeadHunterAPI(API):
    """
    Класс для работы с API сайта HeadHunter
    """

    URL = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, profession: str):
        """
        Получает и возвращает словарь с данными о вакансиях
        :param profession: название должности
        :return: словарь с данными о вакансиях
        """
        profession = profession.strip()

        vacancies_list = []
        page, pages = 0, 1
        params = {
            "text": profession,
            "search_field": 'name',
            "page": page,
            "per_page": 100
        }

        while page < pages:
            time.sleep(1)

            vacancies = requests.get(self.URL, params=params).json()

            vacancies_list.extend(vacancies['items'])
            pages = vacancies['pages']
            page += 1

        return vacancies_list

    @staticmethod
    def formate_data(vacancies: list):
        """
        Возвращает данные о вакансиях в требуемом формате
        :return: список словарей с данными о вакансиях
        """
        vacancies_for_return = []

        validator = HeadHunterVacancyDataValidator()

        for vacancy in vacancies:
            profession = validator.validate_profession(vacancy['name'])
            address = validator.validate_address(vacancy['address'])
            salary_from, salary_to = validator.validate_salary(vacancy['salary'])
            requirement = validator.validate_vacancy_requirement(vacancy['snippet'])
            url = validator.validate_url(vacancy['url'])

            vacancies_for_return.append({'profession': profession,
                                         'salary_from': salary_from,
                                         'salary_to': salary_to,
                                         'url': url,
                                         'requirements': requirement,
                                         'address': address})

        return vacancies_for_return


class VacancyDataValidator(ABC):
    """
    Абстрактный класс для проверки данных добавляемых в класс Vacancy
    """

    @staticmethod
    @abstractmethod
    def validate_profession(profession):
        """
        Абстрактный метод для проверки правильности формата должности
        """
        pass

    @staticmethod
    @abstractmethod
    def validate_salary(salary, currency):
        """
        Абстрактный метод для проверки правильности формата зарплаты
        """
        pass

    @staticmethod
    @abstractmethod
    def validate_url(url):
        """
        Абстрактный метод для проверки правильности формата ссылки
        """
        pass

    @staticmethod
    @abstractmethod
    def validate_address(address):
        """
        Абстрактный метод для проверки правильности формата адреса
        """
        pass

    @staticmethod
    @abstractmethod
    def validate_vacancy_requirement(vacancy_requirement):
        """
        Абстрактный метод для проверки правильности формата требований к вакансии
        """
        pass


class SuperJobVacancyDataValidator(VacancyDataValidator):
    """
    Класс для проверки данных добавляемых в класс Vacancy с платформы SuperJob
    """

    @staticmethod
    def validate_profession(profession):
        """
        Проверяет правильность формата должности и возвращает в нужном формате
        :param profession: данные о должности
        :return: данные о должности в str
        """
        if profession is None:
            return 'Должность не указана'

        return profession

    @staticmethod
    def validate_salary(salary, currency):
        """
        Проверяет правильность формата зарплаты и возвращает в нужном формате
        :param currency: валюта
        :param salary: данные о зарплате
        :return: данные о зарплате в int
        """
        rate = 1

        if currency != 'rub':
            translator = CurrencyTranslator()
            rate = translator.get_exchange_rate(currency.upper())

        if salary is None:
            salary = 0

        return round(int(salary) / rate)

    @staticmethod
    def validate_address(address):
        """
        Проверяет правильность формата адреса и возвращает в нужном формате
        :param address: данные об адресе
        :return: данные об адресе в str
        """
        if address is None:
            return 'Нет информации об адресе'

        return address

    @staticmethod
    def validate_url(url):
        """
        Проверяет правильность формата url и возвращает в нужном формате
        :param url: данные об url
        :return: данные об url в str
        """
        if url is None:
            return 'url не указан'

        return url

    @staticmethod
    def validate_vacancy_requirement(vacancy_requirement):
        """
        Проверяет правильность формата требований и возвращает в нужном формате
        :param vacancy_requirement: данные об адресе
        :return: данные об адресе в str
        """
        if vacancy_requirement is None:
            return 'Требования к вакансии не указаны'

        return vacancy_requirement


class HeadHunterVacancyDataValidator(VacancyDataValidator):
    """
    Класс для проверки данных добавляемых в класс Vacancy с платформы HeadHunter
    """

    @staticmethod
    def validate_profession(profession):
        """
        Проверяет правильность формата должности и возвращает в нужном формате
        :param profession: данные о должности
        :return: данные о должности в str
        """
        if profession is None:
            return 'Должность не указана'

        return profession

    @staticmethod
    def validate_salary(salary, currency=None):
        """
        Проверяет правильность формата зарплаты и возвращает в нужном формате
        :param currency: валюта
        :param salary: данные о зарплате
        :return: данные о зарплате в int
        """
        if salary is None:
            return 0, 0

        rate = 1
        salary_from = salary['from']
        salary_to = salary['to']

        if salary_from is None:
            salary_from = 0

        if salary_to is None:
            salary_to = 0

        if salary.get('currency') is not None:
            currency = salary['currency']

            if currency != 'RUR':
                translator = CurrencyTranslator()
                rate = translator.get_exchange_rate(currency)

        return round(int(salary_from) / rate), round(int(salary_to) / rate)

    @staticmethod
    def validate_address(address):
        """
        Проверяет правильность формата адреса и возвращает в нужном формате
        :param address: данные об адресе
        :return: данные об адресе в str
        """
        if address is None:
            return 'Нет информации об адресе'

        if address['raw'] is not None:
            return address['raw']

        city, street, building = address['city'], address['street'], address['building']

        if address['city'] is None:
            city = ''

        if address['street'] is None:
            street = ''

        if address['building'] is None:
            building = ''

        return f'{city}, {street}, {building}'

    @staticmethod
    def validate_url(url):
        """
        Проверяет правильность формата url и возвращает в нужном формате
        :param url: данные об url
        :return: данные об url в str
        """
        if url is None:
            return 'url не указан'

        return url

    @staticmethod
    def validate_vacancy_requirement(vacancy_requirement):
        """
        Проверяет правильность формата требований и возвращает в нужном формате
        :param vacancy_requirement: данные об адресе
        :return: данные об адресе в str
        """
        if vacancy_requirement is None:
            return 'Требования к вакансии не указаны'

        requirement = vacancy_requirement['requirement']
        responsibility = vacancy_requirement['responsibility']

        if requirement is None:
            requirement = ''

        if responsibility is None:
            responsibility = ''

        return f'{requirement} {responsibility}'


class CurrencyTranslator:
    """
    Класс для получения курса валют
    """
    URL = "https://api.apilayer.com/exchangerates_data/latest"
    PARAMS = {
        'base': 'RUB'
    }
    HEADERS = {
        "apikey": os.environ.get('EXCHANGE_RATE_API_KEY')
    }

    def get_exchange_rate(self, currency):
        """
        Возвращает курс валюты
        :return: курс валюты
        """
        currency = currency.upper()
        response = requests.request("GET", self.URL, headers=self.HEADERS, params=self.PARAMS)

        status_code = response.status_code

        if status_code == 200:
            result = response.json()
        else:
            return 1

        return result['rates'][currency]
