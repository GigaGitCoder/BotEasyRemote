import tkinter as tk
import webbrowser
import pystray
from PIL import Image, ImageTk
from pystray import MenuItem, Icon
import threading
import os
import time
from colorama import Fore
import subprocess

process = None

# Информация автора
username = "GigaGitCoder"
repository = "BotEasyRemote"
donateun = "ava_channel_live"

# Путь к файлу бота
bot_main = "bot.py" # Если основной файл бота с другим названием, то замените на него

# Глобальная переменная для иконки
tray_icon = None

# Флаги состояния бота
bot_running = False

# Функции для кнопок
def start_bot():
    global bot_running
    global process
    bot_running = True
    print(Fore.CYAN +   "\n========start=======" + Fore.RESET)
    process = subprocess.Popen(['python', f'{bot_main}'])
    print(Fore.GREEN + "     Бот запущен!" + Fore.RESET) 
    print(Fore.CYAN + "====================\n" + Fore.RESET)  
    update_button_states()

def restart_bot():
    global process
    print(Fore.CYAN +   "\n======restart=======" + Fore.RESET)
    print(Fore.YELLOW + "Бот перезапускается!" + Fore.RESET) 
    process.terminate()
    time.sleep(5)
    process = subprocess.Popen(['python', f'{bot_main}'])
    print(Fore.GREEN + "  Бот запустился!") 
    print(Fore.CYAN + "====================\n" + Fore.RESET) 
    
def stop_bot():
    global bot_running
    global process
    bot_running = False
    print(Fore.CYAN + "\n========exit========" + Fore.RESET)
    print(Fore.YELLOW + "Бот останавливается!" + Fore.RESET) 
    process.terminate()
    time.sleep(5)
    print(Fore.RED + "   Бот остановлен!") 
    print(Fore.CYAN + "====================\n" + Fore.RESET) 
    update_button_states()

def open_author_github():
    webbrowser.open(f"https://github.com/{username}") 

def open_repository_github():
    webbrowser.open(f"https://github.com/{username}/{repository}")  

def open_cat_link(event):
    webbrowser.open(f"https://donationalerts.com/r/{donateun}")

def minimize_app():
    root.withdraw()  # Скрыть главное окно

def restore_app(icon, item):
    root.after(0, lambda: root.deiconify())  # Показать главное окно

def exit_app(icon, item):
    global process
    if process is not None:
        process.terminate()
        print(Fore.RED + f"\n\nФайл бота {bot_main} будет закрыт принудительно из-за выхода из приложения!\n" + Fore.RESET)
        time.sleep(2)
    icon.stop()  # Остановить иконку в трее
    time.sleep(2)
    root.destroy()  # Закрыть приложение

def exit_app_from_button():
    global process
    if process is not None:
        process.terminate()
        print(Fore.RED + f"\n\nФайл бота {bot_main} будет закрыт принудительно из-за выхода из приложения!\n" + Fore.RESET)
        time.sleep(2)
    if tray_icon:
        tray_icon.stop()  # Остановить иконку в трее
    root.quit()  # Закрыть приложение

# Обновление состояния кнопок
def update_button_states():
    if bot_running:
        btn_start.config(state=tk.DISABLED)
        btn_restart.config(state=tk.NORMAL)
        btn_stop.config(state=tk.NORMAL)
    else:
        btn_start.config(state=tk.NORMAL)
        btn_restart.config(state=tk.DISABLED)
        btn_stop.config(state=tk.DISABLED)

# Создание иконки для системного трея
def create_tray_icon():
    global tray_icon
    # Загрузка иконки из файла
    icon_path = os.path.join(os.path.dirname(__file__), 'BER_Content\icon.png')  
    image = Image.open(icon_path)
    tray_icon = Icon("test_icon", image, "Bot Easy Remote", menu=pystray.Menu(
        MenuItem("Развернуть", restore_app),
        MenuItem("Выход", exit_app)
    ))
    tray_icon.run()

# Обработка закрытия окна
def on_closing():
    minimize_app()  # Скрыть окно вместо закрытия

# Создание основного окна
root = tk.Tk()
root.title("Bot Easy Remote")
root.geometry("650x300")  # Установка размера окна
root.resizable(False, False)  # Запрет изменения размера окна
root.configure(bg="#4B0082")  # Темно-фиолетовый фон

# Установка иконки для окна
icon_path = os.path.join(os.path.dirname(__file__), 'BER_Content\icon.png')  # Путь к иконке
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

# Функция для создания кнопок с фиксированным размером
def create_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, 
                       bg="#6A5ACD", fg="white", borderwidth=0,
                       relief="flat", padx=20, pady=10, font=("Arial", 12),
                       width=12, height=1)  # Задаем фиксированный размер
    return button

# Загрузка Logo
logo_image_path = os.path.join(os.path.dirname(__file__), 'BER_Content\BER_Logo.png')  # Убедитесь, что имя файла совпадает
logo_image = Image.open(logo_image_path)
logo_photo = ImageTk.PhotoImage(logo_image)
cat_label = tk.Label(root, image=logo_photo, bg="#4B0082")
cat_label.pack(pady=0)

# Создание кнопок в первом ряду
frame1 = tk.Frame(root, bg="#4B0082")
frame1.pack(pady=20)

btn_start = create_button(frame1, "Запустить бота", start_bot)
btn_start.grid(row=0, column=0, padx=10)

btn_restart = create_button(frame1, "Перезапустить бота", restart_bot)
btn_restart.grid(row=0, column=1, padx=10)
btn_restart.config(state=tk.DISABLED)  # Изначально неактивна

btn_stop = create_button(frame1, "Остановить бота", stop_bot)
btn_stop.grid(row=0, column=2, padx=10)
btn_stop.config(state =tk.DISABLED)  # Изначально неактивна

# Загрузка изображения котика
cat_image_path = os.path.join(os.path.dirname(__file__), 'BER_Content\cat.png')  # Убедитесь, что имя файла совпадает
cat_image = Image.open(cat_image_path)
cat_image = cat_image.resize((50, 50), Image.LANCZOS)  # Изменение размера изображения
cat_photo = ImageTk.PhotoImage(cat_image)

# Добавление изображения котика в правый нижний угол
cat_label = tk.Label(root, image=cat_photo, bg="#4B0082")
cat_label.place(relx=1.0, rely=1.0, anchor='se')  # Правый нижний угол

# Добавление действия к котику
cat_label.bind("<Button-1>", open_cat_link)

# Создание кнопок во втором ряду
frame2 = tk.Frame(root, bg="#4B0082")
frame2.pack(pady=20)

btn_author = create_button(frame2, "Автор на GitHub", open_author_github)
btn_author.grid(row=0, column=0, padx=10)

btn_repo = create_button(frame2, "Репозиторий GitHub", open_repository_github)
btn_repo.grid(row=0, column=1, padx=10)

btn_minimize = create_button(frame2, "Выход", exit_app_from_button)
btn_minimize.grid(row=0, column=2, padx=10)

# Привязка события закрытия окна к функции on_closing
root.protocol("WM_DELETE_WINDOW", on_closing)

# Запуск иконки в системном трее в отдельном потоке
threading.Thread(target=create_tray_icon, daemon=True).start()

# Запуск основного цикла приложения
root.mainloop()
