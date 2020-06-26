import math
import random

from turtle import *

def forward_to_position(dest_x, dest_y):
   delta_x = dest_x - xcor()
   delta_y = dest_y - ycor()

   setheading(math.degrees(math.atan2(delta_y, delta_x)) % 360)
   setposition(dest_x, dest_y)

speed(0)

GRAPH_SIZE = 720
PHASE_SHIFT = 45

bgcolor("black")
pencolor("white")

penup()
setposition(0, GRAPH_SIZE/2)
pendown()
setposition(0, -GRAPH_SIZE/2)
penup()
setposition(GRAPH_SIZE/2, 0)
pendown()
setposition(-GRAPH_SIZE/2, 0)

input("Press Enter to begin...")

penup()
speed(1)
forward_to_position(-GRAPH_SIZE/2, math.sin(math.radians(PHASE_SHIFT))*(GRAPH_SIZE/4))
speed(0)
pendown()
pencolor("cyan")

for i in range(math.floor(-GRAPH_SIZE/2), math.floor(GRAPH_SIZE/2)+1):
   forward_to_position(i, math.sin(math.radians(i+PHASE_SHIFT))*(GRAPH_SIZE/4))


penup()
speed(1)
forward_to_position(GRAPH_SIZE/2, math.sin(math.radians(0))*(GRAPH_SIZE/4))
speed(0)
pendown()
pencolor("magenta")

for i in range(math.floor(GRAPH_SIZE/2), math.floor(-GRAPH_SIZE/2)-1, -1):
   forward_to_position(i, math.sin(math.radians(i))*(GRAPH_SIZE/4))


penup()
speed(1)
forward_to_position(-GRAPH_SIZE/2, math.sin(math.radians(-PHASE_SHIFT))*(GRAPH_SIZE/4))
speed(0)
pendown()
pencolor("yellow")

for i in range(math.floor(-GRAPH_SIZE/2), math.floor(GRAPH_SIZE/2)+1):
   forward_to_position(i, math.sin(math.radians(i-PHASE_SHIFT))*(GRAPH_SIZE/4))

input("Press Enter to continue...")

penup()
forward_to_position(0, 0)
clear()
bgcolor("black")
pencolor("orange red")

for i in range(GRAPH_SIZE*4):
   if(i % 10 == 0):
      dot()
   i_rad = math.radians(i)
   forward_to_position(math.sin(i_rad) * (i/8), math.cos(i_rad) * (i/8))

print("Final position: ", position())
print("Absolute position: ", abs(position()))
input("Press Enter to exit...")
