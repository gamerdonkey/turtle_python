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
setposition(0, random.randint(0, BOX_SIZE))
pendown()

while(True):
   pencolor(max(0, min(xcor() / BOX_SIZE, 1)), max(0, min(ycor() / BOX_SIZE, 1)), 0.1)

   if((not 0 < xcor() < BOX_SIZE) or (not 0 < ycor() < BOX_SIZE)):
      if(0 < xcor() < BOX_SIZE):
         if(ycor() >= BOX_SIZE):
            setheading(random.randint(180, 360))
         else:
            setheading(random.randint(0, 180))
      else:
         if(xcor() >= BOX_SIZE):
            setheading(random.randint(90, 270))
         else:
            setheading(random.randint(0, 180) - 90)
   #print("Position: ", position(), " Heading: ", heading())            
   forward(2)

print("Final position: ", position())
print("Absolute position: ", abs(position()))

