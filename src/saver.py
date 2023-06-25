from abc import ABC, abstractmethod
import src.vacancy
import pandas as pd
import json


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
    def remove_vacancy(self):
        """
        Абстрактный метод для удаления вакансии из файла
        """
        pass

    @abstractmethod
    def get_vacancy(self, *args, **kwargs):
        """
        Абстрактный метод для получения вакансий из файла
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
        vacancies = self.to_json()

        with open(self.PATH_TO_FILE, 'w', encoding='utf-8') as file:
            file.write(vacancies)

    def remove_vacancy(self):
        pass

    def get_vacancy(self, *args, **kwargs):
        pass

    @staticmethod
    def to_json():
        """
        Возвращает экземпляры класса Vacancy в формате списка с JSON
        :return: список с JSON
        """
        vacancies = src.vacancy.Vacancy.all
        vacancies_in_json = []

        for vacancy in vacancies:
            if isinstance(vacancy, src.vacancy.Vacancy):
                vacancies_in_json.append({
                    "profession": vacancy.profession,
                    "salary": vacancy.salary,
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
        vacancies = src.vacancy.Vacancy.all

        csv_data = pd.DataFrame(src.vacancy.Vacancy.all,
                                columns=['page.number in order', 'name', 'url', 'price', 'address', 'date'])
        csv_data.to_csv(self.PATH_TO_FILE)

    def remove_vacancy(self):
        pass

    def get_vacancy(self, *args, **kwargs):
        pass
