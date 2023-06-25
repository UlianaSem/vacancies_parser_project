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
                    if vacancy['salary'] is None and vacancy['address'] is None:
                        salary_from = 0
                        salary_to = 0
                        address = 'Нет информации об адресе'
                    elif vacancy['salary'] is None:
                        salary_from = 0
                        salary_to = 0
                        address = vacancy['address']['raw']
                    elif vacancy['address'] is None:
                        salary_from = int(vacancy['salary']['from'])
                        salary_to = int(vacancy['salary']['to'])
                        address = 'Нет информации об адресе'
                    else:
                        try:
                            salary_from = int(vacancy['salary']['from'])
                        except TypeError:
                            salary_from = 0
                        try:
                            salary_to = int(vacancy['salary']['to'])
                        except TypeError:
                            salary_to = 0
                        address = vacancy['address']['raw']

                    cls(vacancy['name'], salary_from, salary_to, vacancy['url'], vacancy['snippet']['requirement'] +
                        '\n' + vacancy['snippet']['responsibility'], address)
