import tkinter as tk
from tkinter.messagebox import showinfo
from datetime import *

from modules import dbase
from modules import id_functions as idf

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
    close_button = tk.Button(window_finder, text="Закрыть окно", command=lambda: dismiss(window_finder))
    close_button.pack(anchor="s", expand=1)
    window_finder.grab_set()

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
    ent_id_out.insert(0, idf.get_new_id())
    ent_date_out.insert(0, get_date())
    ent_time_out.insert(0, get_time())


#-----------Общие настойки программы и окна-------------#

window = tk.Tk()
window.title('Заметки v0.1b')
window.geometry("500x600")
window.resizable(False, False)
# Копируем имя пути к папке программы
idf.id_generator()

#-----------Форма общая-------------#
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=1)
frm_form.pack(expand=True,
              fill='x',
              padx=3,
              pady=3)

# Внесение ID
lbl_id = tk.Label(master=frm_form, text='ID', font=('Calibri', 16))
lbl_id.columnconfigure(index=0, weight=1)
lbl_id.rowconfigure(index=0, weight=1)
lbl_id.grid(row=0, column=0)

ent_id_out = tk.Entry(master=frm_form, font=('Calibri', 12))
ent_id_out.grid(row=1, column=0)

# Дата
lbl_date = tk.Label(master=frm_form, text='Дата', font=('Calibri', 16))
lbl_date.columnconfigure(index=1, weight=1)
lbl_date.rowconfigure(index=1, weight=1)
lbl_date.grid(row=0, column=1)

ent_date_out = tk.Entry(master=frm_form, font=('Calibri', 12))
ent_date_out.grid(row=1, column=1)

# Время
lbl_time = tk.Label(master=frm_form, text='Время', font=('Calibri', 16))
lbl_time.columnconfigure(index=2, weight=1)
lbl_time.rowconfigure(index=2, weight=1)
lbl_time.grid(row=0, column=2)

ent_time_out = tk.Entry(master=frm_form, font=('Calibri', 12))
ent_time_out.grid(row=1, column=2)

#--------------------------------------------------#


#-----------Форма для названия заметки-------------#
frm_form_name = tk.Frame(relief=tk.SUNKEN, borderwidth=1)
frm_form_name.pack(expand=True,
                   fill='x',
                   padx=3,
                   pady=3)

#-----------Внесение заголовка-------------#
lbl_name = tk.Label(master=frm_form_name, text='Заголовок', font=('Calibri', 16))
ent_name_input = tk.Entry(master=frm_form_name)
lbl_name.grid(row=0, column=0)
ent_name_input.grid(row=1, column=0)
ent_name_input.configure(width=70)
#----------------------------------------------#


#-----------Форма для тела заметки-------------#
frm_form_body = tk.Frame(relief=tk.SUNKEN, borderwidth=2)
frm_form_body.pack(expand=True,
                   fill='x',
                   padx=3,
                   pady=3)

# Тело заметки
lbl_body = tk.Label(master=frm_form_body, text='Текст заметки', font=('Calibri', 16))
txt_body_input = tk.Text(master=frm_form_body, width=50, height=10)
lbl_body.grid(row=0, column=0)
txt_body_input.grid(row=1, column=0, ipadx=5, ipady=5, sticky='nswe')

btn_clear = tk.Button(master=frm_form_body, text='Очистить текст', command=click_clear)
btn_clear.grid(row=2, column=0, padx=5, pady=5, sticky='w')

#----------------------------------------------#


#---------------Рамка для кнопок---------------#
frm_buttons = tk.Frame()
frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

btn_save = tk.Button(master=frm_buttons, text='Сохранить заметку', command=click_save)
btn_save.pack(side=tk.LEFT, padx=10, ipadx=10)

btn_save = tk.Button(master=frm_buttons, text='Вывести все', command=click_show_all)
btn_save.pack(side=tk.LEFT, padx=10, ipadx=10)

btn_save = tk.Button(master=frm_buttons, text='Удалить заметку', command=click_del)
btn_save.pack(side=tk.LEFT, padx=10, ipadx=10)

#----------------------------------------------#

# Рамка модуля поиска
frm_find = tk.Frame(relief=tk.GROOVE, borderwidth=1)
frm_find.pack(fill=tk.X, ipadx=5, ipady=5)

lbl_text_in = tk.Label(master=frm_find, text='Введите ключение слова или ID для поиска:', font=('Calibri', 12))
lbl_text_in.grid(row=0, column=0, sticky='e')

ent_find = tk.Entry(master=frm_find, width=30)
ent_find.grid(row=1, column=0)

btn_find = tk.Button(master=frm_find, text='Поиск', command=click_find, height=3, width=20)
btn_find.grid(row=0, column=1, columnspan=3, rowspan=3, pady=3, padx=3)

# Рамка сохранения
frm_data = tk.Frame()
frm_data.pack(fill=tk.X)

lbl_data_adress = tk.Label(master=frm_data, text='Путь к файлу: ', font=('Colibri', 12))
lbl_data_adress.grid(row=0, column=0, sticky='w')

ent_data = tk.Entry(master=frm_data, width=40)
ent_data.grid(row=0, column=1)

refesh_head()
window.mainloop()
