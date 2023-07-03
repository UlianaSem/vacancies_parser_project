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
    def add_to_class(cls, vacancies_data):
        """
        Инициализирует экземпляры класса Vacancy
        :param vacancies_data: данные о вакансиях
        """

        if vacancies_data:

            for vacancy in vacancies_data:

                cls(vacancy['profession'], vacancy['salary_from'], vacancy['salary_to'], vacancy['url'],
                    vacancy['requirements'], vacancy['address'])


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
            raise Exception('Введите хотя бы одно число')

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
