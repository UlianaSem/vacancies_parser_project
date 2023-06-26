import json
import re
from abc import ABC, abstractmethod

import pandas as pd

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


class JSONSaver(Saver):
    """
    Класс для работы с файлами JSON
    """

    PATH_TO_FILE = '../src/vacancies.json'

    def add_vacancy(self):
        """
        Сохраняет вакансии в файл JSON
        """
        vacancies = self.get_json__()

        with open(self.PATH_TO_FILE, 'w', encoding='utf-8') as file:
            file.write(vacancies)

    def remove_vacancy(self, vacancy):
        pass

    def get_vacancy_by_salary(self, salary):
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

        vacancies = self.open_file__()

        for vacancy in vacancies:
            if vacancy['salary_from'] >= salary_for_check[0]:
                vacancies_for_response.append(vacancy)

        return vacancies_for_response

    def get_vacancy_by_address(self, address):
        """
        Ищет вакансии по адресу и возвращает список с вакансиями
        :param address: адрес для поиска
        :return: список с вакансиями
        """
        address = set(address.strip().lower().split(', '))
        vacancies_for_response = []

        vacancies = self.open_file__()

        for vacancy in vacancies:
            address_for_check = set(vacancy['work_address'].lower().split(', '))
            if address.issubset(address_for_check):
                vacancies_for_response.append(vacancy)

        return vacancies_for_response

    def open_file__(self):
        """
        Открывает и возвращает файл с вакансиями
        :return: список словарей м вакансиями
        """
        with open(self.PATH_TO_FILE, 'r', encoding='utf-8') as file:
            vacancies = file.read()

        return json.loads(vacancies)

    @staticmethod
    def get_json__():
        """
        Возвращает экземпляры класса Vacancy в формате JSON
        :return: JSON
        """
        vacancies = src.vacancy.Vacancy.all
        vacancies_in_json = []

        for vacancy in vacancies:
            if isinstance(vacancy, src.vacancy.Vacancy):
                vacancies_in_json.append({
                    "profession": vacancy.profession,
                    "salary_from": vacancy.salary_from,
                    "salary_to": vacancy.salary_to,
                    "vacancy_url": vacancy.vacancy_url,
                    "vacancy_requirement": vacancy.vacancy_requirement,
                    "work_address": vacancy.work_address
                })

        return json.dumps(vacancies_in_json)


class CSVSaver(Saver):
    """
    Класс для работы с файлами CSV
    """

    PATH_TO_FILE = '../src/vacancies.csv'

    def add_vacancy(self):
        """
        Сохраняет вакансии в файл CSV
        """
        vacancies = self.get_list__()

        csv_data = pd.DataFrame(vacancies, columns=['profession', 'salary_from', 'salary_to', 'vacancy_url',
                                                    'vacancy_requirement', 'work_address'])

        csv_data.to_csv(self.PATH_TO_FILE)

    def remove_vacancy(self, vacancy):
        pass

    def get_vacancy_by_salary(self, salary):
        pass

    def get_vacancy_by_address(self, address):
        """
        Абстрактный метод для получения вакансий из файла по адресу
        """
        pass

    @staticmethod
    def get_list__():
        """
        Возвращает экземпляры класса Vacancy в формате списка
        :return: список
        """
        vacancies = src.vacancy.Vacancy.all
        vacancies_in_list = []

        for vacancy in vacancies:
            if isinstance(vacancy, src.vacancy.Vacancy):
                vacancies_in_list.append([
                    vacancy.profession,
                    vacancy.salary_from,
                    vacancy.salary_to,
                    vacancy.vacancy_url,
                    vacancy.vacancy_requirement,
                    vacancy.work_address
                ])

        return vacancies_in_list
