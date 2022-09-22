'''
Question:
Circle overlap pattern using turtle.
'''

from turtle import *

myColour = ['black','red','green','yellow','blue']

def crc():
    speed(10000)
    for y in range(10):
        for x in range(10):
            circle(100 - (10*x))
        rt(36 + (y))

for repeat in range(5):
    pencolor(myColour[repeat])
    crc()
    
