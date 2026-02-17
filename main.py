from turtle import*

t = Turtle()
t.color('red')
t.pensize(5)
t.shape('circle')
t.pendown()
t.speed(3)

def draw(x,y):
    t.goto(x,y)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def setGreen():
    t.color('green')

def setBlue():
    t.color('blue')

def setYellow():
    t.color('yellow')

def setViolet():
    t.color('violet')

def setTan():
    t.color('tan')

def setPurple():
    t.color('purple')

def setOlive():
    t.color('olive')

def setRed():
    t.color('red')

def stepRight():
    t.goto(t.xcor() + 5, t.ycor())

def stepLeft():
    t.goto(t.xcor() - 5,t.ycor())

def stepUp():
    t.goto(t.xcor(), t.ycor() + 5)

def stepDown():
    t.goto(t.xcor(), t.ycor() - 5)

def beginffff():
    t.begin_fill()

def endffff():
    t.end_fill()

scr = t.getscreen()
scr.onscreenclick(move)
scr.listen()
scr.onkey(setGreen, 'g')
scr.onkey(setBlue, 'b')
scr.onkey(setYellow, 'y')
scr.onkey(setViolet, 'v')
scr.onkey(setTan, 't')
scr.onkey(setPurple, 'p')
scr.onkey(setOlive, 'o')
scr.onkey(setRed, 'r')
scr.onkey(stepRight, 'Right')
scr.onkey(stepLeft, 'Left')
scr.onkey(stepUp, 'Up')
scr.onkey(stepDown, 'Down')
scr.onkey(beginffff, 'i')
scr.onkey(endffff, 'e')

t.ondrag(draw)
