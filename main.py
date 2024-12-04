import turtle
from turtle import Turtle, Screen
from random import choice, randint
turtle.colormode(255)

square =  Turtle()
square.shape("turtle")
square.fillcolor("green")
square.pencolor("brown")

dotted_line = Turtle()
dotted_line.shape("square")
dotted_line.color("blue")

diff_shapes = Turtle()
diff_shapes.shape("circle")

walk = Turtle()
walk.shape("arrow")

directions = [0, 90, 180, 270]

square.up()
square.goto(-500, 45)
square.down()
for sides in range(4):
  square.forward(90)
  square.right(90)

dotted_line.up()
dotted_line.goto(-350,-100)
dotted_line.down()
dotted_line.left(45)
for step in range(20):
  dotted_line.forward(10)
  dotted_line.up()
  dotted_line.forward(10)
  dotted_line.down()

diff_shapes.up()
diff_shapes.goto(0, 200)
diff_shapes.down()
for shapes in range(3, 11):
  diff_shapes.pencolor((randint(0, 255), randint(0, 255), randint(0,255)))
  for shape in range(shapes):
    diff_shapes.forward(100)
    diff_shapes.right(360/shapes)

walk.up()
walk.goto(250, 0)
walk.down()
walk.speed(8)
walk.pensize(5)
for step in range(200):
  walk.pencolor((randint(0, 255), randint(0, 255), randint(0,255)))
  walk.setheading(choice(directions))
  walk.forward(10)

screen = Screen()
screen.exitonclick()