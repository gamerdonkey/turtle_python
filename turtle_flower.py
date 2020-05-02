import math
import random

from turtle import *

#speed(10)

while(True):
   if(abs(position()) == 0):
      right(36)
   left(2*(abs(position())/360))
   forward(3)
#1   forward((360-abs(position()))/45)

