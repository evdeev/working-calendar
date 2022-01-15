# Производственный календарь

Можно использовать собрынные json файлы из **data**.
Последний календарь обновляется ежедневно по расписанию с сайта consultant.ru


Парсинг производственных календарей с сайта consultant.ru после **2010 года**.

**Формат:**

```json
{
// ... some data ...
  '2022-02-21': 'workday',
  '2022-02-22': 'preholiday',
  '2022-02-23': 'holiday weekend',
  '2022-02-24': 'workday',
// ... some data ...
}
```

**Статусы:**

- workday (рабочий)
- preholiday (предпраздничный, сокращенный)
- weekend (выходной)
- nowork (нерабочий)


**Пример использования**

```Python
from workingcal import get_working_calendar, save_working_calendar

data = get_working_calendar(input_year=2022)
save_working_calendar(data=data, path='data')
```

**В командной строке**

```bash
# Календарь текущего года
> python3 main.py
```

```bash
# Календарь 2015 и 2022 года
> python3 main.py --years 2015 2022
```

```bash
# Календари за период с 2010 по 2022 год
> python3 main.py --range 2010 2022
```

```bash
# Дополнительно: можно указать папку для скачивания.
# По умолчанию всегда создается папка "data"
> python3 main.py --range 2010 2022 --path your_folder
```

