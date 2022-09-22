'''
Question:
Turtle Graphics: City Skyline
'''

from turtle import *
from tkinter import *

def main():
    borders()
    buildings()
    windows()
    stars()

def borders():
    pu()
    setpos(-275.00, -350.00)
    pd()
    begin_fill()
    color("black" )
    for x in range(2):
        fd(550)
        lt(90)
        fd(700)
        lt(90)
    end_fill()
        
def buildings():
    pu()
    setpos(-275.00, -350.00)
    pd()
    begin_fill()
    color("grey")
    fd(550)
    lt(90)
    fd(300)
    lt(90)
    fd(65)
    rt(90)
    fd(100)
    lt(90)
    fd(35)
    rt(90)
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    fd(150)
    rt(90)
    fd(75)
    rt(90)
    fd(250)
    lt(90)
    fd(150)
    lt(90)
    fd(225)
    rt(90)
    fd(75)
    lt(90)
    fd(100)
    rt(90)
    fd(50)
    lt(90)
    fd(275)
    end_fill()

def windows():
    def win():
        pd()
        begin_fill()
        color("white")
        for x in range(4):
            fd(15)
            lt(90)
        end_fill()
        pu()

    pu()
    setpos(-210.00, -7.00)
    win()
    setpos(-135.00, 175.00)
    win()
    setpos(-135.00, 200.00)
    win()
    setpos(-60.00, -100.00)
    win()
    setpos(-30.00, 115.00)
    win()
    setpos(90.00, 105.00)
    win()

def stars():
    def dots():
        dot(5, "white")

    setpos(-255.00, 138.00)
    dots()
    setpos(-220.00, 246.00)
    dots()
    setpos(-180.00, 125.00)
    dots()
    setpos(-50.00, 305.00)
    dots()
    setpos(60.00, 235.00)
    dots()
    setpos(205.00, 110.00)
    dots()
    setpos(250.00, 290.00)
    dots()
    ht()

window = Tk()

window.geometry('200x50')

lbl = Label(window, text="Namaste!")

lbl.grid(column=0, row=0)

def clicked():
    #speed(100)
    main()

btn = Button(window, text="Click to continue!", command=clicked)

btn.grid(column=1, row=1)

window.mainloop()

