'''
Question:
Create a hexagon spiral using Turtle Graphics.
'''
from turtle import *

side = 100
speed(100)
for x in range(100):
    fd(side)
    lt(60)
    side = side - 1

ht()
