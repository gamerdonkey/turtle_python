import math
import random

from turtle import *

speed(0)

BOX_SIZE = 900
BOUND = BOX_SIZE/2

bgcolor("black")
pencolor("white")

penup()
setposition(BOUND, BOUND)
setheading(180)
pendown()

input("Press Enter to begin...")

for i in range(4):
   forward(BOX_SIZE)
   left(90)

penup()
setposition(random.randint(-BOUND, BOUND), BOUND)
pendown()

def forward_to_boundary(max_adj, max_opp, heading_rads):
   if(abs(max_adj * math.tan(heading_rads)) < abs(max_opp)):
      forward(max_adj / math.cos(heading_rads))
   else:
      forward(max_opp / math.sin(heading_rads))


lines = 256 

for i in range(lines):
   # pencolor(max(0, min(xcor() / BOX_SIZE, 1)), max(0, min(ycor() / BOX_SIZE, 1)), 0.1)
   colormod = math.pow(i/lines, 2) * 0.7
   #colormod = i/lines
   #if(colormod <= 0.33):
   #   pencolor(1.0 - colormod * 3, colormod * 3, 0)
   #elif(0.33 < colormod <= 0.66):
   #   colormod -= 0.33
   #   pencolor(colormod * 3, 1.0 - colormod * 3, 0)
   #elif(0.66 < colormod < 0.99):
   #   colormod -= 0.66
   #   pencolor(0, 1.0 - colormod * 3, colormod * 3)
   #else:
   #   pencolor(0, 0, colormod)
   pencolor(1.0, colormod, colormod)

   if(-BOUND < round(xcor()) < BOUND):
      if(round(ycor()) >= BOUND):
         setheading(random.randint(180, 360))
         opposite = -BOX_SIZE
      else:
         setheading(random.randint(0, 180))
         opposite = BOX_SIZE


      if(math.cos(math.radians(heading())) > 0):
         adjacent = BOUND - xcor()
      else:
         adjacent = -(xcor() + BOUND)

   else:
      if(round(xcor()) >= BOUND):
         setheading(random.randint(90, 270))
         adjacent = -BOX_SIZE
      else:
         setheading(random.randint(0, 180) - 90)
         adjacent = BOX_SIZE

      if(math.sin(math.radians(heading())) > 0):
         opposite = BOUND - ycor()
      else:
         opposite = -(ycor() + BOUND)
   
   forward_to_boundary(adjacent, opposite, math.radians(heading()))

print("Final position: ", position())
print("Absolute position: ", abs(position()))
input("Press Enter to exit...")
