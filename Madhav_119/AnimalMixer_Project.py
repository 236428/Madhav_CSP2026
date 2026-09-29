import turtle as trtl
wn = trtl.Screen()
painter = trtl.Turtle()

#List of colors
color = ["Green", "Orange", "Ivory", "Black", "DarkOliveGreen", "Blue", "Blue4","chartreuse4", "chocolate4",]
##########

#Draw background
painter.speed(0)
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
###########

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
###########

#Draw waves
for step in range(2):
    painter.penup()
    painter.forward(100)
    painter.left(90)
    painter.forward(30)
    painter.right(90)
    painter.pendown()
    painter.pencolor(color[6])
    painter.pensize(8)
    painter.forward(100)
painter.penup()
painter.forward(100)
painter.right(90)
painter.forward(50)
painter.left(90)
painter.pendown()
painter.pencolor(color[6])
painter.pensize(8)
painter.forward(100)

painter.penup()
painter.forward(30)
painter.left(90)
painter.forward(70)
painter.right(90)
painter.pendown()
painter.pencolor(color[6])
painter.pensize(8)
painter.forward(100)
##########

#Draw Trees
def draw_trees():
    painter.penup()
    painter.pencolor(color[8])
    painter.fillcolor(color[8])
    painter.pendown()
    painter.begin_fill()
    painter.forward(60)
    painter.left(90)
    painter.forward(120)
    painter.left(90)
    painter.forward(60)
    painter.left(90)
    painter.forward(120)
    painter.end_fill()
    painter.penup()
    painter.left(180)
    painter.forward(120)
    painter.right(90)
    painter.forward(30)
    painter.pencolor("chartreuse4")
    painter.fillcolor("chartreuse4")
    painter.pendown()
    painter.begin_fill()
    painter.circle(40)
    painter.end_fill()
    painter.penup()
    painter.forward(50)
    painter.pendown()
    painter.begin_fill()
    painter.circle(40)
    painter.end_fill()
    painter.penup()
    painter.left(180)
    painter.forward(90)
    painter.left(180)
    painter.pendown()
    painter.begin_fill()
    painter.circle(40)
    painter.end_fill()
    painter.penup()
    painter.forward(41)
    painter.left(90)
    painter.forward(50)
    painter.right(90)
    painter.pendown()
    painter.begin_fill()
    painter.circle(40)
    painter.end_fill()
    painter.penup()

painter.penup()
painter.goto(-300,-300)
painter.pendown()
draw_trees()
painter.goto(250,-200)
painter.pendown()
draw_trees()
painter.goto(-300,200)
for step in range (4):
    painter.pendown()
    draw_trees()
    painter.right(90)
    painter.forward(170)
    painter.left(90)
    painter.forward(150)


#Introduce task to player
start_answer = trtl.textinput("Start Program","You are an animal scientist in the Amazon Rainforest and you reported an interesting animal in your region. Would you like to describe it to us? Yes(y) or No(n)")
if (start_answer == "y"):
    painter.penup()
    painter.goto(0,0)
else:
    wn.bye

wn.mainloop()