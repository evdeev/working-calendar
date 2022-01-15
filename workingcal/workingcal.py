from calendar import different_locale, month_abbr
from bs4 import BeautifulSoup
from datetime import date
import requests
import json


this_year = date.today().year
data_years = range(2010, this_year+1)


def input_validation_year(entered_year: int | str) -> int:
    if int(entered_year) in data_years:
        return entered_year
    raise ValueError(f'Missing data for {entered_year}')


def get_month_number(month_name: str, locale="ru_RU") -> int:
    with different_locale(locale):
        month_names = tuple(x.lower() for x in month_abbr)
        return month_names.index(month_name.lower()[:3])

month_number_dict = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12
}


def get_working_calendar(input_year: int | str) -> dict:
    input_validation_year(input_year)
    result_data = {}
    url = f'https://www.consultant.ru/law/ref/calendar/proizvodstvennye/{input_year}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    raw_calendar_year = soup.find_all('table', class_='cal')

    for month in raw_calendar_year:
        month_name = month.find('th', class_='month').text.lower()
        month_num = month_number_dict[month_name]
        month_days = [day for day in month.find_all('td')]

        for day_td in month_days:
            if not ''.join(day_td['class']) == 'inactively':
                class_name = ' '.join(day_td['class'])
                day_num = int(''.join(day for day in day_td.text if day.isdigit()))
                result_data[str(date(int(input_year), month_num, day_num))] = 'workday' if not class_name else class_name

    return result_data


def save_working_calendar(data, path='data'):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(json.dumps(data, ensure_ascii=False))