from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("pong")

my_turtle = Turtle()
my_turtle.shape("square")


def move_forward():
    my_turtle.forward(20)


screen.onkey(move_forward, "Up")
screen.listen()

screen.exitonclick()
