import pytest

import src.saver
import src.vacancy


@pytest.fixture
def get_saver_for_test():
    return src.saver.JSONSaver(), src.saver.CSVSaver()


def test_get_data__(get_saver_for_test):
    vacancy = src.vacancy.Vacancy('Developer', 100000, 110000, 'www.test.ru', 'Some requirements', 'Some address')

    json, csv = get_saver_for_test

    assert json.get_data__() == '[{"profession": "Developer", "salary_from": 100000, "salary_to": 110000, ' \
                                '"vacancy_url": "www.test.ru", "vacancy_requirement": "Some requirements", ' \
                                '"work_address": "Some address"}]'
    assert csv.get_data__() == [{'profession': 'Developer', 'salary_from': 100000, 'salary_to': 110000,
                                 'vacancy_requirement': 'Some requirements', 'vacancy_url': 'www.test.ru',
                                 'work_address': 'Some address'}]
