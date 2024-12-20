import os
import time
import sys
import win32com.client

# Укажите имя файла и иконки
target_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Start.bat")  # Путь к вашему файлу
icon_file = "BER_Content\\icon.ico"       # Путь к вашей иконке

# Создаем имя ярлыка
shortcut_name = os.path.join(os.path.join(os.path.dirname(__file__), os.pardir), "Bot Easy Remote.lnk")  # Ярлык будет называться Start.lnk

# Проверяем, существует ли ярлык
if os.path.exists(shortcut_name):
    print(f"Ярлык '{shortcut_name}' уже существует.")
    time.sleep(5)  # Ждем 5 секунд
    sys.exit()

# Получаем путь к текущей папке
current_dir = os.path.dirname(os.path.join(os.path.dirname(__file__), os.pardir))

# Создаем ярлык
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortcut(shortcut_name)
shortcut.TargetPath = target_file
shortcut.IconLocation = os.path.join(current_dir, icon_file)
shortcut.Save()

print(f"Ярлык '{shortcut_name}' успешно создан.")