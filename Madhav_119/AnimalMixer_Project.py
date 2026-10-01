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
    painter.pencolor(color[7])
    painter.fillcolor(color[7])
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
animal_choice = ["tiger", "turtle", "rabbit",]
start_choice = ["y", "n",]

start_answer = trtl.textinput("Start Program","You are an animal scientist in the Amazon Rainforest and you reported an interesting 3-way animal breed in your region. Would you like to describe it to us? Yes(y) or No(n)")
while start_answer not in start_choice:
    start_answer = trtl.textinput("Invalid start choice", "y or n")
if (start_answer == "y"):
    painter.penup()
    painter.goto(-500,0)
   
    #head select
    head_select = trtl.textinput("Head of animal","Ok, what did the head of the animal look most like, a tiger, turtle, or rabbit?")
    while head_select not in animal_choice:
        head_select = trtl.textinput("Invalid input", "The options were tiger, turtle, and rabbit, please select one")
    
    #body select
    body_select = trtl.textinput("Body of animal","Now, what did the body of the animal look like, a tiger, turtle, or rabbit?")
    while body_select not in animal_choice:
        body_select = trtl.textinput("Invalid input", "The options were tiger, turtle, and rabbit, please select one")
    while (body_select == head_select):
        body_select = trtl.textinput("Repeat input", "Remember, it's a 3-way breed, don't pick the same one twice, tiger, turtle, or rabbit?")
        while body_select not in animal_choice:
            body_select = trtl.textinput("Invalid under repeat", "tiger, turtle, or rabbit. And remember, no repeats.")
    
    #tail select
    tail_select = trtl.textinput("Tail of animal","Finally, what did the tail of the animal look like, a tiger, turtle, or rabbit?")
    while tail_select not in animal_choice:
        tail_select = trtl.textinput("Invalid input", "The options were tiger, turtle, and rabbit, please select one")
    while (tail_select == head_select):
        tail_select = trtl.textinput("Repeat input", "Remember, it's a 3-way breed, don't pick the same one twice, tiger, turtle, or rabbit?")
        while tail_select not in animal_choice:
            tail_select = trtl.textinput("Invalid under repeat", "tiger, turtle, or rabbit. And remember, no repeats.")
        while (tail_select == body_select):
            tail_select = trtl.textinput("Repeat under repeat", "tiger, turtle, or rabbit. And remember, no repeats.")
            while tail_select not in animal_choice:
                body_select = trtl.textinput("Invalid under repeat", "tiger, turtle, or rabbit. And remember, no repeats.")
    while (tail_select == body_select):
        tail_select = trtl.textinput("Repeat input", "Remember, it's a 3-way breed, don't pick the same one twice, tiger, turtle, or rabbit?")
        while tail_select not in animal_choice:
            body_select = trtl.textinput("Invalid under repeat", "tiger, turtle, or rabbit. And remember, no repeats.")
        while (tail_select == head_select):
            tail_select = trtl.textinput("Repeat under repeat", "tiger, turtle, or rabbit. And remember, no repeats.")
            while tail_select not in animal_choice:
                body_select = trtl.textinput("Invalid under repeat", "tiger, turtle, or rabbit. And remember, no repeats.")
    #generate animal
    if (head_select == "tiger" and body_select == "turtle" and tail_select == "rabbit"):
        wn.addshape("ti-tu-r.gif")
        painter.shape("ti-tu-r.gif")
        painter.speed(1)
        painter.forward(500)
        painter.stamp()
    if (head_select == "tiger" and body_select == "rabbit" and tail_select == "turtle"):
        wn.addshape("ti-r-tu.gif")
        painter.shape("ti-r-tu.gif")
        painter.speed(1)
        painter.forward(500)
        painter.stamp()
    if (head_select == "turtle" and body_select == "tiger" and tail_select == "rabbit"):
        wn.addshape("tu-ti-r.gif")
        painter.shape("tu-ti-r.gif")
        painter.goto(-500,-30)
        painter.speed(1)
        painter.forward(500)
        painter.stamp()
    if (head_select == "turtle" and body_select == "rabbit" and tail_select == "tiger"):
        wn.addshape("tu-r-ti.gif")
        painter.shape("tu-r-ti.gif")
        painter.goto(-500,-30)
        painter.speed(1)
        painter.forward(500)
        painter.stamp()
    if (head_select == "rabbit" and body_select == "turtle" and tail_select == "tiger"):
        wn.addshape("r-tu-ti.gif")
        painter.shape("r-tu-ti.gif")
        painter.goto(-500,-30)
        painter.speed(1)
        painter.forward(500)
        painter.stamp()
    if (head_select == "rabbit" and body_select == "tiger" and tail_select == "turtle"):
        wn.addshape("r-ti-tu.gif")
        painter.shape("r-ti-tu.gif")
        painter.goto(-500,-30)
        painter.speed(1)
        painter.forward(500)
        painter.stamp()
else:
    wn.bye

wn.mainloop()