from tkinter import*


def skup():
    if o.focus_get() == e:
        sp1.focus_set()
    o.after(10, skup)

def oblicz(*a):
    global e
    policz.set(wynik)

def przel_pot():
    global wynik
    for i in range(len(wartosci)):
        if wartosci[i] == sp4.get():
            wynik0 = i
        if wartosci[i] == sp3.get():
            wynik1 = i*16
        if wartosci[i] == sp2.get():
            wynik2 = i*16**2
        if wartosci[i] == sp1.get():
            wynik3 = i*16**3
    wynik = wynik3 + wynik2 + wynik1 + wynik0
    e.delete(0,END)
    e.insert(0, wynik)


o = Tk()
o.title('Spinbox')
wynik3 = wynik2 = wynik1 = wynik0 = 0
wynik = 0
policz = StringVar()
o.register(oblicz)

wartosci = ['0x0','0x1','0x2','0x3','0x4','0x5','0x6','0x7','0x8','0x9','0xA','0xB','0xC','0xD','0xE','0xF']

sp1 = Spinbox(o, values=wartosci, command=przel_pot, width=4, state='readonly')
sp1.place(x=500,y=50)
sp2 = Spinbox(o, values=wartosci, command=przel_pot, width=4, state='readonly')
sp2.place(x=540,y=50)
sp3 = Spinbox(o, values=wartosci, command=przel_pot, width=4, state='readonly')
sp3.place(x=580,y=50)
sp4 = Spinbox(o, values=wartosci, command=przel_pot, width=4, state='readonly')
sp4.place(x=620,y=50)
e = Entry(o, bd=5, relief=GROOVE, textvariable=policz)
e.place(x=515, y=70)
e.bind('<Key>', skup)
e.insert(0, wynik)

o.after(10, skup)
o.mainloop()
