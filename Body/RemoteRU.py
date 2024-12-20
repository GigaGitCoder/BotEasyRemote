import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import webbrowser
import pystray
from PIL import Image, ImageTk
from pystray import MenuItem, Icon
import threading
import os
from colorama import Fore
import subprocess




process = None
Project_Path = os.path.dirname(__file__)

# Информация автора
username = "GigaGitCoder"
repository = "BotEasyRemote"
donateun = "ava_channel_live"

# Глобальная переменная для иконки
tray_icon = None

# Флаги состояния бота
bot_running = False




def refresh_code_repair():
    if checkbox_var.get() == True:
        checkbox.config(bg="#5B009E", fg="white")
        
    elif checkbox_var.get() == False:
        checkbox.config(bg="#380061", fg="white")

# Путь к файлу бота
def bot_main():
    return open(f"{Project_Path}\path.txt", 'r', encoding='utf-8').read() 

# Функция для выбора файла
def select_file():
    file_path = filedialog.askopenfilename(title="Выберите файл бота", filetypes=[("Python files", "*.py")])
    if file_path:
        entry_bot_path.delete(0, tk.END)  # Очищаем текущее значение
        entry_bot_path.insert(0, file_path)  # Вставляем выбранный путь

# Функция для передачи пути в другой файл
def send_path():
    bot_path = entry_bot_path.get()
    open(f"{Project_Path}\path.txt", 'w', encoding='utf-8').write(bot_path)  # Записываем путь в файл
    print(f"\n\nПуть к файлу бота теперь такой: {bot_path}\nПерезаписан в файл path.txt\n")
    # Здесь вы можете добавить код для передачи пути в другой файл

