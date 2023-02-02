'''
Question: Create a Car Racing Game using Trutle Graphics.
'''

from turtle import *
from random import *

speed(1000)

pu()
setpos(-300.00,100.00)
pd()

for rows in range(1,6):
    fd(600)
    pu()
    home()
    setpos(-300.00,100.00)
    lt(90)
    fd(rows*50)
    rt(90)
    pd()

pu()
home()
setpos(-300.00,100.00)
pd()

ht()

#shape("turtle")

Satyam = Turtle()
Satyam.shape("turtle")
Satyam.color('purple')
Shivam = Satyam.clone()
Shivam.color('blue')
Sundaram = Shivam.clone()
Sundaram.color('green')
Suhradam = Sundaram.clone()
Suhradam.color('orange')

#For Satyam
Satyam.pu()
Satyam.goto(-300.00,125.00)
#Satyam.pd()

#For Shivam
Shivam.pu()
Shivam.goto(-300.00,175.00)
#Shivam.pd()

#For Sundaram
Sundaram.pu()
Sundaram.goto(-300.00,225.00)
#Sundaram.pd()

#For Suhradam
Suhradam.pu()
Suhradam.goto(-300.00,275.00)
#Suhradam.pd()

#For Rotation
for rot in range(36):
    Satyam.tilt(10)
    Shivam.tilt(10)
    Sundaram.tilt(10)
    Suhradam.tilt(10)
    
#For Race
for race in range(250):
    Satyam.fd(randint(1,4))
    Shivam.fd(randint(1,4))
    Sundaram.fd(randint(1,4))
    Suhradam.fd(randint(1,4))





































