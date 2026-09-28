import turtle as trtl
wn = trtl.Screen()
painter = trtl.Turtle()

#List of colors
color = ["Green", "Orange", "Ivory", "Black", "DarkOliveGreen", "Blue", "Blue4",]

#Draw background
painter.penup()
painter.pencolor(color[0])
painter.fillcolor(color[0])
painter.goto(-400,-400)
painter.pendown()
painter.begin_fill()

for step in range (4):
    painter.forward(800)
    painter.left(90)
painter.end_fill()

#Draw river
painter.penup()
painter.goto(-400,50)
painter.pencolor(color[5])
painter.fillcolor(color[5])
painter.pendown()
painter.begin_fill()

for step in range (2):
    painter.forward(800)
    painter.left(90)
    painter.forward(100)
    painter.left(90)
painter.end_fill()

#Draw waves
painter.penup()




wn.mainloop()