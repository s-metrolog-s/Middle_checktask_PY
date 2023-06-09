import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import filedialog
from datetime import *

from modules import dbase
from modules import id_functions as idf
from modules import logger as log

def click_save():
    result_str = {"name": ent_name_input.get(),
                  "body": txt_body_input.get("1.0", tk.END),
                  "date": ent_date_out.get(),
                  "time": get_time()
                  }
    if none_empty_fields():
        dbase.add_item(ent_id_out.get(), result_str)
        click_clear_fields()
        refesh_head()

def click_find():
    if ent_find.get() != "":
        id_find = ent_find.get()
        result = dbase.find_string(id_find)
        if result != {}:
            click_clear_fields()
            ent_id_out.insert("0", id_find)
            ent_name_input.insert("0", result.get("name"))
            txt_body_input.replace("1.0", tk.END, result.get("body"))
            ent_date_out.insert("0", result.get("date"))
            ent_time_out.insert("0", result.get("time"))
        else:
            showinfo(title="Результат поиска", message="Запись не найдена")
    else:
        showinfo(title="Результат поиска", message="Введите ID для поиска")

def click_del():
    dbase.del_row(ent_id_out.get())
    click_clear_fields()
    refesh_head()

def click_clear_fields():
    ent_id_out.delete('0', tk.END)
    ent_name_input.delete('0', tk.END)
    txt_body_input.delete('1.0', tk.END)
    ent_date_out.delete('0', tk.END)
    ent_time_out.delete('0', tk.END)
    ent_find.delete("0", tk.END)
    ent_name_input.focus()

def click_clear():
    txt_body_input.delete("1.0", tk.END)
    txt_body_input.focus()

def dismiss(window):
    window.grab_release()
    window.destroy()

def click_show_all():
    window_finder = tk.Toplevel()
    window_finder.title("Список всех заметок в базе данных")
    window_finder.geometry("400x400")
    window_finder.resizable(False, False)
    window_finder.protocol("WM_DELETE_WINDOW", lambda: dismiss(window_finder))
    result = tk.Text(master=window_finder, width=100, height=20)
    result.pack()
    result.replace("1.0", tk.END, dbase.make_list(ent_find_all.get()))
    close_button = tk.Button(window_finder, text="Закрыть окно", command=lambda: dismiss(window_finder))
    close_button.pack(anchor="s", expand=1)
    window_finder.grab_set()

def click_open_file():
    open_file = tk.filedialog
    ent_data.delete(0, tk.END)
    new_path = open_file.askopenfilename()
    ent_data.insert(0, new_path)
    idf.config.FILEPATH = new_path
    idf.id_generator()
    idf.refresh_id()
    refesh_head()
    log.save_log(f"Открыта новая база данных, путь: {new_path}")
def none_empty_fields():
    if ent_name_input.get() == "" or txt_body_input.get("1.0", tk.END) == "\n":
        showinfo(title="Найдены пустые поля", message="Заполните поля Заголовок и Текст")
        return False
    else:
        return True

def get_date():
    return datetime.now().strftime("%d-%m-%Y")

def get_time():
    return datetime.now().strftime("%H:%M")

def refesh_head():
    idf.id_generator()
    ent_id_out.delete(0, tk.END)
    ent_id_out.insert(0, idf.get_new_id())
    ent_date_out.delete(0, tk.END)
    ent_date_out.insert(0, get_date())
    ent_time_out.delete(0, tk.END)
    ent_time_out.insert(0, get_time())


#-----------Общие настойки программы и окна-------------#

window = tk.Tk()
window.title('Заметки v0.1b')
window.geometry("500x600")
window.resizable(False, False)

# Проверка нумерации заметок и возврат последнего индекса
idf.id_generator()
idf.refresh_id()
idf.id_generator()

#-----------Форма общая-------------#
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=1)
frm_form.pack(expand=True,
              fill=tk.X,
              padx=1,
              pady=1)

# Внесение ID
lbl_id = tk.Label(master=frm_form, text='ID', font=('Calibri', 16))
lbl_id.columnconfigure(index=0, weight=1)
lbl_id.rowconfigure(index=0, weight=1)
lbl_id.grid(row=0, column=0)

ent_id_out = tk.Entry(master=frm_form, font=('Calibri', 12), justify=tk.CENTER)
ent_id_out.grid(row=1, column=0)

