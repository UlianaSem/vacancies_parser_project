import src.api
import src.saver
import src.vacancy


def main():
    """Задает основной алгоритм работы программы"""

    # Подключаем API
    superjob = src.api.SuperJobAPI()
    hh = src.api.HeadHunterAPI()

    # Запрашиваем название должности для поиска
    profession = input('Здравствуйте! Вас приветствует парсер вакансий. Пожалуйста, введите название должности, '
                       'которая Вас интересует\n').title()

    while True:

        # Получаем вакансии
        superjob_vacancies = superjob.get_vacancies(profession)
        hh_vacancies = hh.get_vacancies(profession)

        # Добавляем вакансии в класс Vacancy
        src.vacancy.Vacancy.add_to_class_from_superjob(superjob_vacancies)
        src.vacancy.Vacancy.add_to_class_from_headhunter(hh_vacancies)

        # Создаем объекты для работы с файлами
        csv_file = src.saver.CSVSaver()
        json_file = src.saver.JSONSaver()

        # Заполняем файл полученными вакансиями
        csv_file.add_vacancy()
        json_file.add_vacancy()

        # Запрашиваем адрес и зарплату для поиска
        work_address = input(
            'Пожалуйста, введите интересующий Вас город. Введите слово "везде", если хотите искать вакансии по всей '
            'стране\n').lower().strip()
        salary = input('Пожалуйста, введите интересующий Вас диапазон зарплаты\n').lower().strip()

        # Создаем объект для фильтрации вакансий
        vacancies_filter = src.vacancy.VacancyFilter()

        vacancies_for_filter = src.vacancy.Vacancy.all

        # Получаем вакансии по зарплате и адресу
        filtered_vacancies = vacancies_filter.get_vacancy_by_salary(vacancies_for_filter, salary)

        if work_address != 'везде':
            filtered_vacancies = vacancies_filter.get_vacancy_by_address(filtered_vacancies, work_address)

        # Находим количество полученных вакансий
        vacancies_quantity = len(filtered_vacancies)

        if vacancies_quantity == 0:
            profession = input(
                'Вакансии по Вашему запросу не найдены. Попробуйте изменить запрос. Какая профессия Вас интересует? '
                'Для выхода введите "выход"\n').title()

            src.vacancy.Vacancy.all.clear()

            if profession.lower().strip() == 'выход':
                return

        else:
            top = int(input(f'Количество найденных вакансий: {vacancies_quantity}. Сколько вывести на экран?\n'))

            if top > vacancies_quantity or top < 0:
                top = vacancies_quantity

            # Создаем объект для построения ответа
            builder = src.vacancy.VacancyBuilder()

            for index in range(top):
                print(builder.build_response(filtered_vacancies[index]))
                print('')

            return


if __name__ == '__main__':
    main()
