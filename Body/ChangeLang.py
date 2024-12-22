import tkinter as tk
import sys
import os

Project_Path = os.path.dirname(__file__)

def lang_var():
    return open(f"{Project_Path}\lang_var.txt", 'r', encoding='utf-8').read() 

def start_bot():
    if language_var.get() == "ru":
        sys.exit()

    elif language_var.get() == "en":
        sys.exit()

def create_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, 
                       bg="#6A5ACD", fg="white", borderwidth=0,
                       relief="flat", padx=20, pady=10, font=("Arial", 12),
                       width=19, height=1)  # Задаем фиксированный размер
    return button

def change_language():
    if language_var.get() == "ru":
        start_button.config(text="Сохранить свой выбор")
        root.title("Выбор языка BER")
        radio_ru.config(bg="#5B009E", fg="white")
        radio_en.config(bg="#380061", fg="white")
        open(f"{Project_Path}\lang_var.txt", 'w', encoding='utf-8').write("ru")
        
    elif language_var.get() == "en":
        start_button.config(text="Save your choice")
        root.title("Language select BER")
        radio_en.config(bg="#5B009E", fg="white")
        radio_ru.config(bg="#380061", fg="white")
        open(f"{Project_Path}\lang_var.txt", 'w', encoding='utf-8').write("en")

    else:
        tk.messagebox.showerror("Choose language", "Not a single language has been selected.")


# Создание основного окна
root = tk.Tk()
root.title("Выбор языка BER")
root.geometry("300x150")  # Размер окна
root.resizable(False, False)  # Запрет изменения размера окна
root.configure(bg="#4B0082")

# Переменная для хранения выбранного языка
language_var = tk.StringVar(value=lang_var())  # Устанавливаем русский как язык по умолчанию

# Кнопка запуска
start_button = create_button(root, text="", command=start_bot)
start_button.pack(pady=20)

# Фрейм для радиокнопок с обводкой
language_frame = tk.Frame(root, bg="#4B0082", bd=2, relief="sunken")  # Устанавливаем обводку
language_frame.pack(pady=10, padx=10)  # Добавляем отступы

# Радиокнопки для выбора языка
radio_ru = tk.Radiobutton(language_frame, padx=10, text="Русский", variable=language_var, value="ru",
                           command=change_language, bg="#4B0082", font=("Arial", 12), fg="white", selectcolor="#380061",
                             activebackground="#4B0082", activeforeground="white")
radio_en = tk.Radiobutton(language_frame, padx=10, text="English", variable=language_var, value="en",
                           command=change_language, bg="#4B0082", font=("Arial", 12), fg="white", selectcolor="#380061",
                             activebackground="#4B0082", activeforeground="white")

radio_ru.pack(side=tk.LEFT)
radio_en.pack(side=tk.LEFT)
change_language()

# Запуск основного цикла приложения
root.mainloop()
