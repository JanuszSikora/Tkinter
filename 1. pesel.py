from tkinter import*
from tkinter import messagebox


def wczytuj_cyfry(*a):
    global psl, cyfra
    ps = psl.get()
    if ps == '' or ps.isdigit():
        cyfra = ps
    else:
        psl.set(cyfra)


def sprawdz():
    pesel = list(cyfra)
    pesel1 = []
    for i in range(len(pesel)):
        pesel1.append(int(pesel[i]))
    if len(pesel) == 11 and ((9*pesel1[0]+7*pesel1[1]+3*pesel1[2]+1*pesel1[3]+9*pesel1[4]+7*pesel1[5]+3*pesel1[6]+1*pesel1[7]+9*pesel1[8]+7*pesel1[9])%10)==pesel1[10]:
            messagebox.showinfo('','To prawidłowy nr PESEL!')
    else:
        messagebox.showinfo('', 'Nieprawidłowy nr PESEL!')


o = Tk()
Label(o,text='''Wprowadź nr PESEL; naciśnij przycisk "Sprawdź",
      żeby sprawdzić jego poprawność''').grid(row=0)
Label(o,text='PESEL:').place(x=30,y=35)

cyfra = ''
psl = StringVar()
wcyfr = o.register(wczytuj_cyfry)
e = Entry(o, textvariable=psl)
psl.set(cyfra)
psl.trace('w',wczytuj_cyfry)  # wywołanie obserwatora
e.grid(row=1)
e.focus_set()
Button(o, text='Sprawdź', command=sprawdz).grid(row=2)
o.mainloop()
