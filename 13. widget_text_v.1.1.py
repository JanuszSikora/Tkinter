from tkinter import*


def skup():
    if o.focus_get() != t1:
        t1.focus_set()
    o.after(10, skup)

def l_release(*a):
    licz_znaki.set('Znaków: ' + str(tekst1))
    licz_litery.set('Liter: ' + str(tekst2))
    licz_cyfry.set('Cyfr: ' + str(tekst3))

def puszczony_klawisz(zdarz=None):
    global tekst1, tekst2, tekst3
    tekst1 = 0
    tekst2 = 0
    tekst3 = 0

    for i in t1.get(1.0, END):
        if i.isalnum():
            tekst1 += 1
        if i.isalpha():
            tekst2 += 1
        if i.isdigit():
            tekst3 += 1

    licz_znaki.set(str(tekst1))
    licz_litery.set(str(tekst2))
    licz_cyfry.set(str(tekst3))
    en1.insert(0, txt1)
    en2.insert(0, txt2)
    en3.insert(0, txt3)


o = Tk()
o.title('Text')

t1 = Text(o, width=60, height=20, bd=5, relief=RAISED)
t1.pack(side=TOP)
t1.focus_set()
t2 = Text(o, width=60, height=1, bd=5, relief=RAISED)
t2.pack(side=TOP)

licz_znaki = StringVar()
licz_litery = StringVar()
licz_cyfry = StringVar()
count_release = StringVar()
o.register(l_release)

en1 = Entry(t2, relief=SUNKEN, bd=2, width=26, textvariable=licz_znaki)
en2 = Entry(t2, relief=SUNKEN, bd=2, width=25, textvariable=licz_litery)
en3 = Entry(t2, relief=SUNKEN, bd=2, width=26, textvariable=licz_cyfry)

tekst1 = 0
tekst2 = 0
tekst3 = 0

txt1 = 'Znaków: '
txt2 = 'Liter: '
txt3 = 'Cyfr: '
en1.insert(0, txt1)
en2.insert(0, txt2)
en3.insert(0, txt3)

t1.bind('<KeyRelease>', puszczony_klawisz)
licz_znaki.set(txt1)
licz_litery.set(txt2)
licz_cyfry.set(txt3)

t2.window_create(INSERT, window=en1)
t2.window_create(INSERT, window=en2)
t2.window_create(INSERT, window=en3)

count_release.trace('w', l_release)

o.after(10, skup)
o.mainloop()
