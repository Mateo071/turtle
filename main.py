import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)

directions = [0, 90, 180, 270]

def random_color():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  return (r, g, b)

def square():
  square =  Turtle()
  square.shape("turtle")
  square.fillcolor("green")
  square.pencolor("brown")

  square.speed(10)
  square.up()
  square.goto(-500, 45)
  square.down()
  for _ in range(4):
    square.forward(90)
    square.right(90)

def dotted_line():
  dotted_line = Turtle()
  dotted_line.shape("square")
  dotted_line.color("blue")

  dotted_line.speed(10)
  dotted_line.up()
  dotted_line.goto(-350,-100)
  dotted_line.down()
  dotted_line.left(45)
  for step in range(20):
    dotted_line.forward(10)
    dotted_line.up()
    dotted_line.forward(10)
    dotted_line.down()

def diff_shapes():
  diff_shapes = Turtle()
  diff_shapes.shape("circle")
  
  diff_shapes.speed(10)
  diff_shapes.up()
  diff_shapes.goto(0, 200)
  diff_shapes.down()
  for shapes in range(3, 11):
    diff_shapes.pencolor(random_color())
    for shape in range(shapes):
      diff_shapes.forward(100)
      diff_shapes.right(360/shapes)

def walk():
  walk = Turtle()
  walk.shape("arrow")

  walk.speed(0)
  walk.up()
  walk.goto(250, 0)
  walk.down()
  walk.speed(8)
  walk.pensize(5)
  for step in range(200):
    walk.pencolor(random_color())
    walk.setheading(choice(directions))
    walk.forward(10)

def spirograph(num_of_circles):
  spirograph = Turtle()
  spirograph.shape("triangle")
  spirograph.pensize(2)

  spirograph.speed(0)
  spirograph.up()
  spirograph.goto(500, 0)
  spirograph.down()

  rotation = int(360/num_of_circles)
  for circle in range(num_of_circles):
    spirograph.pencolor(random_color())
    spirograph.circle(100, None, None)
    spirograph.left(rotation)


while True:
  shape = int(input("What would you like to see? Please select one of the following by typing the corresponding number:\n\n1. Square\n2. Dotted Line\n3.Different Shapes\n4. Walk\n5. Spirograph\n>"))

  if shape == 1:
    square()
  elif shape == 2:
    dotted_line()
  elif shape == 3:
    diff_shapes()
  elif shape == 4:
    walk()
  elif shape == 5:
    spirograph(72)
  else:
    print("Please select a valid option.\n")

