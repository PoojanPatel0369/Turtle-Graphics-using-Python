'''
Question:
Create a flower pattern using Turtle Graphics.
'''

from turtle import *

def pattern():
    for x in range(2):
        fd(100)
        lt(45)
        fd(100)
        lt(135)
for y in range(8):
    pattern()
    lt(45)

ht()
done()
