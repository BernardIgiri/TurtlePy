#!/usr/bin/env python3
import turtle

turtle.setup(500, 500)
move = turtle.Turtle()
window = move.getscreen()
window.title("TurtlePy")
canvas = window.getcanvas()
text = (
    "Press Q to quit.\n"
    "Press arrow keys to move cursor.\n"
    "Press spacebar to toggle if the pen is up or down."
)
canvas.create_text(0, -205, text=text, fill="black", font=('Helvetica 15'))
canvas.pack()

move.speed(0)
move.color("red")
move.penup()

def draw(direction):
    move.setheading(direction)
    move.forward(1)
def onQ():
    window.bye()
def onToggle():
    if move.isdown():
        move.color("red")
        move.penup()
    else:
        move.color("green")
        move.pendown()
def onUp():
    draw(90)
def onDown():
    draw(270)
def onLeft():
    draw(180)
def onRight():
    draw(0)

turtle.onkeypress(onQ, "q")
turtle.onkeypress(onToggle, "space")
turtle.onkey(onUp, "Up")
turtle.onkey(onDown, "Down")
turtle.onkey(onLeft, "Left")
turtle.onkey(onRight, "Right")

turtle.listen()
turtle.mainloop()
