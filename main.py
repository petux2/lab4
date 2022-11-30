import random
from tkinter import *
from PIL import ImageTk, Image

def gen():
    s = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
    l = {}
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
            if 65 <= c <= 90: break
        r[j] = f'{a[0]}{a[1]}{a[2]}{a[3]}'
    return f'{r[0]}-{r[1]}-{r[2]}'

window = Tk()
window.title("Генератор ключа")
window.geometry('400x500')
window.resizable(height=False, width=False)

img = Image.open('art.png')
img = img.resize((400, 500))
img = ImageTk.PhotoImage(img)
panel = Label(window, image=img)
panel.pack()

lbl = Label(window, text='XXXX-XXXX-XXXX', font=('Arial Bold', 12))
lbl.place(x=100, y=220, width=200, height=30)

def click():
    lbl.configure(text=gen())

btn = Button(text='Сгенерировать ключ', command=click)
btn.place(x=120, y=400, width=160, height=30)

window.mainloop()
