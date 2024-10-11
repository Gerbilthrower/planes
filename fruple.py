#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
x = trtl.Turtle()
x.pensize(40)
x.circle(20)
w = 6
y = 70
z = 360 / w
x.pensize(5)
n = 0
while (n < w):
  x.penup()
  x.goto(0,0)
  x.setheading(z*n)
  x.pendown()
  x.circle(200,30)
  n = n + 0.8
x.hideturtle()
x.penup()
x.goto(0,0)
x.forward(10)
x.pendown()
x.pencolor("white")
x.pensize(15)
x.forward(1)
x.penup()
x.goto(0,0)
x.forward(-10)
x.pendown()
x.pencolor("white")
x.forward(1)
wn = trtl.Screen()
wn.mainloop()
