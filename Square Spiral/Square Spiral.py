'''
Question: Create a Spiral Square using Trutle Graphics.
'''

from turtle import *

side = 200
speed(100)
for x in range(100):
    fd(side)
    lt(90)
    side = side -2

ht()
