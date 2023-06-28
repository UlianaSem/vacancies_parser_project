import csv
import json
import re
from abc import ABC, abstractmethod

import src.vacancy


class Saver(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    @abstractmethod
    def add_vacancy(self):
        """
        Абстрактный метод для добавления вакансий в файл
        """
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy):
        """
        Абстрактный метод для удаления вакансии из файла
        """
        pass

    @abstractmethod
    def get_vacancy_by_salary(self, salary):
        """
        Абстрактный метод для получения вакансий из файла по зарплате
        """
        pass

    @abstractmethod
    def get_vacancy_by_address(self, address):
        """
        Абстрактный метод для получения вакансий из файла по адресу
        """
        pass

    @classmethod
    def get_data__(cls):
        """
        Возвращает экземпляры класса Vacancy в формате списка словарей
        :return: список словарей
        """
        vacancies = src.vacancy.Vacancy.all
        vacancies_ = []

        for vacancy in vacancies:
            if isinstance(vacancy, src.vacancy.Vacancy):
                vacancies_.append({
                    "profession": vacancy.profession,
                    "salary_from": vacancy.salary_from,
                    "salary_to": vacancy.salary_to,
                    "vacancy_url": vacancy.vacancy_url,
                    "vacancy_requirement": vacancy.vacancy_requirement,
                    "work_address": vacancy.work_address
                })

        return vacancies_


class VacancyRemover:
    """
    Класс для удаления вакансии из файлов
    """

    @staticmethod
    def remove_vacancy(saver, vacancy_for_remove: src.vacancy.Vacancy):
        """
        Удаляет заданную вакансию из файла
        :param saver: экземпляр класса JSONSaver или CSVSaver
        :param vacancy_for_remove: объект класса Vacancy для удаления
        """
        flag = False
        vacancies = saver.open_file__()

        for vacancy in vacancies:
            if vacancy_for_remove.vacancy_url == vacancy['vacancy_url']:
                vacancies.remove(vacancy)
                flag = True
                break

        return flag, vacancies


class VacancyFilter:
    """
    Класс для получения отфильтрованных вакансий
    """

    @staticmethod
    def get_vacancy_by_address(saver, address):
        """
        Ищет вакансии по адресу и возвращает список с вакансиями
        :param saver: экземпляр класса JSONSaver или CSVSaver
        :param address: адрес для поиска
        :return: список с вакансиями
        """
        address = set(re.split(r', | ', address.strip().lower()))
        vacancies_for_response = []

        vacancies = saver.open_file__()

        for vacancy in vacancies:
            address_for_check = set(re.split(r', | ', vacancy['work_address'].lower()))
            if address.issubset(address_for_check):
                vacancies_for_response.append(vacancy)

        return vacancies_for_response

    @staticmethod
    def get_vacancy_by_salary(saver, salary):
        """
        Ищет вакансии по зарплате и возвращает список с вакансиями
        :param saver: экземпляр класса JSONSaver или CSVSaver
        :param salary: зарплата для поиска
        :return: список с вакансиями
        """
        salary_for_check = []
        vacancies_for_response = []

        for salary_ in re.split(r"[/ -]", salary):
            if salary_.isdigit():
                salary_for_check.append(int(salary_))

        vacancies = saver.open_file__()

        for vacancy in vacancies:
            if int(vacancy['salary_from']) >= salary_for_check[0] or int(vacancy['salary_to']) >= salary_for_check[0]:
                vacancies_for_response.append(vacancy)

        return vacancies_for_response


class JSONSaver(Saver):
    """
    Класс для работы с файлами JSON
    """

    PATH_TO_FILE = '../src/vacancies.json'

    def add_vacancy(self):
        """
        Сохраняет вакансии в файл JSON
        """
        vacancies = self.get_data__()

        self.write_to_file(vacancies)

    def remove_vacancy(self, vacancy_for_remove: src.vacancy.Vacancy):
        """
        Удаляет заданную вакансию из файла
        :param vacancy_for_remove: объект класса Vacancy для удаления
        """
        remover = VacancyRemover()
        flag, vacancies = remover.remove_vacancy(self, vacancy_for_remove)

        if flag:
            vacancies = json.dumps(vacancies)
            self.write_to_file(vacancies)

    def get_vacancy_by_salary(self, salary):
        """
        Ищет вакансии по зарплате и возвращает список с вакансиями
        :param salary: зарплата для поиска
        :return: список с вакансиями
        """
        filter_ = VacancyFilter()

        return filter_.get_vacancy_by_salary(self, salary)

    def get_vacancy_by_address(self, address):
        """
        Ищет вакансии по адресу и возвращает список с вакансиями
        :param address: адрес для поиска
        :return: список с вакансиями
        """
        filter_ = VacancyFilter()

        return filter_.get_vacancy_by_address(self, address)

    def open_file__(self):
        """
        Открывает и возвращает файл с вакансиями
        :return: список словарей м вакансиями
        """
        with open(self.PATH_TO_FILE, 'r', encoding='utf-8') as file:
            vacancies = file.read()

        return json.loads(vacancies)

    def write_to_file(self, vacancies):
        """
        Записывает информацию о вакансиях в файл
        """
        with open(self.PATH_TO_FILE, 'w', encoding='utf-8') as file:
            file.write(vacancies)

    @classmethod
    def get_data__(cls):
        """
        Возвращает экземпляры класса Vacancy в формате JSON
        :return: JSON
        """
        vacancies = super().get_data__()

        return json.dumps(vacancies)


class CSVSaver(Saver):
    """
    Класс для работы с файлами CSV
    """

    PATH_TO_FILE = '../src/vacancies.csv'

    def add_vacancy(self):
        """
        Сохраняет вакансии в файл CSV
        """
        vacancies = self.get_data__()

        self.write_to_file(vacancies)

    def remove_vacancy(self, vacancy_for_remove: src.vacancy.Vacancy):
        """
        Удаляет заданную вакансию из файла
        :param vacancy_for_remove: объект класса Vacancy для удаления
        """
        remover = VacancyRemover()
        flag, vacancies = remover.remove_vacancy(self, vacancy_for_remove)

        if flag:
            self.write_to_file(vacancies)

    def get_vacancy_by_salary(self, salary):
        """
        Ищет вакансии по зарплате и возвращает список с вакансиями
        :param salary: зарплата для поиска
        :return: список с вакансиями
        """
        filter_ = VacancyFilter()

        return filter_.get_vacancy_by_salary(self, salary)

    def get_vacancy_by_address(self, address):
        """
        Ищет вакансии по адресу и возвращает список с вакансиями
        :param address: адрес для поиска
        :return: список с вакансиями
        """
        filter_ = VacancyFilter()

        return filter_.get_vacancy_by_address(self, address)

    def open_file__(self):
        """
        Открывает и возвращает файл с вакансиями
        :return: список словарей м вакансиями
        """
        vacancies = []

        with open(self.PATH_TO_FILE, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for line in reader:
                vacancies.append(line)

        return vacancies

    def write_to_file(self, vacancies):
        """
        Записывает информацию о вакансиях в файл
        """
        with open(self.PATH_TO_FILE, 'w', encoding='utf-8') as file:
            field_names = ['profession', 'salary_from', 'salary_to', 'vacancy_url', 'vacancy_requirement',
                           'work_address']
            writer = csv.DictWriter(file, fieldnames=field_names)

            writer.writeheader()
            writer.writerows(vacancies)
