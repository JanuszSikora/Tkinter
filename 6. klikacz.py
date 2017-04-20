from tkinter import*
from tkinter import messagebox
from random import randint


def klik(event):

    indeks = str(event.widget)
    try:
        ind = int(indeks[8:]) - 1
    except ValueError:
        ind = 0

    tbchecked = lista[ind]['text']
    if tbchecked == liczby_sort[0]:
        del liczby_sort[0]
        lista[ind]['state'] = DISABLED
    else:
        pass

    if liczby_sort == []:
        messagebox.showinfo('', 'Gratulacje!!!\n Wskazałaś/łeś wszystkie liczby w rosnącej kolejności.')


def draw():
    global liczby_sort

    while len(liczby)<len(zmienne):
        l = randint(1,999)
        if l not in liczby:
            liczby.append(l)
    liczby_sort = sorted(liczby[:])


o = Tk()
o.title('Klikacz')
f = Frame(o, height=100, width=400)
f.grid(row=0, column=0)

messagebox.showinfo('', 'Zadanie użytkownika polega na klikaniu przycisków w \
kolejności rosnących liczb')

zmienne = []
liczby = []
for f in range(1,6):
    for j in range(1,6):
        zmienne.append('b'+str(f)+str(j))

draw()

lista = zmienne[:]
k = 1
for i in range(len(zmienne)):
    lista[i] = Button(o, text=liczby[i],height=1, width=8)
    lista[i].bind("<Button-1>",klik)
    if (i)%5 == 0:
        k += 1
    lista[i].grid(row=k, column=i%5+1)

o.mainloop()
