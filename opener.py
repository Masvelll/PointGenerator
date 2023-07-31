#webbrowser module helps in open default web browser of os
from webbrowser import open
def open_map(x, y):
    open(f"https://yandex.ru/maps/10827/donskoy/?ll={x}%2C{y}&mode=search&sll={x}%2C{y}&text={y}%2C{x}&z=18.55")