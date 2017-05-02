from tkinter import*
from tkinter import messagebox


def obs_wyn(*a):
    policz.set(wynik)

def oblicz():
    global wynik
    wynik = switch_pion.get()*switch_poz.get()
    policz.set(wynik)
    l['fg'] = kolor[wynik-1]


o = Tk()
o.title('Tabliczka')

switch_pion = IntVar()
switch_poz = IntVar()
policz = IntVar()
o.register(obs_wyn)

pionowe = []
poziome = []
wynik = 1

for i in range(10):
    pionowe.append('b'+str(i+1))

for i in range(10):
    pionowe[i] = Radiobutton(o, text=str(i+1),variable=switch_pion, value=i+1, command=oblicz)
    pionowe[i].grid(row=i+2, column=0)

pionowe[0].select()

for i in range(10):
    poziome.append('a'+str(i+1))

for i in range(10):
    poziome[i] = Radiobutton(o, text=str(i+1),variable=switch_poz, value=i+1, command=oblicz)
    poziome[i].grid(row=0, column= i+2)

poziome[0].select()
policz.set(1)

kolor = []
for i in range(100):
    kolor.append(str(hex(3*i)))
    kolor[i].upper()
for i in range(100):
    if len(kolor[i]) == 3:
        kolor[i] = '#000'+kolor[i]
    elif len(kolor[i]) == 4:
        kolor[i] = '#00' + kolor[i]
    elif len(kolor[i]) == 5:
        kolor[i] = '#0' + kolor[i]
    else:
        pass

for i in range(100):
    kolor[i] = kolor[i].upper()


print(kolor)

kolor = ['#FF00A0', '#FF00A3', '#FF00A6', '#FF00A9', '#FF00AC', '#FF00AF', '#FF0A12', '#FF0A15', '#FF0A18', '#FF0A1B',\
         '#CC0A1E', '#CC0A21', '#CC0A24', '#CC0A27', '#CC0A2A', '#CC0A2D', '#CC0A30', '#CC0A33', '#CC0A36', '#CC0A39',\
         '#000A3C', '#000A3F', '#000A42', '#000A45', '#000A48', '#000A4B', '#000A4E', '#000A51', '#000A54', '#000A57',\
         '#000A5A', '#000A5D', '#000A60', '#000A63', '#000A66', '#000A69', '#000A6C', '#000A6F', '#000A72', '#000A75',\
         '#000A78', '#000A7D', '#000A7E', '#000A81', '#000A84', '#000A87', '#000A8A', '#000A8D', '#000A90', '#000A93',\
         '#000A96', '#000A99', '#000A9C', '#000A9F', '#000AA2', '#000AA5', '#000AA8', '#000AAB', '#000AAE', '#000AB1',\
         '#000AB4', '#000AB7', '#000ABA', '#000ABD', '#000AC0', '#000AC3', '#000AC6', '#000AC9', '#000ACC', '#000ACF',\
         '#000AD2', '#000AD5', '#000AD8', '#000ADB', '#000ADE', '#000AE1', '#000AE4', '#000AE7', '#000AEA', '#000AED',\
         '#000AF0', '#000AF3', '#000AF6', '#000AF9', '#000AFC', '#000AFF', '#00A102', '#00A105', '#00A108', '#00A10B',\
         '#00A10E', '#00A111', '#00A114', '#00A117', '#00A11A', '#00A11D', '#00A120', '#00A123', '#00A126', '#00A129']

l = Label(o, textvariable=policz, font=("Arial", "120", "bold"))
l.place(x=100, y=80)
policz.trace('w', obs_wyn)


o.mainloop()