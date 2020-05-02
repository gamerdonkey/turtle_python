import math
import svg
import sys

from turtle import *

speed(1)
bgcolor("black")
pencolor("orange")

def go_to_coord(dest_x, dest_y, draw = True):
   dest_y = -dest_y

   delta_x = dest_x - xcor()
   delta_y = dest_y - ycor()

   if(abs(delta_x) < 1 and abs(delta_y) < 1):
      return

   if draw:
      pendown()
   else:
      penup()
   setheading(math.degrees(math.atan2(delta_y, delta_x)) % 360)
   forward(math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2)))
   
def draw_svg(svg_filename, centered = True):
   f = svg.parse(svg_filename)

   (min_point, max_point) = f.bbox()
   (width, height) = (min_point + max_point).coord()
   x_centering_adj = width / 2
   y_centering_adj = height / 2
   
   for item in f.flatten():
      if(hasattr(item, 'segments')):
         for segment in item.segments(20):
            x, y = segment[0].coord()

            if(centered):
               x = x - x_centering_adj
               y = y - y_centering_adj

            go_to_coord(x, y, False)

            for point in segment[1:]:
               x, y = point.coord()

               if(centered):
                  x = x - x_centering_adj
                  y = y - y_centering_adj

               go_to_coord(x, y)
               
   go_to_coord(0, 0, False)

if(len(sys.argv) < 2):
   print("One arg required for SVG filename: %s <file.svg>" % sys.argv[0])
   exit(1)



while(True):
   go_to_coord(0, 0, False)
   input("Enter to start...")
   draw_svg(sys.argv[1], centered=True)
   input("Press Enter to exit...")
   clearscreen()
