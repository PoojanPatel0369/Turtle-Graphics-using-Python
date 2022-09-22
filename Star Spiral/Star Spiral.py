'''
Question: Create a Star Spiral using Trutle Graphics.
'''

from turtle import *

side = 400
speed(100)

for x in range(72):
    fd(side)
    lt(144)
    side = side - 4

ht()
