import pytest

import src.api


@pytest.fixture
def get_super_job_api_object():
    return src.api.SuperJobAPI()


@pytest.fixture
def get_head_hunter_api_object():
    return src.api.HeadHunterAPI()


def test_get_vacancies(get_super_job_api_object, get_head_hunter_api_object):
    """
    Проверяет правильность url
    :param get_super_job_api_object: объект класса SuperJobAPI
    :param get_head_hunter_api_object: объект класса HeadHunterAPI
    """
    assert get_head_hunter_api_object.URL == 'https://api.hh.ru/vacancies'
    assert get_super_job_api_object.URL == 'https://api.superjob.ru/2.0/vacancies/'


def test_formate_data(get_super_job_api_object, get_head_hunter_api_object):
    """
    Проверяет правильность форматирования данных о вакансиях
    :param get_super_job_api_object: объект класса SuperJobAPI
    :param get_head_hunter_api_object: объект класса HeadHunterAPI
    """
    assert get_super_job_api_object.formate_data([{'canEdit': False, 'is_closed': False, 'id': 44933587,
                                                   'id_client': 2974144, 'payment_from': 40065, 'payment_to': 0,
                                                   'date_pub_to': 1689849303, 'date_archived': 1670832602,
                                                   'date_published': 1687257303,
                                                   'address': 'Москва, Николоямская улица, 33с1',
                                                   'profession': 'Программист 1C', 'work': None, 'compensation': None,
                                                   'candidat': 'Обязанности: Создание программного комплекса под '
                                                               'требования работодателя (1С Колледж)\nТребования: \n- '
                                                               'высшее профессиональное (техническое или '
                                                               'инженерно-экономическое) образование без предъявления '
                                                               'требований к стажу работы или среднее '
                                                               'профессиональное (техническое или '
                                                               'инженерно-экономическое) образование и стаж работы в '
                                                               'должности не менее 3 лет\n- Знание: 1С 8.3, '
                                                               'умение читать "чужой код". Приветствуется знания: '
                                                               'Python, Java Script, Html, CSS\n- Сертификат о '
                                                               'вакцинации Covid\nУсловия:\n• Оформление по ТК РФ\n• '
                                                               'З/П от 40 065 (оклад) + KPI\n• График работы 5/2\n• '
                                                               'Отпуск 28 календарных дней\n• Интересные '
                                                               'задачи\nРабота в Правительстве Москвы — это '
                                                               'возможность делать наш город современнее и удобнее. '
                                                               'Если ты тоже неравнодушен к Москве, хочешь развивать '
                                                               'ее и развиваться сам, присоединяйся к нашей команде! '
                                                               'Твой город – твое дело!',
                                                   'metro': [], 'currency': 'rub',
                                                   'vacancyRichText': '<p>Обязанности: Создание программного '
                                                                      'комплекса под требования работодателя (1С '
                                                                      'Колледж)</p><p>Требования: </p><p>- высшее '
                                                                      'профессиональное (техническое или '
                                                                      'инженерно-экономическое) образование без '
                                                                      'предъявления требований к стажу работы или '
                                                                      'среднее профессиональное (техническое или '
                                                                      'инженерно-экономическое) образование и стаж '
                                                                      'работы в должности не менее 3 лет</p><p>- '
                                                                      'Знание: 1С 8.3, умение читать "чужой код". '
                                                                      'Приветствуется знания: Python, Java Script, '
                                                                      'Html, CSS</p><p>- Сертификат о вакцинации '
                                                                      'Covid</p><p>Условия:</p><ul><li>Оформление по '
                                                                      'ТК РФ</li><li>З/П от 40 065 (оклад) + '
                                                                      'KPI</li><li>График работы 5/2</li><li>Отпуск '
                                                                      '28 календарных дней</li><li>Интересные '
                                                                      'задачи</li></ul><p>Работа в Правительстве '
                                                                      'Москвы — это возможность делать наш город '
                                                                      'современнее и удобнее. Если ты тоже '
                                                                      'неравнодушен к Москве, хочешь развивать ее и '
                                                                      'развиваться сам, присоединяйся к нашей '
                                                                      'команде! Твой город – твое дело!</p>',
                                                   'covid_vaccination_requirement': {'id': 2,
                                                                                     'title': 'Требуется сертификат'},
                                                   'moveable': False, 'agreement': False, 'anonymous': False,
                                                   'is_archive': False, 'is_storage': False,
                                                   'type_of_work': {'id': 6, 'title': 'Полный рабочий день'},
                                                   'place_of_work': {'id': 0, 'title': 'Не имеет значения'},
                                                   'education': {'id': 2, 'title': 'Высшее'},
                                                   'experience': {'id': 3, 'title': 'От 3 лет'},
                                                   'maritalstatus': {'id': 0, 'title': 'Не имеет значения'},
                                                   'children': {'id': 0, 'title': 'Не имеет значения'},
                                                   'client': {'id': 2974144, 'title': 'Медицинский колледж № 7',
                                                              'link': 'https://www.superjob.ru/clients/medicinskij'
                                                                      '-kolledzh-7-2974144/vacancies.html',
                                                              'industry': [], 'description': 'Медицинский колледж № 7',
                                                              'vacancy_count': 0, 'staff_count': '100 — 500',
                                                              'client_logo': 'https://public.superjob.ru/images'
                                                                             '/clients_logos.ru'
                                                                             '/2974144_08eba726918269720294f40a0d5d3e'
                                                                             '34.png',
                                                              'address': 'Москва, ул. Николоямская, д.33 ',
                                                              'addresses': [
                                                                  {'addressString': 'Москва, ул. Николоямская, д.33 ',
                                                                   'latitude': 55.747475, 'longitude': 37.658473,
                                                                   'phones': [{'number': 74959157169,
                                                                               'additionalNumber': None}]}],
                                                              'url': 'http://medcollege7.ru', 'short_reg': False,
                                                              'is_blocked': False, 'registered_date': 1479384750,
                                                              'town': {'id': 4, 'title': 'Москва',
                                                                       'declension': 'в Москве', 'hasMetro': True,
                                                                       'genitive': 'Москвы'}}, 'languages': [],
                                                   'driving_licence': [], 'catalogues': [
            {'id': 33, 'title': 'IT, Интернет, связь, телеком', 'key': 33,
             'positions': [{'id': 36, 'title': 'Web-верстка', 'key': 36},
                           {'id': 42, 'title': 'Интернет, создание и поддержка сайтов', 'key': 42},
                           {'id': 48, 'title': 'Разработка, программирование', 'key': 48},
                           {'id': 53, 'title': 'Системы управления предприятием (ERP)', 'key': 53},
                           {'id': 57, 'title': 'Техническая поддержка', 'key': 57}]}],
                                                   'agency': {'id': 1, 'title': 'прямой работодатель'},
                                                   'town': {'id': 4, 'title': 'Москва', 'declension': 'в Москве',
                                                            'hasMetro': True, 'genitive': 'Москвы'},
                                                   'already_sent_on_vacancy': False, 'rejected': False,
                                                   'response_info': [], 'phone': None, 'phones': None, 'fax': None,
                                                   'faxes': None,
                                                   'client_logo': 'https://public.superjob.ru/images/clients_logos.ru'
                                                                  '/2974144_08eba726918269720294f40a0d5d3e34.png',
                                                   'highlight': False, 'age_from': 0, 'age_to': 0,
                                                   'gender': {'id': 0, 'title': 'Не имеет значения'},
                                                   'firm_name': 'ГБПОУ Департамента Здравоохранения Города Москвы '
                                                                'Медицинский Колледж № 7',
                                                   'firm_activity': 'Медицинский колледж 7',
                                                   'link': 'https://www.superjob.ru/vakansii/programmist-1c-44933587'
                                                           '.html',
                                                   'latitude': 55.747475, 'longitude': 37.658482}]) == [{
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
        'url': 'https://www.superjob.ru/vakansii/programmist-1c-44933587.html'}]
    assert get_head_hunter_api_object.formate_data([{'id': '82128820', 'premium': False,
                                                     'name': 'Junior Python разработчик', 'department': None,
                                                     'has_test': False, 'response_letter_required': False,
                                                     'area': {'id': '2', 'name': 'Санкт-Петербург',
                                                              'url': 'https://api.hh.ru/areas/2'},
                                                     'salary': {'from': 60000, 'to': None, 'currency': 'RUR',
                                                                'gross': True},
                                                     'type': {'id': 'open', 'name': 'Открытая'},
                                                     'address': {'city': 'Санкт-Петербург',
                                                                 'street': 'набережная Обводного Канала',
                                                                 'building': '93а', 'lat': 59.916451, 'lng': 30.338676,
                                                                 'description': None,
                                                                 'raw': 'Санкт-Петербург, набережная Обводного Канал'
                                                                        'а, 93а',
                                                                 'metro': None, 'metro_stations': [], 'id': '445179'},
                                                     'response_url': None, 'sort_point_distance': None,
                                                     'published_at': '2023-06-19T15:03:24+0300',
                                                     'created_at': '2023-06-19T15:03:24+0300', 'archived': False,
                                                     'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response'
                                                                            '?vacancyId=82128820',
                                                     'insider_interview': None,
                                                     'url': 'https://api.hh.ru/vacancies/82128820?host=hh.ru',
                                                     'adv_response_url': None,
                                                     'alternate_url': 'https://hh.ru/vacancy/82128820', 'relations': [],
                                                     'employer': {'id': '1684993', 'name': 'Виста',
                                                                  'url': 'https://api.hh.ru/employers/1684993',
                                                                  'alternate_url': 'https://hh.ru/employer/1684993',
                                                                  'logo_urls': None,
                                                                  'vacancies_url': 'https://api.hh.ru/vacancies'
                                                                                   '?employer_id=1684993',
                                                                  'accredited_it_employer': False, 'trusted': True},
                                                     'snippet': {
                                                         'requirement': 'Комплекс Программных Средств "Виста-Мед". * '
                                                                        'Опыт коммерческой разработки от 1 года. * '
                                                                        'Владение '
                                                                        '<highlighttext>Python</highlighttext> 2/3. * '
                                                                        'Владение (My)SQL, конкретно: * * Иметь...',
                                                         'responsibility': 'Написание и поддержка интеграций ('
                                                                           '<highlighttext>python</highlighttext>2/3 '
                                                                           '+ REST/SOAP + MySQL). * Разработка новых '
                                                                           'продуктов ('
                                                                           '<highlighttext>python</highlighttext>3 + '
                                                                           'Flask/Django...'},
                                                     'contacts': None, 'schedule': None, 'working_days': [],
                                                     'working_time_intervals': [], 'working_time_modes': [],
                                                     'accept_temporary': False, 'professional_roles': [
            {'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
                                                     'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
                                                     'employment': {'id': 'full', 'name': 'Полная занятость'}}]) == [
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


def test_validate_profession():
    """
    Проверяет правильность валидирования данных о профессии
    """
    hh_validator = src.api.HeadHunterVacancyDataValidator()
    sj_validator = src.api.SuperJobVacancyDataValidator()

    assert hh_validator.validate_profession(None) == 'Должность не указана'
    assert sj_validator.validate_profession(None) == 'Должность не указана'
    assert hh_validator.validate_profession('Test') == 'Test'
    assert sj_validator.validate_profession('Test') == 'Test'


def test_validate_salary():
    """
    Проверяет правильность валидирования данных о зарплате
    """
    hh_validator = src.api.HeadHunterVacancyDataValidator()
    sj_validator = src.api.SuperJobVacancyDataValidator()

    assert hh_validator.validate_salary(None) == (0, 0)
    assert sj_validator.validate_salary(None, 'rub') == 0
    assert sj_validator.validate_salary('1000', 'rub') == 1000
    assert hh_validator.validate_salary({'from': None, 'to': 1000}) == (0, 1000)
    assert hh_validator.validate_salary({'from': 800, 'to': 1000}) == (800, 1000)


def test_validate_address():
    """
    Проверяет правильность валидирования данных об адресе
    """
    hh_validator = src.api.HeadHunterVacancyDataValidator()
    sj_validator = src.api.SuperJobVacancyDataValidator()

    assert hh_validator.validate_address(None) == 'Нет информации об адресе'
    assert sj_validator.validate_address(None) == 'Нет информации об адресе'
    assert hh_validator.validate_address({'city': 'Санкт-Петербург', 'street': 'набережная Обводного Канала',
                                          'building': '93а', 'lat': 59.916451, 'lng': 30.338676, 'description': None,
                                          'raw': 'Санкт-Петербург, набережная Обводного Канала, 93а', 'metro': None,
                                          'metro_stations': [],
                                          'id': '445179'}) == 'Санкт-Петербург, набережная Обводного Канала, 93а'
    assert hh_validator.validate_address({'city': 'Санкт-Петербург', 'street': 'набережная Обводного Канала',
                                          'building': '93а', 'lat': 59.916451, 'lng': 30.338676, 'description': None,
                                          'raw': None, 'metro': None, 'metro_stations': [],
                                          'id': '445179'}) == 'Санкт-Петербург, набережная Обводного Канала, 93а'
    assert sj_validator.validate_address(
        'Санкт-Петербург, набережная Обводного Канала, 93а') == 'Санкт-Петербург, набережная Обводного Канала, 93а'


def test_validate_url():
    """
    Проверяет правильность валидирования данных о url
    """
    hh_validator = src.api.HeadHunterVacancyDataValidator()
    sj_validator = src.api.SuperJobVacancyDataValidator()

    assert hh_validator.validate_url(None) == 'url не указан'
    assert sj_validator.validate_url(None) == 'url не указан'
    assert hh_validator.validate_url('Test') == 'Test'
    assert sj_validator.validate_url('Test') == 'Test'


def test_validate_vacancy_requirement():
    """
    Проверяет правильность валидирования данных о требованиях к вакансии
    """
    hh_validator = src.api.HeadHunterVacancyDataValidator()
    sj_validator = src.api.SuperJobVacancyDataValidator()

    assert hh_validator.validate_vacancy_requirement(None) == 'Требования к вакансии не указаны'
    assert sj_validator.validate_vacancy_requirement(None) == 'Требования к вакансии не указаны'
    assert hh_validator.validate_vacancy_requirement({'requirement': 'Test', 'responsibility': 'Test'}) == 'Test Test'
    assert hh_validator.validate_vacancy_requirement({'requirement': 'Test', 'responsibility': None}) == 'Test '
    assert sj_validator.validate_vacancy_requirement('Test') == 'Test'
