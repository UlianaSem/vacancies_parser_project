import re


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
    def add_to_class(cls, vacancies_data: dict):
        """
        Инициализирует экземпляры класса Vacancy из переданных данных
        :param vacancies_data: данные о вакансиях
        """
        if vacancies_data.get('objects') is not None:
            if vacancies_data['objects'] != [] and vacancies_data['total'] != 0:

                for vacancy in vacancies_data['objects']:
                    cls(vacancy['profession'], int(vacancy['payment_from']),  int(vacancy['payment_to']),
                        vacancy['link'], vacancy['candidat'], vacancy['address'])

        if vacancies_data.get('items') is not None:
            if vacancies_data['items'] != [] and vacancies_data['found'] != 0:

                for vacancy in vacancies_data['items']:

                    address = cls.validate_address(vacancy['address'])
                    salary_from, salary_to = cls.validate_salary(vacancy['salary'])

                    cls(vacancy['name'], salary_from, salary_to, vacancy['url'], vacancy['snippet']['requirement'] +
                        '\n' + vacancy['snippet']['responsibility'], address)

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

    @classmethod
    def get_vacancy_by_salary(cls, salary):
        """
        Ищет вакансии по зарплате и возвращает список с вакансиями
        :param salary: зарплата для поиска
        :return: список с вакансиями
        """
        salary_for_check = []
        vacancies_for_response = []

        for salary_ in re.split(r"[/ -]", salary):
            if salary_.isdigit():
                salary_for_check.append(int(salary_))

        vacancies = cls.all

        for vacancy in vacancies:
            if vacancy.salary_from >= salary_for_check[0]:
                vacancies_for_response.append(vacancy)

        return vacancies_for_response

    @classmethod
    def get_vacancy_by_address(cls, address):
        """
        Ищет вакансии по адресу и возвращает список с вакансиями
        :param address: адрес для поиска
        :return: список с вакансиями
        """
        address = set(re.split(r', | ', address.strip().lower()))
        vacancies_for_response = []

        vacancies = cls.all

        for vacancy in vacancies:
            address_for_check = set(re.split(r', | ', vacancy.work_address.lower()))
            if address.issubset(address_for_check):
                vacancies_for_response.append(vacancy)

        return vacancies_for_response

    @staticmethod
    def validate_address(address):
        """
        Проверяет правильность формата адреса и возвращает в нужном формате
        :param address: данные об адресе
        :return: данные об адресе в str
        """
        if address is None:
            return 'Нет информации об адресе'

        return address['raw']
