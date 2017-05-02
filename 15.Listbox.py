from tkinter import*


def skup():
    if o.focus_get() == e:
        l1.focus_set()
    o.after(10, skup)


def oblicz(*a):
    pass


def ptaszek(*a):
    global month_no, day_no, l1, flag_day, flag_month, flag_check

    if flag_month == 1 and month_no > 31:
        if przestepny.get() == 1:
            month_no = month_no + 1
        elif przestepny.get() == 0 and flag_check == 1:
            month_no = month_no - 1
        else:
            pass
    flag_check = 1

    wynik = day_no + month_no
    policz.set(wynik)


def przel_pot(zdarz=None):
    global wynik, l1, month_no, day_no, flag_month, dni

    flag_month = 1
    month_no = pelne_msce[l1.index(ACTIVE) - 1]
    if przestepny.get() == 1:
        month_no += 1
    l2.selection_clear(l2.index(ACTIVE))
    l2.selection_set(0)
    day_no = dni[0]
    wynik = day_no + month_no

    if flag_day == 1:
        policz.set(wynik)


def przel_pot2(zdarz=None):
    global wynik, l2, month_no, day_no, flag_day

    flag_day = 1
    if month_no == 31:
        if przestepny.get() == 1:
            if dni[l2.curselection()[0]] > 29:
                l2.selection_clear(l2.index(ACTIVE))
                l2.selection_set(28)
                day_no = dni[l2.index(28)]
            else:
                day_no = l2.get(ACTIVE)
        else:  # przestepny.get() == 0:
            if dni[l2.curselection()[0]] > 28:
                l2.selection_clear(l2.index(ACTIVE))
                l2.selection_set(27)
                day_no = dni[l2.index(27)]
            else:
                day_no = l2.get(ACTIVE)
    elif month_no == 90 or month_no == 151 or month_no == 243 or month_no == 304:
        if dni[l2.curselection()[0]] > 30:
            l2.selection_clear(l2.index(ACTIVE))
            l2.selection_set(29)
            day_no = dni[l2.index(29)]
        else:
            day_no = l2.get(ACTIVE)
    else:
        day_no = l2.get(ACTIVE)

    wynik = day_no + month_no

    if flag_month == 1:
        policz.set(wynik)


o = Tk()
o.title('Listbox')

month_no = 0
day_no = 0
wynik = 0
flag_month = 0
flag_day = 0
flag_check = 0
policz = StringVar()
przestepny = IntVar()
o.register(oblicz)
o.register(ptaszek)

miesiace = ['styczeń', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik',
            'listopad', 'grudzień']
dni = []
for i in range(1, 32):
    dni.append(i)

pelne_msce = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 0]

l1 = Listbox(o, selectmode=EXTENDED, height=12)
l1.grid(row=1, column=1)
l2 = Listbox(o, selectmode=EXTENDED, height=31)
l2.grid(row=1, column=2)
b = Checkbutton(o, text='rok przestępny', variable=przestepny)
b.grid(row=2, column=1, columnspan=2)

for i in miesiace:
    l1.insert(END, i)

for i in dni:
    l2.insert(END, i)

l1.bind('<Double-Button-1>', przel_pot)
l2.bind('<Double-Button-1>', przel_pot2)

e = Entry(o, bd=5, relief=GROOVE, textvariable=policz)
e.grid(row=3, column=1, columnspan=2)
e.bind('<Key>', skup)
e.insert(0, wynik)
policz.trace('w', oblicz)
przestepny.trace('w', ptaszek)

o.after(10, skup)
o.mainloop()
