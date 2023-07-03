import pytest

import src.vacancy


@pytest.fixture
def get_vacancy_for_test():
    return src.vacancy.Vacancy('Developer', 100000, 110000, 'www.test.ru', 'Some requirements', 'Some address')


def test_init(get_vacancy_for_test):
    """
    Проверяет правильность инициализации
    """
    assert get_vacancy_for_test.salary_from == 100000
    assert get_vacancy_for_test.salary_to == 110000
    assert get_vacancy_for_test.profession == 'Developer'
    assert get_vacancy_for_test.vacancy_url == 'www.test.ru'
    assert get_vacancy_for_test.vacancy_requirement == 'Some requirements'
    assert get_vacancy_for_test.work_address == 'Some address'


def test_compressions(get_vacancy_for_test):
    """
    Проверяет правильность сравнений объектов класса
    :param get_vacancy_for_test: объект класса Vacancy
    """
    other_vacancy = src.vacancy.Vacancy('Engineer', 60000, 60000, 'www.test.ru', 'Some requirements', 'Some address')

    assert (get_vacancy_for_test > other_vacancy) is True
    assert (get_vacancy_for_test < other_vacancy) is False
    assert (get_vacancy_for_test == other_vacancy) is False
    assert (get_vacancy_for_test >= other_vacancy) is True
    assert (get_vacancy_for_test <= other_vacancy) is False


def test_add_to_class():
    """
    Проверяет корректность добавления экземпляров класса
    """
    src.vacancy.Vacancy.add_to_class([
        {'address': 'Санкт-Петербург, набережная Обводного Канала, 93а',
         'profession': 'Junior Python разработчик',
         'requirements': 'Комплекс Программных Средств "Виста-Мед". * Опыт '
                         'коммерческой разработки от 1 года. * Владение '
                         '<highlighttext>Python</highlighttext> 2/3. * Владение '
                         '(My)SQL, конкретно: * * Иметь... Написание и поддержка '
                         'интеграций (<highlighttext>python</highlighttext>2/3 + '
                         'REST/SOAP + MySQL). * Разработка новых продуктов '
                         '(<highlighttext>python</highlighttext>3 + Flask/Django...',
         'salary_from': 60000,
         'salary_to': 0,
         'url': 'https://api.hh.ru/vacancies/82128820?host=hh.ru'}]
    )

    first_vacancy = src.vacancy.Vacancy.all[-1]

    assert first_vacancy.profession == 'Junior Python разработчик'
    assert first_vacancy.salary_from == 60000
    assert first_vacancy.salary_to == 0
    assert first_vacancy.vacancy_url == 'https://api.hh.ru/vacancies/82128820?host=hh.ru'
    assert first_vacancy.work_address == 'Санкт-Петербург, набережная Обводного Канала, 93а'

    src.vacancy.Vacancy.add_to_class([{
        'address': 'Москва, Николоямская улица, 33с1',
        'profession': 'Программист 1C',
        'requirements': 'Обязанности: Создание программного комплекса под требования '
                        'работодателя (1С Колледж)\n'
                        'Требования: \n'
                        '- высшее профессиональное (техническое или '
                        'инженерно-экономическое) образование без предъявления '
                        'требований к стажу работы или среднее профессиональное '
                        '(техническое или инженерно-экономическое) образование и '
                        'стаж работы в должности не менее 3 лет\n'
                        '- Знание: 1С 8.3, умение читать "чужой код". Приветствуется '
                        'знания: Python, Java Script, Html, CSS\n'
                        '- Сертификат о вакцинации Covid\n'
                        'Условия:\n'
                        '• Оформление по ТК РФ\n'
                        '• З/П от 40 065 (оклад) + KPI\n'
                        '• График работы 5/2\n'
                        '• Отпуск 28 календарных дней\n'
                        '• Интересные задачи\n'
                        'Работа в Правительстве Москвы — это возможность делать наш '
                        'город современнее и удобнее. Если ты тоже неравнодушен к '
                        'Москве, хочешь развивать ее и развиваться сам, '
                        'присоединяйся к нашей команде! Твой город – твое дело!',
        'salary_from': 40065,
        'salary_to': 0,
        'url': 'https://www.superjob.ru/vakansii/programmist-1c-44933587.html'}])

    second_vacancy = src.vacancy.Vacancy.all[-1]

    assert second_vacancy.profession == 'Программист 1C'
    assert second_vacancy.salary_from == 40065
    assert second_vacancy.salary_to == 0
    assert second_vacancy.vacancy_url == 'https://www.superjob.ru/vakansii/programmist-1c-44933587.html'
    assert second_vacancy.work_address == 'Москва, Николоямская улица, 33с1'


def test_build_response(get_vacancy_for_test):
    """
    Проверяет правильность построения ответа для пользователя
    """
    builder = src.vacancy.VacancyBuilder()

    assert builder.build_response(get_vacancy_for_test) == "Должность: Developer\nЗарплата: от 100000 до " \
                                                           "110000\nСсылка на вакансию: www.test.ru\nАдрес работы: " \
                                                           "Some address"


def test_get_vacancy_by_salary():
    """
    Проверяет правильность фильтра по зарплате
    """
    filter_ = src.vacancy.VacancyFilter()

    with pytest.raises(Exception):
        filter_.get_vacancy_by_salary(src.vacancy.Vacancy.all, 'Тест')

    response = filter_.get_vacancy_by_salary(src.vacancy.Vacancy.all, '10000')
    builder = src.vacancy.VacancyBuilder()

    assert builder.build_response(response[0]) == 'Должность: Developer\nЗарплата: от 100000 до 110000\nСсылка на ' \
                                                  'вакансию: www.test.ru\nАдрес работы: Some address'


def test_get_vacancy_by_address():
    """
    Проверяет правильность фильтра по адресу
    """
    filter_ = src.vacancy.VacancyFilter()
    response = filter_.get_vacancy_by_address(src.vacancy.Vacancy.all, 'Москва, Николоямская')

    builder = src.vacancy.VacancyBuilder()

    assert builder.build_response(response[0]) == 'Должность: Программист 1C\nЗарплата: от 40065 до 0\nСсылка на ' \
                                                  'вакансию: https://www.superjob.ru/vakansii/programmist-1c-44933587' \
                                                  '.html\nАдрес работы: Москва, Николоямская улица, 33с1'
