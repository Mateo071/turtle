from turtle import Turtle, Screen
from random import randint

square =  Turtle()
square.shape("circle")
square.fillcolor("green")
square.pencolor("brown")

dotted_line = Turtle()
dotted_line.shape("square")
dotted_line.color("blue")

diff_shapes = Turtle()
diff_shapes.shape("circle")

colors = ["black", "slate gray", "alice blue", "cornflower blue", "blue", "powder blue", "teal", "lime", "dark red", "yellow", "dark orange", "indian red", "medium slate blue", "deep pink"]

square.up()
square.goto(-500, 45)
square.down()
for sides in range(4):
  square.forward(90)
  square.right(90)

dotted_line.up()
dotted_line.goto(-100,-100)
dotted_line.down()
dotted_line.left(45)
for step in range(20):
  dotted_line.forward(10)
  dotted_line.up()
  dotted_line.forward(10)
  dotted_line.down()

diff_shapes.up()
diff_shapes.goto(100, 200)
diff_shapes.down()
for shapes in range(3, 11):
  diff_shapes.pencolor(colors[randint(0, len(colors) - 1)])
  for shape in range(shapes):
    diff_shapes.forward(100)
    diff_shapes.right(360/shapes)

screen = Screen()
screen.exitonclick()