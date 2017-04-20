from tkinter import*


o = Tk()
zagl = Canvas(o, width=600, height=400, bg='white')
zagl.create_line(80,350,520,350,570,270,30,270,80,350, fill='red')
zagl.create_line(400,270,400,30,410,30,410,270, fill='red')
zagl.create_line(410,50,500,100,410,150,500,200,410,250,fill='red')
zagl.create_line(190,270,190,200,200,200,200,270,fill='red')
zagl.create_line(190,100,190,30,200,30,200,100,fill='red')
zagl.create_line(110,100,280,100,fill='red')
zagl.create_line(110,200,280,200,fill='red')
zagl.create_arc(60,100,160,200,outline='red', start='270', \
                extent='180', width='0.5', style='arc')
zagl.create_arc(230,100,330,200,outline='red', start='90', \
                extent='180', width='0.5', style='arc')
zagl.create_oval(420,290,450,320,outline='red')
zagl.create_oval(470,290,500,320,outline='red')
zagl.create_rectangle(15,250,50,240,outline='red', fill='red')
zagl.create_rectangle(15,230,50,240,outline='red')
zagl.create_line(50,250,50,270,fill='red')
for i in range (0,600,25):
    zagl.create_arc(5+i,375,30+i,350,outline='blue', start='15', \
                extent='150', width='2', style='arc')
zagl.create_line(100,210,100,270,fill='gold', width='2')
zagl.create_line(75,235,125,235,fill='gold', width='2')
zagl.create_oval(80,215,120,255,outline='gold',width='2')
zagl.create_line(80,220,120,250,fill='gold', width='2')
zagl.create_line(80,250,120,220,fill='gold', width='2')
zagl.create_text(130,310,text='TSR 2017',justify='center', \
                 font=('arial','20','bold'))

zagl.grid(row=0)
o.mainloop()
