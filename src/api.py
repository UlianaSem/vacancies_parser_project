from abc import ABC, abstractmethod


class API(ABC):
    """
    Абстрактный класс для работы с API сайтов
    """
    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_jobs(self):
        pass


class SuperJobAPI(API):
    def connect_to_api(self):
        pass

    def get_jobs(self):
        pass


class HeadHunterAPI(API):
    def connect_to_api(self):
        pass

    def get_jobs(self):
        pass
