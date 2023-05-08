import turtle

import time
import random
fast = 0.15

window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('lightblue')

window.setup(width=600, height=600)
window.tracer(0)

head = turtle.Turtle
head.speed(0)
head.shape('square')
head.color('black')
head.penup()
head.goto(0, 100)
head.direction='stop'

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.80, 0.80)
food.goto(0, 0)

Tail = []
Point = 0

write = turtle.Turtle()
write.speed(0)
write.shape("square")
write.color("white")
write.penup()
write.hideturtle()
write.goto(0, 260)
write.write("Point: {}".format(Point), align="center", font=("Courier", 24, "normal"))

if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)
 
        new_Tail = turtle.Turtle()
        new_Tail.speed(0)
        new_Tail.shape("square")
        new_Tail.color("white")
        new_Tail.penup()
new_Tail.append(new_Tail)
 

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
 
 
 
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"


window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_right, "Right")
window.onkey(go_left, "Left")

while True:
    window.update()

if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
 
        for Tail in Tail:
            Tail.goto(1000, 1000)
        Tail = []
 
        Point = 0
        delay = 0.1
 
        write.clear()
        write.write("Point: {}".format(Point), align="center", font=("Courier", 24, "normal"))
   

if kafa.distance(food)<20:
     x = random.randint(-250, 250)
     y = random.randint(-250, 250)
     food.goto(x, y)

new_Tail = turtle.Turtle()
new_Tail.speed(0)
new.Tail.shape("square")
new_Tail.color("white")
new_Tail.penup()
Tail.append(new_Tail)
 
for index in range(len(Tail) - 1, 0, -1):
        x = Tail[index - 1].xcor()
        y = Tail[index - 1].ycor()
        Tail[index].goto(x, y)
 
if len(Tail) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        Tail[0].goto(x, y)

        move()
time.sleep(fast)