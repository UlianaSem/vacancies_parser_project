import os
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

        params = {
            "keyword": profession
        }

        vacancies = requests.get(self.URL, headers=self.HEADERS, params=params)

        return vacancies.json()


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

        params = {
            "text": profession,
            "search_field": 'name'
        }

        vacancies = requests.get(self.URL, params=params)

        return vacancies.json()
