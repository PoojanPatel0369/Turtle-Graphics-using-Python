'''
Question: Create an Pentagon Spiral using Trutle Graphics.
'''

from turtle import *

side = 200
speed(100)
for x in range(100):
    fd(side)
    lt(72)
    side = side -2

ht()
