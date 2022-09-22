'''
Question: Create an Octagon Spiral using Trutle Graphics.
'''

from turtle import *

side = 100
speed(100)
for x in range(100):
    fd(side)
    lt(45)
    side = side - 1

ht()
