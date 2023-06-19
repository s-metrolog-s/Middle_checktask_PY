import json
from modules import config


def open_json() -> dict:
    my_dict = {}
    with open(f'{config.FILEPATH}', 'r', encoding="utf_8") as file:
        try:
            my_dict = json.loads(file.read())
        except:
            print("Файл пустой")
        file.close()
    return my_dict


def save_json(my_dict: dict):
    with open(f'{config.FILEPATH}', 'w', encoding="utf_8") as file:
        json.dump(my_dict, file)
        file.close()
