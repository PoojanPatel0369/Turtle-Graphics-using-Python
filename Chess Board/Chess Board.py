'''
Question:
Create a chess board using Turtle Graphics.
'''

from turtle import *

setpos(0.00,-80.00)
speed(1000)
pencolor('black')

for main in range(4):
    fd(400)
    lt(90)

def fline():
    for rows in range(4):
        color('black')
        begin_fill()
        for black in range(4):
            fd(50)
            lt(90)
        fd(50)
        end_fill()
        pencolor('black')
        for white in range(4):
            fd(50)
            lt(90)
        fd(50)
def sline():
    for Rows in range(4):
        pencolor('black')
        for Black in range(4):
            fd(50)
            lt(90)
        fd(50)
        color('black')
        begin_fill()
        for White in range(4):
            fd(50)
            lt(90)
        fd(50)
        end_fill()
        
for chess in range(1,5):
    fline()
    lt(90)
    fd(50)
    lt(90)
    fd(400)
    rt(180)
    sline()
    penup()
    home()
    setpos(0.00,-80.00)
    lt(90)
    fd(chess * 100)
    rt(90)
ht()

