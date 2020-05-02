import math
import svg
import sys
import turtle

from multiprocessing import Process

#speed(1)
#bgcolor("black")
#pencolor("orange")

def go_to_coord(turtle, dest_x, dest_y, draw = True):
   dest_y = -dest_y

   delta_x = dest_x - turtle.xcor()
   delta_y = dest_y - turtle.ycor()

   if(abs(delta_x) < 1 and abs(delta_y) < 1):
      return

   if draw:
      turtle.pendown()
   else:
      turtle.penup()
   turtle.setheading(math.degrees(math.atan2(delta_y, delta_x)) % 360)
   turtle.forward(math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2)))

def draw_segment(t, segment, x_centering_adj, y_centering_adj, centered = True):
   print("Thread started")

   x, y = segment[0].coord()

   if(centered):
      x = x - x_centering_adj
      y = y - y_centering_adj

   go_to_coord(t, x, y, False)

   for point in segment[1:]:
      x, y = point.coord()

      if(centered):
         x = x - x_centering_adj
         y = y - y_centering_adj

      go_to_coord(t, x, y)
   
   
def draw_svg(svg_filename, centered = True):
   f = svg.parse(svg_filename)

   (min_point, max_point) = f.bbox()
   (width, height) = (min_point + max_point).coord()
   x_centering_adj = width / 2
   y_centering_adj = height / 2
   
   screen = turtle.Screen()
   turtles = []
   processes = []

   for item in f.flatten():
      if(hasattr(item, 'segments')):
         segments = item.segments(20)
         for segment in segments:
            print("doing a segment")
            turtles.append(turtle.Turtle())
            new_process = Process(target = draw_segment, args = (turtles[-1], segment, x_centering_adj, y_centering_adj))
            print("created process")
            new_process.start()
            print("started process")
            processes.append(new_process)
            print("added process to processes")

   for process in processes:
      process.join()

   screen.mainloop()
   input("waiting...")

if(len(sys.argv) < 2):
   print("One arg required for SVG filename: %s <file.svg>" % sys.argv[0])
   exit(1)



draw_svg(sys.argv[1], centered=True)
input("Press Enter to exit...")
