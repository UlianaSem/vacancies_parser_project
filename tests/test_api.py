import pytest

import src.api


@pytest.fixture
def get_super_job_api_object():
    return src.api.SuperJobAPI()


@pytest.fixture
def get_head_hunter_api_object():
    return src.api.HeadHunterAPI()


def test_get_vacancies(get_super_job_api_object, get_head_hunter_api_object):
    assert get_head_hunter_api_object.URL == 'https://api.hh.ru/vacancies'
    assert get_super_job_api_object.URL == 'https://api.superjob.ru/2.0/vacancies/'

    assert get_super_job_api_object.get_vacancies('ggggggggggg') == {'more': False,
                                                                     'objects': [],
                                                                     'subscription_active': False,
                                                                     'subscription_id': 0,
                                                                     'total': 0}
    assert get_head_hunter_api_object.get_vacancies('ggggggggggg') == {'alternate_url': 'https://hh.ru/search/vacancy'
                                                                                        '?enable_snippets=true&search'
                                                                                        '_field=name&text=ggggggggggg',
                                                                       'arguments': None,
                                                                       'clusters': None,
                                                                       'found': 0,
                                                                       'items': [],
                                                                       'page': 0,
                                                                       'pages': 1,
                                                                       'per_page': 20}
