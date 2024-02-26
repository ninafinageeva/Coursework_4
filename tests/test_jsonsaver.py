import json


def test_file_writer(self):
    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(self, file, indent=4, ensure_ascii=False)
    assert file == {
        "vacancy_title": "Ведущий програмист-разработчик Unity, C#",
        "town": "Москва",
        "salary_from": 120000,
        "salary_to": 250000,
        "employment": "Полная занятость",
        "url": "https://hh.ru/vacancy/93159478"
    }