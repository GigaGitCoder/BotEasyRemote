@echo off
setlocal

rem Устанавливаем заголовок консольного окна
title Logs

rem Указываем путь к файлу lang_var.txt
set "langFile=%~dp0Body\lang_var.txt"

rem Читаем содержимое файла
set /p lang=<%langFile%

rem Проверяем значение переменной lang и запускаем соответствующий скрипт
if "%lang%"=="ru" (
    python "%~dp0Body\RemoteRU.py"
) else if "%lang%"=="en" (
    python "%~dp0Body\RemoteEN.py"
) else (
    echo Неверное значение в lang_var.txt. Ожидалось "ru" или "en".
)

endlocal