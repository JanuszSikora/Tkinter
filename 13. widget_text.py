from tkinter import*


def skup():
    if o.focus_get() != t1:
        t1.focus_set()
    o.after(10, skup)

def l_znak(*a):
    licz_znaki.set('Znaków: ' + str(tekst1))

def l_liter(*a):
    licz_litery.set('Liter: ' + str(tekst2))

def l_cyfr(*a):
    licz_cyfry.set('Cyfr: ' + str(tekst3))

def klawisz(zdarz = None):
    global tekst1
    tekst1 +=1
    en1.insert(0, txt1)

def litera(zdarz = None):
    global tekst1, tekst2
    tekst1 += 1
    en1.insert(0, txt1)
    tekst2 += 1
    en2.insert(0, txt2)

def cyfra(zdarz = None):
    global tekst1, tekst3
    tekst1 += 1
    en1.insert(0, txt1)
    tekst3 += 1
    en3.insert(0, txt3)

def kasowanie_b(zdarz = None):
    global tekst1

    if t1.index('insert linestart') != t1.index(INSERT):
        if tekst1 <0:
            tekst1 = 0
        else:
            tekst1 -= 1
    en1.insert(0, txt1)

def kasowanie_d(zdarz = None):
    global tekst1

    if t1.index('insert lineend') != t1.index(INSERT):
        if tekst1 <0:
            tekst1 = 0
        else:
            tekst1 -= 1
    en1.insert(0, txt1)

def kombinacje(zdarz = None):
    pass

o = Tk()
o.title('Text')

t1 = Text(o, width=60, height=20, bd=5, relief=RAISED)
t1.pack(side=TOP)
t1.focus_set()
t2 = Text(o, width=60, height=1, bd=5, relief=RAISED)
t2.pack(side=TOP)

licz_znaki = StringVar()
o.register(l_znak)
licz_litery = StringVar()
o.register(l_liter)
licz_cyfry = StringVar()
o.register(l_cyfr)

en1 = Entry(t2, relief=SUNKEN, bd=2, width=26, textvariable=licz_znaki)
en2 = Entry(t2, relief=SUNKEN, bd=2, width=25, textvariable=licz_litery)
en3 = Entry(t2, relief=SUNKEN, bd=2, width=26, textvariable=licz_cyfry)

tekst1 = 0
tekst2 = 0
tekst3 = 0

txt1 = 'Znaków: '+str(tekst1)
txt2 = 'Liter: '+str(tekst2)
txt3 = 'Cyfr: '+str(tekst3)
en1.insert(0, txt1)
en2.insert(0, txt2)
en3.insert(0, txt3)

klawisze = ['<less>', '>','<space>','!','"','#','$','%','<quoteright>','(',')','*','+',',','-','.','/',\
           '0','1','2','3','4','5','6','7','8','9',':',';','=','?','@','A','B','C','D','E','F','G','H','I','J','K'\
            ,'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','<backslash>',']','^','_','`','a','b','c',\
            'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']

litery = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cyfry = ['0','1','2','3','4','5','6','7','8','9']

komb = ['<Control-<>','<Control-!>','<Control-">','<Control-#>','<Control-$>','<Control-%>',
        '<Control-(>','<Control-)>','<Control-*>','<Control-+>','<Control-,>','<Control-.>','<Control-/>','<Control-0>',\
        '<Control-1>','<Control-2>','<Control-3>','<Control-4>','<Control-5>','<Control-6>','<Control-7>','<Control-8>',\
        '<Control-9>','<Control-0>','<Control-:>','<Control-;>','<Control-=>','<Control-?>','<Control-@>','<Control-A>',\
        '<Control-B>','<Control-C>','<Control-D>','<Control-E>','<Control-F>','<Control-G>','<Control-H>','<Control-I>',\
        '<Control-J>','<Control-K>','<Control-L>','<Control-M>','<Control-N>','<Control-O>','<Control-P>','<Control-Q>',\
        '<Control-R>','<Control-S>','<Control-T>','<Control-U>','<Control-V>','<Control-W>','<Control-X>','<Control-Y>',\
        '<Control-Z>','<Control-[>','<Control-]>','<Control-^>','<Control-_>','<Control-`>','<Control-a>','<Control-b>',\
        '<Control-c>','<Control-d>','<Control-e>','<Control-f>','<Control-g>','<Control-h>','<Control-i>','<Control-j>',\
        '<Control-k>','<Control-l>','<Control-m>','<Control-n>','<Control-o>','<Control-p>','<Control-q>','<Control-r>',\
        '<Control-s>','<Control-t>','<Control-u>','<Control-v>','<Control-w>','<Control-x>','<Control-y>','<Control-z>',\
        '<Control-{>','<Control-|>','<Control-}>','<Control-~>','<Alt-<>','<Alt-!>','<Alt-">','<Alt-#>','<Alt-$>',\
        '<Alt-%>', '<Alt-(>','<Alt-)>','<Alt-*>','<Alt-+>','<Alt-,>','<Alt-.>','<Alt-/>','<Alt-0>','<Alt-1>','<Alt-2>',\
        '<Alt-3>','<Alt-4>','<Alt-5>','<Alt-6>','<Alt-7>','<Alt-8>','<Alt-9>','<Alt-0>','<Alt-:>','<Alt-;>','<Alt-=>',\
        '<Alt-?>','<Alt-@>','<Alt-B>','<Alt-D>','<Alt-F>','<Alt-G>','<Alt-H>','<Alt-I>','<Alt-J>','<Alt-K>','<Alt-M>',\
        '<Alt-P>','<Alt-Q>','<Alt-R>','<Alt-T>','<Alt-U>','<Alt-V>','<Alt-W>','<Alt-Y>','<Alt-[>','<Alt-]>','<Alt-^>',\
        '<Alt-_>','<Alt-`>','<Alt-b>','<Alt-d>','<Alt-f>','<Alt-g>','<Alt-h>','<Alt-i>','<Alt-j>','<Alt-k>','<Alt-m>',\
        '<Alt-p>','<Alt-q>','<Alt-r>','<Alt-t>','<Alt-u>','<Alt-v>','<Alt-w>','<Alt-y>','<Alt-{>','<Alt-|>','<Alt-}>',\
        '<Alt-~>']

for i in klawisze:
    t1.bind(i, klawisz)

for k in litery:
    t1.bind(k, litera)

for l in cyfry:
    t1.bind(l, cyfra)

for j in komb:
   t1.bind(j, kombinacje)

t1.bind('<BackSpace>', kasowanie_b)
t1.bind('<Delete>', kasowanie_d)

licz_znaki.set(txt1)
licz_litery.set(txt2)
licz_cyfry.set(txt3)

t2.window_create(INSERT, window=en1)
t2.window_create(INSERT, window=en2)
t2.window_create(INSERT, window=en3)

licz_znaki.trace('w', l_znak)
licz_litery.trace('w', l_liter)
licz_cyfry.trace('w', l_cyfr)

o.after(10, skup)
o.mainloop()
