import math
import random

from turtle import *

#speed(10)

BOX_SIZE = 300

bgcolor("black")
pencolor("white")

for i in range(4):
   forward(BOX_SIZE)
   left(90)

penup()
setposition(random.randint(0, BOX_SIZE), 0)
setheading(random.randint(280, 370))
pendown()

while(True):
   pencolor(max(0, min(xcor() / BOX_SIZE, 1)), max(0, min(ycor() / BOX_SIZE, 1)), 0.1)

   if((not 0 < xcor() < BOX_SIZE) or (not 0 < ycor() < BOX_SIZE)):
      left(80)
   
   forward(2)

print("Final position: ", position())
print("Absolute position: ", abs(position()))

