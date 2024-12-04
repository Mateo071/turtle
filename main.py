from turtle import Turtle, Screen

ellen =  Turtle()
ellen.shape("turtle")
ellen.fillcolor("green")
ellen.pencolor("brown")

for sides in range(4):
  ellen.forward(90)
  ellen.right(90)


screen = Screen()
screen.exitonclick()