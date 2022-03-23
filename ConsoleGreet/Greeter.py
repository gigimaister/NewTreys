import datetime
from rich.console import Console
from rich.progress import track
from time import sleep
import Config

console = Console()


def rev(string_word):
    return string_word[::-1]


def greet_user():
    """
    Greet User By Time
    """
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        return "בוקר טוב"
    elif 12 <= currentTime.hour < 18:
        return "צהריים טובים"
    else:
        return "ערב טוב"


class Greeter:
    pass


def ui_ruler(style, string):
    """
    Promt Ruler With (Style, String Output) To User
    """
    console.rule(f"[{style}]{string}")


def loading_bar(string, t):
    for _ in track(range(100), description=f'[green]{string}'):
        sleep(t)