def start_bot():
    file_path = bot_main()  # Укажите путь к вашему файлу

    try:
        # Проверяем, существует ли файл
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        global bot_running
        global process
        bot_running = True


        if checkbox_var.get() == True:
            print("\n========start=======")

            # Открываем новый терминал и запускаем бота
            process = subprocess.Popen(['python', f'{file_path}'])        
            print("     Бот запущен!") 
            print("====================\n")  

        elif checkbox_var.get() == False:
            print(Fore.CYAN + "\n========start=======" + Fore.RESET)

            # Открываем новый терминал и запускаем бота
            process = subprocess.Popen(['python', f'{file_path}'])        
            print(Fore.GREEN + "     Бот запущен!" + Fore.RESET) 
            print(Fore.CYAN + "====================\n" + Fore.RESET)  
            
        update_button_states()

    except FileNotFoundError as e:
        print(e)
        tk.messagebox.showerror("Ошибка", str(e))
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении скрипта: {e}")
        tk.messagebox.showerror("Ошибка", f"Ошибка при выполнении скрипта: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        tk.messagebox.showerror("Ошибка", f"Произошла непредвиденная ошибка: {e}")

def restart_bot():
    global process


    if checkbox_var.get() == True:
        print("\n~~~~~~~restart~~~~~~~")
        print("Бот перезапускается!")  

        stop_bot()  # Останавливаем бота
        start_bot()  # Запускаем бота заново

        print("~~~~~~~~~~~~~~~~~~~~~\n")
        
    elif checkbox_var.get() == False:
        print(Fore.CYAN + "\n~~~~~~~restart~~~~~~~" + Fore.RESET)
        print(Fore.YELLOW + "Бот перезапускается!" + Fore.RESET + "\n")  

        stop_bot()  # Останавливаем бота
        start_bot()  # Запускаем бота заново

        print(Fore.CYAN + "\n~~~~~~~~~~~~~~~~~~~~~\n" + Fore.RESET)
    
def stop_bot():
    global bot_running
    global process
    bot_running = False


    if checkbox_var.get() == True:
        print("\n========exit========")
        print("Бот останавливается!") 
        
        if process is not None:
            process.terminate()  # Останавливаем процесс
            process.wait()  # Ожидаем завершения процесса
            process = None  # Обнуляем переменную процесса

        print("   Бот остановлен!") 
        print("====================\n") 

    elif checkbox_var.get() == False:
        print(Fore.CYAN + "\n========exit========" + Fore.RESET)
        print(Fore.YELLOW + "Бот останавливается!" + Fore.RESET) 
        
        if process is not None:
            process.terminate()  # Останавливаем процесс
            process.wait()  # Ожидаем завершения процесса
            process = None  # Обнуляем переменную процесса

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

def restore_app():
    root.after(0, lambda: root.deiconify())  # Показать главное окно

def exit_app():
    global process
    if process is not None:
        print(Fore.RED + f"\n\nФайл бота {bot_main()} будет закрыт принудительно из-за выхода из приложения!\n" + Fore.RESET)
        stop_bot()
    if tray_icon:
        tray_icon.stop()  # Остановить иконку в трее
    root.destroy()  # Закрыть приложение


# Обновление состояния кнопок
def update_button_states():
    if bot_running:
        btn_start.config(state=tk.DISABLED)
        btn_start.config(bg="#41377B")
        btn_restart.config(state=tk.NORMAL)
        btn_restart.config(bg="#6A5ACD")
        btn_stop.config(state=tk.NORMAL)
        btn_stop.config(bg="#6A5ACD")
        btn_select_file.config(state=tk.DISABLED)
        btn_select_file.config(bg="#A51D2D")
        btn_send_path.config(state=tk.DISABLED)
        btn_send_path.config(bg="#A51D2D")
    else:
        btn_start.config(state=tk.NORMAL)
        btn_start.config(bg="#6A5ACD")
        btn_restart.config(state=tk.DISABLED)
        btn_restart.config(bg="#41377B")
        btn_stop.config(state=tk.DISABLED)
        btn_stop.config(bg="#41377B")
        btn_select_file.config(state=tk.NORMAL)
        btn_select_file.config(bg="#E1233A")
        btn_send_path.config(state=tk.NORMAL)
        btn_send_path.config(bg="#E1233A")

# Создание иконки для системного трея
def create_tray_icon():
    global tray_icon
    # Загрузка иконки из файла
    icon_path = os.path.join(os.path.dirname (__file__), f'{Project_Path}\BER_Content\icon.png')  
    image = Image.open(icon_path)
    tray_icon = Icon("test_icon", image, "Bot Easy Remote", menu=pystray.Menu(
        MenuItem("Поддержать", open_cat_link),
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
root.geometry("650x540")  # Увеличение размера окна для блока логов
root.resizable(False, False)  # Запрет изменения размера окна
root.configure(bg="#4B0082")  # Темно-фиолетовый фон


# Установка иконки для окна
icon_path = os.path.join(os.path.dirname(__file__), f'{Project_Path}\BER_Content\icon.png')  # Путь к иконке
icon_image = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, icon_photo)

# Функция для создания кнопок с фиксированным размером
def create_button(parent, text, command):
    button = tk.Button(parent, text=text, command=command, 
                       bg="#6A5ACD", fg="white", borderwidth=0,
                       relief="flat", padx=20, pady=10, font=("Arial", 12),
                       width=12, height=1, activebackground="#7D6FD3",
                       activeforeground="white", disabledforeground="#A8A8A8")  # Задаем фиксированный размер
    return button




# Загрузка Logo
logo_image_path = os.path.join(os.path.dirname(__file__), f'{Project_Path}\BER_Content\BER_Logo.png')  # Убедитесь, что имя файла совпадает
logo_image = Image.open(logo_image_path)
logo_photo = ImageTk.PhotoImage(logo_image)
cat_label = tk.Label(root, image=logo_photo, bg="#4B0082")
cat_label.pack(pady=0)


# Создание кнопок в первом ряду
frame1 = tk.Frame(root, bg="#4B0082")
frame1.pack(pady=20)

btn_start = create_button(frame1, "Запустить бота", start_bot)
btn_start.grid(row=0, column=0, padx=10)

checkbox_var = tk.BooleanVar()
checkbox = tk.Checkbutton(frame1, text="CodeFix (cmd)", variable=checkbox_var, 
                          command=refresh_code_repair, bg="#380061", font=("Arial", 12), 
                          fg="white", selectcolor="#380061", activebackground="#4B0082", 
                          activeforeground="white", relief="sunken")
checkbox.grid(row=1, column=0, pady=(10, 0))

btn_restart = create_button(frame1, "Перезапустить бота", restart_bot)
btn_restart.grid(row=0, column=1, padx=10)
btn_restart.config(state=tk.DISABLED, bg="#41377B")  # Изначально неактивна

btn_stop = create_button(frame1, "Остановить бота", stop_bot)
btn_stop.grid(row=0, column=2, padx=10)
btn_stop.config(state=tk.DISABLED, bg="#41377B")  # Изначально неактивна


# Создание текстового поля для ввода пути к файлу
entry_bot_path = tk.Entry(root, width=50, font=("Arial", 12))
entry_bot_path.pack(padx=10, pady=(20,10))
entry_bot_path.insert(0, bot_main())

frame2 = tk.Frame(root, bg="#4B0082")
frame2.pack(pady=(0,60))

# Кнопка для выбора файла
btn_select_file = tk.Button(frame2, text="Выбрать файл", command=select_file, bg="#E1233A", 
                            fg="white", borderwidth=0, relief="flat", padx=20, pady=10, font=("Arial", 12), 
                            activebackground="#EE4458", activeforeground="white", disabledforeground="#A8A8A8")
btn_select_file.grid(row=0, column=0, padx=30)

# Кнопка для отправки пути
btn_send_path = tk.Button(frame2, text="Отправить путь", command=send_path, bg="#E1233A", 
                          fg="white", borderwidth=0, relief="flat", padx=20, pady=10, font=("Arial", 12), 
                          activebackground="#EE4458", activeforeground="white", disabledforeground="#A8A8A8")
btn_send_path.grid(row=0, column=1, padx=30)


# Создание кнопок во втором ряду
frame3 = tk.Frame(root, bg="#4B0082")
frame3.pack(pady=10)

btn_author = create_button(frame3, "Автор на GitHub", open_author_github)
btn_author.grid(row=0, column=0, padx=10)

btn_repo = create_button(frame3, "Репозиторий GitHub", open_repository_github)
btn_repo.grid(row=0, column=1, padx=10)

btn_minimize = create_button(frame3, "Выход", exit_app)
btn_minimize.grid(row=0, column=2, padx=10)


# Загрузка изображения котика
cat_image_path = os.path.join(os.path.dirname(__file__), f'{Project_Path}\BER_Content\cat.png')  # Убедитесь, что имя файла совпадает
cat_image = Image.open(cat_image_path)
cat_image = cat_image.resize((50, 50), Image.LANCZOS)  # Изменение размера изображения
cat_photo = ImageTk.PhotoImage(cat_image)

# Добавление изображения котика в правый нижний угол
cat_label = tk.Label(root, image=cat_photo, bg="#4B0082")
cat_label.pack(side=tk.BOTTOM, anchor='se', padx=10, pady=10)  # Правый нижний угол с отступами

# Добавление действия к котику
cat_label.bind("<Button-1>", open_cat_link)


# Привязка события закрытия окна к функции on_closing
root.protocol("WM_DELETE_WINDOW", on_closing)

# Запуск иконки в системном трее в отдельном потоке
threading.Thread(target=create_tray_icon, daemon=True).start()

# Запуск основного цикла приложения
root.mainloop()
