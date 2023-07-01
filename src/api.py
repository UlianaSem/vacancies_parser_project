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
