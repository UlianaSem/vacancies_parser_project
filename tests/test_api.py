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

    assert get_super_job_api_object.get_vacancies('ggggggggggg') == []
    assert get_head_hunter_api_object.get_vacancies('ggggggggggg') == []
