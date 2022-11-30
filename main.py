# Никулин Максим 368594

import random
from tkinter import *
from PIL import ImageTk, Image
from pygame import mixer

#функция для генерации ключа
def gen_key():
    s = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
    l = {}

    #весовые коэффициенты
    for i in range(len(s)):
        l[s[i]] = i + 1

    r = ['', '', '']

    for j in range(3):
        while True:
            c = 0
            a = []
            for i in range(4):
                b = random.choice(s)
                c += l[b]
                a.append(b)
            if 65 <= c <= 90: break #интервал от 65 до 90

        r[j] = f'{a[0]}{a[1]}{a[2]}{a[3]}'

    return f'{r[0]}-{r[1]}-{r[2]}'

def click():
    lbl.configure(text=gen_key())

#объявление окна
window = Tk()
window.title("Генератор ключа")
window.geometry('400x500')
window.resizable(height=False, width=False)

#музыка
mixer.init()
mixer.music.load('music.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

#арт на фон
img = Image.open('art.png')
img = img.resize((400, 500))
img = ImageTk.PhotoImage(img)
panel = Label(window, image=img)
panel.pack()

#кнопка генерации и область для ключа
lbl = Label(window, text='XXXX-XXXX-XXXX', font=('Arial Bold', 12))
lbl.place(x=100, y=220, width=200, height=30)
btn = Button(text='Сгенерировать ключ', command=click)
btn.place(x=120, y=400, width=160, height=30)

window.mainloop()