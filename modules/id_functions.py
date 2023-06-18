import modules.json_adapter as json_adapter
from modules import config
#from encodings import utf_8


# Генерация нового ID по последней записи в базе данных
def id_generator():
    my_dict = json_adapter.open_json()
    max_index = 0
    for key in my_dict:
        if int(key) > max_index:
            max_index = int(key)
    config.LASTINDEX = max_index


def get_new_id():
    config.LASTINDEX += 1
    return config.LASTINDEX

# Нумерация всех записей в базе данных по порядку
# TODO написать логику переназначения всех ID
# def refresh_id(file_path)
