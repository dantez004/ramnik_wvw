#ramnik with visual window
from tkinter import *
from tkinter import ttk
#functions
def out_value(style, height=0):
    #принимает как str style и int рост
    if height == 0:
        lbl['text'] = 'введи свой рост'
    elif style == 'street':
        if height < 140: lbl['text'] = 'слишком низко'
        elif height >= 140 and height <= 149:lbl['text'] = 'советую размер рамы 19-19.5"'
        elif height >= 150 and height <= 154:lbl['text'] = 'советую размер рамы 20-20.25"'
        elif height >= 155 and height <= 159:lbl['text'] = 'советую размер рамы 20.3-20.4"'
        elif height >= 160 and height <= 169 :lbl['text'] = 'советую размер рамы 20.4-20.5"'
        elif height >= 170 and height <= 174 :lbl['text'] = 'советую размер рамы 20.5-20.6"'
        elif height >= 175 and height <= 180 :lbl['text'] = 'советую размер рамы 20.7-20.8"'
        elif height >= 181 and height <= 189 :lbl['text'] = 'советую размер рамы 20.9-21"'
        elif height >= 190 and height <= 199 :lbl['text'] = 'советую размер рамы 21-21.25"'
    elif style == 'park':
        if height <150: lbl['text'] = 'слишком низко'
        elif height >= 150 and height <= 153: lbl['text'] = 'советую размер рамы 20.2"'
        elif height >= 154 and height <= 158: lbl['text'] = 'советую размер рамы 20.3-20.5"'
        elif height >= 159 and height <= 169: lbl['text'] = 'советую размер рамы 20.6-20.7"'
        elif height >= 170 and height <= 174: lbl['text'] = 'советую размер рамы 20.8"'
        elif height >= 175 and height <= 179: lbl['text'] = 'советую размер рамы 20.7-20.9"'
        elif height >= 180 and height <= 190: lbl['text'] = 'советую размер рамы 20.8-21"'
        elif height >= 190 and height <= 199: lbl['text'] = 'советую размер рамы 21-21.2"'

def entry_clear():
    if entry.get():
        if float(str(entry.get()).replace(',', '.')) > 200 or float(str(entry.get()).replace(',', '.')) < 140:
            entry.delete(0, END)
            return 0
        elif len(entry.get()) > 3:
            entry.delete(3, END)
        out_value(style.get(), int(entry.get()))
    elif not entry.get():
        lbl['text'] = 'введи свой рост'

#head code

head = Tk()
head.title('ramnik')

street = 'street'
park = 'park'
style = StringVar(value=street)
#body(window) code

lbl = ttk.Label(text='я подскажу тебе длину bmx рамы для твоего роста)', font=('Arial', 10))#инициализация текста
lbl.grid(column=0, row=0, columnspan=3, rowspan=2, ipadx=1, ipady=2)#позиционирование текста
street_radiob = ttk.Radiobutton(text=street, value=street, variable=style)#инициализация радио стрита
street_radiob.grid(column=0, row=2, ipadx=1, ipady=1)#позиционирование радио стрита
park_radiob = ttk.Radiobutton(text=park, value=park, variable=style)#инит радио парка
park_radiob.grid(column=0, row=3, ipadx=1, ipady=1)#позициона радио парка
entry = ttk.Entry()#инит поля ввода роста
entry.grid(column=0, columnspan= 1, row=4, ipadx=0, ipady=1)#позиционка поля ввода роста
btn = ttk.Button(text='посчитать длину рамы', command=entry_clear)#инит кнопки расчёта
btn.grid(column=1, row=4, ipadx=1, ipady=1)#позиционка кнопки расчёта


head.mainloop()