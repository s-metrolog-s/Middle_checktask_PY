from datetime import *
from modules import config


# Сохранение действий пользователя
def save_log(data):
    with open(f'{config.DIRPATH}\data\log.csv', 'a', encoding="utf_8") as file:
        result = f'{data};{datetime.now().strftime("%D:%H:%M:%S")}\n'
        print(result)
        file.write(result)
