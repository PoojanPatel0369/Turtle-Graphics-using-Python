'''
Question: Create an Olympic Logo using Trutle Graphics.
'''

import turtle

turtle.pensize(5)
myList1=['blue','black','red']
myList2=['yellow','green']
for x in range(3):
    turtle.pencolor(myList1[x])
    turtle.circle(50)
    turtle.pu()
    turtle.fd(115)
    turtle.pd()

turtle.pu()
turtle.bk(290)
turtle.rt(90)
turtle.fd(50)
turtle.lt(90)
turtle.pd()

for y in range(2):
    turtle.pencolor(myList2[y])
    turtle.circle(50)
    turtle.pu()
    turtle.fd(115)
    turtle.pd()

turtle.ht()



































