from turtle import Turtle, Screen

t = Turtle()
t.speed(1)
window = Screen()

height = 200
width = 400
roof_height = 150

#house
t.goto(0, 0)
t.pendown()
t.pensize(4)
t.pencolor("black")
t.goto(0,  height)
t.goto(width, height)
t.goto(width, 0)
t.goto(0,0)

#roof
t.penup()
t.pencolor("red")
t.goto(-10, height)
t.pendown()
t.goto( width/2, height + roof_height)
t.goto(width + 10, height)
t.goto(-10, height)

#door
door_width = 40
door_height = 100
door_distance = 100
t.penup()
t.pensize(3)
t.pencolor("yellow")
t.goto( door_distance, 0)
t.pendown()
t.goto(door_distance, door_height)
t.goto(door_distance + door_width, door_height)
t.goto(door_distance + door_width, 0)

#window
window_width = 80
window_height = 50
window_to_left = door_distance + door_width + 100
window_to_bottom = 90
t.penup()
t.pensize(2)
t.goto(window_to_left, window_to_bottom)
t.pendown()
t.pencolor("blue")
t.goto(window_to_left, window_to_bottom + window_height)
t.goto(window_to_left + window_width, window_to_bottom + window_height)
t.goto(window_to_left + window_width, window_to_bottom)
t.goto(window_to_left, window_to_bottom)
t.hideturtle()
