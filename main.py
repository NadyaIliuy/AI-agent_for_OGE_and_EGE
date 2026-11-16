"""Стартовый скрипт Урока 1: проверяем связь Python и HTML-страницы."""

import sys
from pyscript import document
from pyscript.ffi import create_proxy

# Находим элементы на HTML-странице по их id
status_box = document.querySelector("#status-box")
hello_button = document.querySelector("#hello-btn")

# Сразу меняем текст при успешной загрузке Python
python_version = sys.version.split()[0]
status_box.innerText = f"Привет, Надя и Николай! Python {python_version} успешно запущен в браузере."

click_count = 0


def on_button_click(event):
    """Срабатывает при каждом нажатии на кнопку."""
    global click_count
    click_count += 1
    status_box.innerText = (
        f"PyScript работает отлично! Кнопка нажата {click_count} раз(а)."
    )


# Привязываем функцию on_button_click к событию "click" на кнопке
hello_button.addEventListener("click", create_proxy(on_button_click))
