import re
from abc import ABC, abstractmethod


class Vacancy:
    """
    Класс для представления вакансии
    """

    all = []

    def __init__(self, profession, salary_from, salary_to, vacancy_url, vacancy_requirement, work_address):
        """
        Инициализирует атрибуты экземпляра класса Vacancy
        :param profession: название должности
        :param salary_from: нижний предел зарплаты
        :param salary_to: верхний предел зарплаты
        :param vacancy_url: ссылка на вакансию
        :param vacancy_requirement: требования вакансии или описание
        :param work_address: адрес работы
        """
        self.__profession = profession
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__vacancy_url = vacancy_url
        self.__vacancy_requirement = vacancy_requirement
        self.__work_address = work_address

        self.all.append(self)

    def __le__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from <= other.__salary_from

    def __lt__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from < other.__salary_from

    def __eq__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from == other.__salary_from

    def __ge__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from >= other.__salary_from

    def __gt__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from > other.__salary_from

    @property
    def profession(self):
        return self.__profession

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def vacancy_url(self):
        return self.__vacancy_url

    @property
    def vacancy_requirement(self):
        return self.__vacancy_requirement

    @property
    def work_address(self):
        return self.__work_address

    @classmethod
    def add_to_class_from_superjob(cls, vacancies_data: dict):
        """
        Инициализирует экземпляры класса Vacancy из переданных данных API SuperJob
        :param vacancies_data: данные о вакансиях
        """
        validator = SuperJobVacancyDataValidator()

        if vacancies_data['objects'] != [] and vacancies_data['total'] != 0:

            for vacancy in vacancies_data['objects']:
                address = validator.validate_address(vacancy['address'])
                profession = validator.validate_profession(vacancy['profession'])
                salary_from = validator.validate_salary(vacancy['payment_from'])
                salary_to = validator.validate_salary(vacancy['payment_to'])
                url = validator.validate_url(vacancy['link'])
                requirements = validator.validate_vacancy_requirement(vacancy['candidat'])

                cls(profession, salary_from, salary_to, url, requirements, address)

    @classmethod
    def add_to_class_from_headhunter(cls, vacancies_data: dict):
        """
        Инициализирует экземпляры класса Vacancy из переданных данных API HeadHunter
        :param vacancies_data: данные о вакансиях
        """
        validator = HeadHunterVacancyDataValidator()

        if vacancies_data['items'] != [] and vacancies_data['found'] != 0:

            for vacancy in vacancies_data['items']:
                profession = validator.validate_profession(vacancy['name'])
                address = validator.validate_address(vacancy['address'])
                salary_from, salary_to = validator.validate_salary(vacancy['salary'])
                requirement = validator.validate_vacancy_requirement(vacancy['snippet'])
                url = validator.validate_url(vacancy['url'])

                cls(profession, salary_from, salary_to, url, requirement, address)


class VacancyFilter:
    """
    Класс для фильтрации вакансий
    """

    @staticmethod
    def get_vacancy_by_salary(vacancies, salary):
        """
        Ищет вакансии по зарплате и возвращает список с вакансиями
        :param vacancies: список с экземплярами класса Vacancy
        :param salary: зарплата для поиска
        :return: список с вакансиями
        """
        salary_for_check = []
        vacancies_for_response = []

        for salary_ in re.split(r"[/ -]", salary):
            if salary_.isdigit():
                salary_for_check.append(int(salary_))

        if len(salary_for_check) == 0:
            return 'Введите хотя бы одно число'

        for vacancy in vacancies:
            if vacancy.salary_from >= salary_for_check[0] or vacancy.salary_to >= salary_for_check[0]:
                vacancies_for_response.append(vacancy)

        return vacancies_for_response

    @staticmethod
    def get_vacancy_by_address(vacancies, address):
        """
        Ищет вакансии по адресу и возвращает список с вакансиями
        :param vacancies: список с экземплярами класса Vacancy
        :param address: адрес для поиска
        :return: список с вакансиями
        """
        address = set(re.split(r', | ', address.strip().lower()))
        vacancies_for_response = []

        for vacancy in vacancies:
            address_for_check = set(re.split(r', | ', vacancy.work_address.lower()))
            if address.issubset(address_for_check):
                vacancies_for_response.append(vacancy)

        return vacancies_for_response


class VacancyBuilder:
    """
    Класс для построения ответа о вакансии
    """

    @staticmethod
    def build_response(vacancy: Vacancy):
        """
        Строит ответ в нужном формате
        :return: строка в нужном формате"""
        return f'''Должность: {vacancy.profession}
Зарплата: от {vacancy.salary_from} до {vacancy.salary_to}
Ссылка на вакансию: {vacancy.vacancy_url}
Адрес работы: {vacancy.work_address}'''


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
    def validate_salary(salary):
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
    def validate_salary(salary):
        """
        Проверяет правильность формата зарплаты и возвращает в нужном формате
        :param salary: данные о зарплате
        :return: данные о зарплате в int
        """
        if salary is None:
            salary = 0

        return int(salary)

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
    def validate_salary(salary):
        """
        Проверяет правильность формата зарплаты и возвращает в нужном формате
        :param salary: данные о зарплате
        :return: данные о зарплате в int
        """
        if salary is None:
            return 0, 0

        salary_from = salary['from']
        salary_to = salary['to']

        if salary_from is None:
            salary_from = 0

        if salary_to is None:
            salary_to = 0

        return int(salary_from), int(salary_to)

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
