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
    log.save_log(f"Запрошен поиск {id}")
    return result


# Удаление записи из базы данных
def del_row(id):
    my_dict = json_adapter.open_json()
    my_dict.pop(id)
    json_adapter.save_json(my_dict)
    log.save_log(f"Удалена заметка {id}")