import platform
import re
from styles import style
from PyInquirer import prompt
import os

def screencls():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    if platform.system() == "Windows":
        os.system("cls")


def back():
    question = [
        {
            "type": "list",
            "name": "back",
            "message": "choose",
            "choices": ["Back"]
        }
    ]
    ans = prompt(question, style=style)
    if ans["back"] == "Back":
        return True