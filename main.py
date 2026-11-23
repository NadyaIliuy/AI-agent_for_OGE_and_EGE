import json
from pyscript import document
from pyscript.ffi import create_proxy

state = {
    "exam": "oge",
    "subject": "math",
    "variant": None,
    "current_index": 0,
}

ACTIVE_SUBJECTS = {
    "math": "Математика",
    "physics": "Физика",
}

def show_screen(screen_id):
    for section in document.querySelectorAll(".screen"):
        section.classList.add("hidden")
    document.querySelector(f"#{screen_id}").classList.remove("hidden")

def go_to_exam(event):
    show_screen("slide-2-1")

def go_to_start(event):
    show_screen("slide-1")

p_start = create_proxy(go_to_exam)
p_back = create_proxy(go_to_start)

document.querySelector("#btn-start").addEventListener("click", p_start)
document.querySelector("#btn-back-to-1").addEventListener("click", p_back)

def go_to_subject(event):
    show_screen("slide-3")

p_oge = create_proxy(go_to_subject)
p_ege = create_proxy(go_to_subject)
p_back2 = create_proxy(go_to_exam)

document.querySelector("#btn-new-oge").addEventListener("click", p_oge)
document.querySelector("#btn-new-ege").addEventListener("click", p_ege)
document.querySelector("#btn-back-to-2").addEventListener("click", p_back2)

def load_tasks_db():
    with open("data/tasks_oge.json", "r", encoding="utf-8") as f:
        return json.load(f)

TASKS_DB = load_tasks_db()

math_tasks = len(TASKS_DB["oge"]["math"][0]["tasks"])
document.querySelector("#py-status").innerText = (
    f"Python готов! Задач ОГЭ по математике: {math_tasks}"
)

print("Python готов!")