# Дата
lbl_date = tk.Label(master=frm_form, text='Дата', font=('Calibri', 16))
lbl_date.columnconfigure(index=1, weight=1)
lbl_date.rowconfigure(index=1, weight=1)
lbl_date.grid(row=0, column=1)

ent_date_out = tk.Entry(master=frm_form, font=('Calibri', 12), justify=tk.CENTER)
ent_date_out.grid(row=1, column=1)

# Время
lbl_time = tk.Label(master=frm_form, text='Время', font=('Calibri', 16))
lbl_time.columnconfigure(index=2, weight=1)
lbl_time.rowconfigure(index=2, weight=1)
lbl_time.grid(row=0, column=2)

ent_time_out = tk.Entry(master=frm_form, font=('Calibri', 12), justify=tk.CENTER)
ent_time_out.grid(row=1, column=2)

#--------------------------------------------------#


#-----------Форма для названия заметки-------------#
frm_form_name = tk.Frame(relief=tk.SUNKEN, borderwidth=1)
frm_form_name.pack(expand=True,
                   fill=tk.X,
                   padx=1,
                   pady=1)

#-----------Внесение заголовка-------------#
lbl_name = tk.Label(master=frm_form_name, text='Заголовок', font=('Calibri', 16))
ent_name_input = tk.Entry(master=frm_form_name)
lbl_name.grid(row=0, column=0)
ent_name_input.grid(row=1, column=0)
ent_name_input.configure(width=85)
#----------------------------------------------#


#-----------Форма для тела заметки-------------#
frm_form_body = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
frm_form_body.pack(expand=True,
                   fill='x',
                   padx=3,
                   pady=3)

# Тело заметки
lbl_body = tk.Label(master=frm_form_body, text='Текст заметки', font=('Calibri', 16))
txt_body_input = tk.Text(master=frm_form_body, width=59, height=12)
lbl_body.grid(row=0, column=0)
txt_body_input.grid(row=1, column=0, ipadx=5, ipady=5)

btn_clear = tk.Button(master=frm_form_body, text='Очистить текст', command=click_clear)
btn_clear.grid(row=2, column=0, padx=5, pady=5, sticky='w')

#----------------------------------------------#


#---------------Рамка для кнопок---------------#
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_save = tk.Button(master=frm_buttons, text='Сохранить заметку', command=click_save)
btn_save.grid(ipadx=10, ipady=10, padx=5, pady=5, row=0, column=0)

btn_del = tk.Button(master=frm_buttons, text='Удалить заметку', command=click_del)
btn_del.grid(ipadx=10, ipady=10, padx=5, pady=5, row=0, column=1)

#----------------------------------------------#

# Рамка модуля поиска
frm_find = tk.Frame(relief=tk.GROOVE, borderwidth=1)
frm_find.pack(fill=tk.X, ipadx=5, ipady=5)

lbl_text_in = tk.Label(master=frm_find, text='Поиск заметки по ID:', font=('Calibri', 12))
lbl_text_in.grid(row=0, column=0, sticky='w')

ent_find = tk.Entry(master=frm_find, width=30)
ent_find.grid(row=0, column=1)

btn_find = tk.Button(master=frm_find, text='Поиск', command=click_find, height=1, width=20)
btn_find.grid(row=0, column=2)

lbl_text_in_all = tk.Label(master=frm_find, text='Поиск заметок по дате:', font=('Calibri', 12))
lbl_text_in_all.grid(row=1, column=0, sticky='w')

ent_find_all = tk.Entry(master=frm_find, width=30)
ent_find_all.insert(0, get_date())
ent_find_all.grid(row=1, column=1)

btn_find_date = tk.Button(master=frm_find, text='Поиск по дате', command=click_show_all, height=1, width=20)
btn_find_date.grid(row=1, column=2)

# Рамка сохранения
frm_data = tk.Frame()
frm_data.pack(fill=tk.X)

lbl_data_adress = tk.Label(master=frm_data, text='Путь к файлу: ', font=('Colibri', 10))
lbl_data_adress.grid(row=0, column=0, sticky='e')

ent_data = tk.Entry(master=frm_data, width=40)
ent_data.insert(0, idf.config.FILEPATH)
ent_data.grid(row=0, column=1)

btn_open_file = tk.Button(master=frm_data, text='Открыть файл', command=click_open_file, height=1, width=22)
btn_open_file.grid(row=0, column=2)

refesh_head()
window.mainloop()
