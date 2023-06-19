# Запись и чтение из базы данных

from modules import json_adapter as json_adapter
from modules import logger as log


# Добавление новой записи в базу данных
def add_item(id, data):
    my_dict = json_adapter.open_json()
    my_dict[id] = data
    json_adapter.save_json(my_dict)
    log.save_log(f"Добавлена заметка {id}")


# Поиск записи в базе данных
def find_string(data_find: str) -> str:
    my_dict = json_adapter.open_json()
    result = {}
    for key in my_dict:
        if key == data_find:
            result = my_dict.get(key)
    log.save_log(f"Запрошен поиск {data_find}")
    return result


# Удаление записи из базы данных
def del_row(id):
    my_dict = json_adapter.open_json()
    my_dict.pop(id)
    json_adapter.save_json(my_dict)
    log.save_log(f"Удалена заметка {id}")

def make_list(date):
    my_dict = json_adapter.open_json()
    result = ""
    for item in my_dict:
        if (my_dict[item].get("date") == date) or (date == ""):
            result += f"{item}: {my_dict[item].get('name')} from {my_dict[item].get('date')} last edit {my_dict[item].get('time')}\n"
    log.save_log(f"Вывод всех замето за {date}")
    return result