import math
import random

from turtle import *

speed(10)

BOX_SIZE = 300

bgcolor("black")
pencolor("white")

#for i in range(4):
#   forward(BOX_SIZE)
#   left(90)

penup()
setposition(random.randint(0, BOX_SIZE), BOX_SIZE)
pendown()

def forward_to_boundary(max_adj, max_opp, heading_rads):
   if(abs(max_adj * math.tan(heading_rads)) < abs(max_opp)):
      forward(max_adj / math.cos(heading_rads))
   else:
      forward(max_opp / math.sin(heading_rads))


while(True):
   # pencolor(max(0, min(xcor() / BOX_SIZE, 1)), max(0, min(ycor() / BOX_SIZE, 1)), 0.1)
   pencolor(random.random(), random.random(), random.random())

   if(0 < round(xcor()) < BOX_SIZE):
      if(round(ycor()) >= BOX_SIZE):
         setheading(random.randint(180, 360))
         opposite = -ycor()
      else:
         setheading(random.randint(0, 180))
         opposite = BOX_SIZE


      if(math.cos(math.radians(heading())) > 0):
         adjacent = BOX_SIZE - xcor()
      else:
         adjacent = -xcor()

   else:
      if(round(xcor()) >= BOX_SIZE):
         setheading(random.randint(90, 270))
         adjacent = -xcor()
      else:
         setheading(random.randint(0, 180) - 90)
         adjacent = BOX_SIZE

      if(math.sin(math.radians(heading())) > 0):
         opposite = BOX_SIZE - ycor()
      else:
         opposite = -ycor()
   
   forward_to_boundary(adjacent, opposite, math.radians(heading()))

print("Final position: ", position())
print("Absolute position: ", abs(position()))

