from src.jsonsaver import JSONSaver
from src.api_hh import HeadHunterAPI
from src.jsonsaver import JSONSaver


def user_choice_hh():
    keyword = input('Напишите название профессии: \n')
    api_hh = HeadHunterAPI()
    print('Сколько вывести страниц? \n')
    pages = int(input())
    from_hh = api_hh.get_vacancies(keyword, pages)
    print('Список вакансий с сайта "HeadHunter": \n')
    for i in from_hh:
        print(i)
    print('Записать, отсортированные по зарплате данные в JSON файл? \n')
    user_answer = input('Да\Нет \n').lower()
    if user_answer not in ['да']:
        print('Спасибо за использование программы')
    else:
        jsonfile_hh = JSONSaver()
        jsonfile_hh.add_vacancies(from_hh)
        jsonfile_hh.sort_vacancies_by_salary()
        jsonfile_hh.file_writer()
        return jsonfile_hh
