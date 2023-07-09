# 📌Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# 📌Преобразуйте его в дату в текущем году.
# 📌Логируйте ошибки, если текст не соответсвует формату.


import logging
from datetime import datetime, timedelta, date


FORMAT = "{levelname} - {asctime}: {msg}"
logging.basicConfig(
    format=FORMAT,
    filename="log.log",
    encoding='utf-8',
    style='{',
    level=logging.ERROR
)

logger = logging.getLogger(__name__)

WEEKS = {"понедельник": 0,
         "вторник": 1,
         "среда": 2,
         "четверг": 3,
         "пятница": 4,
         "суббота": 5,
         "воскресенье": 6}

MONTHS = {"января": 1,
          "февраля": 2,
          "марта": 3,
          "апреля": 4,
          "мая": 5,
          "июня": 6,
          "июля": 7,
          "августа": 8,
          "сентября": 9,
          "октября": 10,
          "ноября": 11,
          "декабря": 12}


def parse_date(income_date):
    try:
        current_year = datetime.now().year
        start_date = date(year=current_year, month=1, day=1)
        data_set = income_date.split(" ")
        weeks_ = int(data_set[0].split("-")[0])
        days = WEEKS[data_set[1]]
        months_ = MONTHS[data_set[2]]
        delta = timedelta(weeks=weeks_, days=days, month=months_)
        date_ = start_date + delta
        return date_
    except (ValueError, KeyError) as e:
        logger.error(f"Failed to parse date: {income_date}. Error: {str(e)}")
        return None


if __name__ == '__main__':
    texts = ["1-й четверг ноября", "3-я среда мая", "29-й понедельник июня"]
    for text in texts:
        parsed_date = parse_date(text)
        if parsed_date:
            print(f"Text: {text}, Parsed Date: {parsed_date}")
        else:
            print(f"Text: {text}, Failed to parse date")
