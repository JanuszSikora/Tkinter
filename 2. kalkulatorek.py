from tkinter import*
from tkinter import messagebox


def oblicz():
    global liczba1, liczba2, e1, e2, switch

    wynik = ''
    licz1 = list(liczba1.get())
    licz2 = list(liczba2.get())
    niecyfra = 0
    for i in licz1:
        if ord(i)<32 or 44<ord(i)<47 or 47<ord(i)<58 or ord(i) == 127:
            pass
        else:
            niecyfra = 1

    for i in licz2:
        if ord(i)<32 or 44<ord(i)<47 or 47<ord(i)<58 or ord(i) == 127:
            pass
        else:
            niecyfra = 2

    if niecyfra == 0:
        if switch.get() == 1:
            wynik = float(liczba1.get())+float(liczba2.get())
        if switch.get() == 2:
            wynik = float(liczba1.get())-float(liczba2.get())
        if switch.get() == 3:
            if float(liczba2.get()) == 0:
                messagebox.showinfo('', 'Wprowadź prawidłowo liczbę w prawym oknie;\
 ten kalkulator nie dzieli przez zero ;-)')
                wynik = ''
                e2.focus_set()
            else:
                wynik = float(liczba1.get())/float(liczba2.get())
        if switch.get() == 4:
            wynik = float(liczba1.get())*float(liczba2.get())

        if wynik == '':
            pass
        elif wynik == 0:
            messagebox.showinfo('Wynik to: ', '0')
        else:
            messagebox.showinfo('Wynik to: ', wynik)

    elif niecyfra == 1:
        messagebox.showinfo('', 'Wprowadź prawidłowo liczbę w lewym oknie; symbol dziesiętny to kropka')
        e1.focus_set()
    else:
        messagebox.showinfo('', 'Wprowadź prawidłowo liczbę w prawym oknie; symbol dziesiętny to kropka')
        e2.focus_set()


o = Tk()
o.title('Kalkulatorek')

switch = IntVar()
plus = Radiobutton(o, text='+',variable=switch, value=1)
plus.select()
minus = Radiobutton(o, text='-',variable=switch, value=2)
dziel = Radiobutton(o, text='/',variable=switch, value=3)
mnoz = Radiobutton(o, text='*',variable=switch, value=4)
plus.pack()
minus.pack()
dziel.pack()
mnoz.pack()

liczba1=StringVar()
liczba2=StringVar()
e1 = Entry(o, textvariable=liczba1, width=20)
e1.place(x=470, y=50)
e2 = Entry(o, textvariable=liczba2, width=20)
e2.place(x=680, y=50)
obl = Button(o, text='Oblicz', command=oblicz).place(x=610,y=150)
o.mainloop()
