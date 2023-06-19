import modules.json_adapter as json_adapter
from modules import config


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
def refresh_id():
    my_dict = json_adapter.open_json()

    min_id = 2147483647
    for item in my_dict:
        if int(item) < min_id:
            min_id = int(item)

    for i in range(0, config.LASTINDEX + 1):
        if str(i) not in my_dict:
            for key in range(i+1, config.LASTINDEX + 1):
                if str(key) in my_dict:
                    my_dict[str(i)] = my_dict.pop(str(key))

    json_adapter.save_json(my_dict)
