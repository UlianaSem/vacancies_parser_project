import pytest

import src.vacancy


@pytest.fixture
def get_vacancy_for_test():
    return src.vacancy.Vacancy('Developer', 100000, 'www.test.ru', 'Some requirements', 'Some address')


def test_init(get_vacancy_for_test):
    assert get_vacancy_for_test.salary_from == 100000
    assert get_vacancy_for_test.profession == 'Developer'
    assert get_vacancy_for_test.vacancy_url == 'www.test.ru'
    assert get_vacancy_for_test.vacancy_requirement == 'Some requirements'
    assert get_vacancy_for_test.work_address == 'Some address'


def test_compressions(get_vacancy_for_test):
    other_vacancy = src.vacancy.Vacancy('Engineer', 60000, 'www.test.ru', 'Some requirements', 'Some address')

    assert (get_vacancy_for_test > other_vacancy) is True
    assert (get_vacancy_for_test < other_vacancy) is False
    assert (get_vacancy_for_test == other_vacancy) is False
    assert (get_vacancy_for_test >= other_vacancy) is True
    assert (get_vacancy_for_test <= other_vacancy) is False


def test_add_to_class():
    src.vacancy.Vacancy.add_to_class(
        {'items': [{'id': '82128820', 'premium': False, 'name': 'Junior Python разработчик',
                    'department': None, 'has_test': False, 'response_letter_required': False, 'area':
                        {'id': '2', 'name': 'Санкт-Петербург', 'url': 'https://api.hh.ru/areas/2'},
                    'salary': {'from': 60000, 'to': None, 'currency': 'RUR', 'gross': True}, 'type':
                        {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Санкт-Петербург',
                                                                        'street': 'набережная Обводного'
                                                                                  ' Канала',
                                                                        'building': '93а',
                                                                        'lat': 59.916451,
                                                                        'lng': 30.338676,
                                                                        'description': None,
                                                                        'raw': 'Санкт-Петербург, набер'
                                                                               'ежная Обводного Кана'
                                                                               'ла, 93а',
                                                                        'metro': None,
                                                                        'metro_stations': [],
                                                                        'id': '445179'},
                    'response_url': None, 'sort_point_distance': None, 'published_at': '2023-06-19T15:'
                                                                                       '03:24+0300',
                    'created_at': '2023-06-19T15:03:24+0300', 'archived': False,
                    'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=8212'
                                           '8820', 'insider_interview': None, 'url': 'https://api.hh.'
                                                                                     'ru/vacancies/821'
                                                                                     '28820?host=hh.ru',
                    'adv_response_url': None, 'alternate_url': 'https://hh.ru/vacancy/82128820',
                    'relations': [], 'employer': {'id': '1684993', 'name': 'Виста', 'url': 'https://api'
                                                                                           '.hh.ru/empl'
                                                                                           'oyers/16849'
                                                                                           '93',
                                                  'alternate_url': 'https://hh.ru/employer/1684993',
                                                  'logo_urls': None, 'vacancies_url': 'https://api.hh.'
                                                                                      'ru/vacancies?em'
                                                                                      'ployer_id=16849'
                                                                                      '93',
                                                  'accredited_it_employer': False, 'trusted': True},
                    'snippet': {'requirement': 'Комплекс Программных Средств "Виста-Мед". * Опыт комме'
                                               'рческой разработки от 1 года. * Владение <highlighttex'
                                               't>Python</highlighttext> 2/3. * Владение (My)SQL, конк'
                                               'ретно: * * Иметь...', 'responsibility': 'Написание и п'
                                                                                        'оддержка интег'
                                                                                        'раций (<highl'
                                                                                        'ighttext>pyth'
                                                                                        'on</highlightt'
                                                                                        'ext>2/3 + RES'
                                                                                        'T/SOAP + MyS'
                                                                                        'QL). * Разраб'
                                                                                        'отка новых про'
                                                                                        'дуктов (<high'
                                                                                        'lighttext>pyt'
                                                                                        'hon</highlight'
                                                                                        'text>3 + Flas'
                                                                                        'k/Django...'},
                    'contacts': None, 'schedule': None, 'working_days': [],
                    'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
                    'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                    'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3',
                                                                       'name': 'От 1 года до 3 лет'},
                    'employment': {'id': 'full', 'name': 'Полная занятость'}}], 'found': 1342,
         'pages': 68, 'per_page': 20, 'page': 0, 'clusters': None, 'arguments': None,
         'alternate_url': 'https://hh.ru/search/vacancy?enable_snippets=true&search_field=name&text=py'
                          'thon'})

    first_vacancy = src.vacancy.Vacancy.all[-1]

    assert first_vacancy.profession == 'Junior Python разработчик'
    assert first_vacancy.salary_from == 60000
    assert first_vacancy.vacancy_url == 'https://api.hh.ru/vacancies/82128820?host=hh.ru'
    assert first_vacancy.work_address == 'Санкт-Петербург, набережная Обводного Канала, 93а'

    src.vacancy.Vacancy.add_to_class({'objects': [{'canEdit': False, 'is_closed': False, 'id': 44933587,
                                                   'id_client': 2974144, 'payment_from': 40065, 'payment_to': 0,
                                                   'date_pub_to': 1689849303, 'date_archived': 1670832602,
                                                   'date_published': 1687257303, 'address': 'Москва, Николоямская улиц'
                                                                                            'а, 33с1',
                                                   'profession': 'Программист 1C', 'work': None, 'compensation': None,
                                                   'candidat': 'Обязанности: Создание программного комплекса под требо'
                                                               'вания работодателя (1С Колледж)\nТребования: \n- высше'
                                                               'е профессиональное (техническое или инженерно-экономич'
                                                               'еское) образование без предъявления требований к стажу'
                                                               ' работы или среднее профессиональное (техническое или '
                                                               'инженерно-экономическое) образование и стаж работы в д'
                                                               'олжности не менее 3 лет\n- Знание: 1С 8.3, умение чита'
                                                               'ть "чужой код". Приветствуется знания: Python, Java Sc'
                                                               'ript, Html, CSS\n- Сертификат о вакцинации Covid\nУсло'
                                                               'вия:\n• Оформление по ТК РФ\n• З/П от 40 065 (оклад) +'
                                                               ' KPI\n• График работы 5/2\n• Отпуск 28 календарных дне'
                                                               'й\n• Интересные задачи\nРабота в Правительстве Москвы'
                                                               ' — это возможность делать наш город современнее и удоб'
                                                               'нее. Если ты тоже неравнодушен к Москве, хочешь развив'
                                                               'ать ее и развиваться сам, присоединяйся к нашей коман'
                                                               'де! Твой город – твое дело!', 'metro': [],
                                                   'currency': 'rub', 'vacancyRichText': '<p>Обязанности: Создание прог'
                                                                                         'раммного комплекса под требо'
                                                                                         'вания работодателя (1С Колле'
                                                                                         'дж)</p><p>Требования: </p>'
                                                                                         '<p>- высшее профессиональное'
                                                                                         ' (техническое или инженерно'
                                                                                         '-экономическое) образование '
                                                                                         'без предъявления требований '
                                                                                         'к стажу работы или среднее п'
                                                                                         'рофессиональное (техническое'
                                                                                         ' или инженерно-экономическое'
                                                                                         ') образование и стаж работы '
                                                                                         'в должности не менее 3 лет<'
                                                                                         '/p><p>- Знание: 1С 8.3, умен'
                                                                                         'ие читать "чужой код". Привет'
                                                                                         'ствуется знания: Python, Jav'
                                                                                         'a Script, Html, CSS</p><p>'
                                                                                         '- Сертификат о вакцинации C'
                                                                                         'ovid</p><p>Условия:</p><ul><'
                                                                                         'li>Оформление по ТК РФ</li>'
                                                                                         '<li>З/П от 40 065 (оклад) + '
                                                                                         'KPI</li><li>График работы 5'
                                                                                         '/2</li><li>Отпуск 28 календа'
                                                                                         'рных дней</li><li>Интересные'
                                                                                         ' задачи</li></ul><p>Работа в'
                                                                                         ' Правительстве Москвы — это '
                                                                                         'возможность делать наш город '
                                                                                         'современнее и удобнее. Если '
                                                                                         'ты тоже неравнодушен к Москв'
                                                                                         'е, хочешь развивать ее и раз'
                                                                                         'виваться сам, присоединяйся '
                                                                                         'к нашей команде! Твой город '
                                                                                         '– твое дело!</p>',
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
                                                              'link': 'https://www.superjob.ru/clients/medicinskij-kol'
                                                                      'ledzh-7-2974144/vacancies.html', 'industry': [],
                                                              'description': 'Медицинский колледж № 7',
                                                              'vacancy_count': 0, 'staff_count': '100 — 500',
                                                              'client_logo': 'https://public.superjob.ru/images/clien'
                                                                             'ts_logos.ru/2974144_08eba726918269720294f'
                                                                             '40a0d5d3e34.png',
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
                                                   'client_logo': 'https://public.superjob.ru/images/clients_logos.r'
                                                                  'u/2974144_08eba726918269720294f40a0d5d3e34.png',
                                                   'highlight': False, 'age_from': 0, 'age_to': 0,
                                                   'gender': {'id': 0, 'title': 'Не имеет значения'},
                                                   'firm_name': 'ГБПОУ Департамента Здравоохранения Города Москвы Медиц'
                                                                'инский Колледж № 7',
                                                   'firm_activity': 'Медицинский колледж 7',
                                                   'link': 'https://www.superjob.ru/vakansii/programmist-1c-44933587.ht'
                                                           'ml',
                                                   'latitude': 55.747475, 'longitude': 37.658482}], 'total': 1816,
                                      'more': True, 'subscription_id': 0, 'subscription_active': False})

    second_vacancy = src.vacancy.Vacancy.all[-1]

    assert second_vacancy.profession == 'Программист 1C'
    assert second_vacancy.salary_from == 40065
    assert second_vacancy.vacancy_url == 'https://www.superjob.ru/vakansii/programmist-1c-44933587.html'
    assert second_vacancy.work_address == 'Москва, Николоямская улица, 33с1'
