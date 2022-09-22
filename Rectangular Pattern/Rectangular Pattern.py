'''
Question: Create a Rectangular Pattern using Trutle Graphics.
'''

from math import *

def main():
    width = float(input("Enter the width of the pattern (>=180): "))
    height = float(input("Enter the height of the pattern (>=180): "))
    if width>=180 and height>=180:
        drawPattern(width, height)
    else:
        print("Please enter width and height >=180")

from turtle import *
speed(5)

def drawPattern(w, h):
    wcopy=w
    hcopy=h
    for t in range(1,4):
        if t==3:
            begin_fill()
            color("black")
    
        for rec in range (2):
            fd(w)
            lt(90)
            fd(h)
            lt(90)
        lt(45)
        fd(30*sqrt(2))
        rt(45)
        w=w-60
        h=h-60
    end_fill()
    penup()
    home()
    pendown()
    for lines in range(1,3):
        fd(wcopy/2)
        lt(90)
        fd(60)
        bk(60)
        rt(90)
        fd(wcopy/2)
        lt(135)
        fd(60*sqrt(2))
        bk(60*sqrt(2))
        rt(45)
        fd(hcopy/2)
        lt(90)
        fd(60)
        bk(60)
        rt(90)
        fd(hcopy/2)
        lt(135)
        fd(60*sqrt(2))
        bk(60*sqrt(2))
        rt(45)
main()
ht()































