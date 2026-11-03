#Setup
import turtle as trtl
import random as rand
from playsound3 import playsound

block1 = trtl.Turtle()
block2 = trtl.Turtle()
block3 = trtl.Turtle()
writer = trtl.Turtle()

round = 0
score = 0
block_num = 3
font_setup = ("Arial", 40, "normal")
def update_spotscore(x,y):
  global score
  score += 1
  writer.write(score, font=font_setup)

def update_block():
    global block_num
    block_num -= 1

def update_round():
    global round
    round += 1
    

writer.penup()
writer.hideturtle()
writer.goto(-10,320)
writer.write(score, font= ("Arial", 40, "normal"))

#Import the lava/volcano background
wn = trtl.Screen()
wn.title("Volcanic Spelling")
wn.setup(width=1.0, height=1.0)
wn.bgpic("lava_background.gif")

#Draw the blocks the character is standing on
wn.addshape("obsidian_block.gif")
block1.penup()
block1.shape("obsidian_block.gif")
block1.goto(0,-250)

block2.penup()
block2.shape("obsidian_block.gif")
block2.goto(0,-100)

block3.penup()
block3.shape("obsidian_block.gif")
block3.goto(0,50)



#Make 3 sets of lists for each “difficulty” of the game
Lvl1 = ["bird","blue","book","cat","dog","fish","frog","hand","house","jump","milk","red","stop","tree"]
Lvl2 = ["believe","calendar","collect","definitely","different","friend","library","receive","until"]
Lvl3 = []

#Get audio files for each of the words
audio1 = ["bird.mp3","blue.mp3","book.mp3","cat.mp3","dog.mp3","fish.mp3","frog.mp3","hand.mp3","house.mp3","jump.mp3","milk.mp3","red.mp3","stop.mp3","tree.mp3"]
audio2 = ["believe.mp3","calendar.mp3","collect.mp3","definitely.mp3","different.mp3","friend.mp3","library.mp3","receive.mp3","until.mp3"]


#Add user input to ask what the user’s name is, store it for later
Uname = trtl.textinput("User Name", "This is a spelling bee game, you have three lives and the words will get progressively harder, now please enter your name")
#writer.goto(-200, 350)
#writer.write("Level 1: Easy")

#Add one more input to ask if user is ready, if yes pull a random word from list 1
for step in range (3):
    update_round()
    if (block_num < 1):
        writer.clear()
        writer.goto(-170,300)
        writer.write("YOU LOSE", font= ("Arial", 50, "normal"))
        writer.goto(-240,-275)
        writer.write(f"{Uname}'s Score: {score}", font= ("Arial", 50, "normal"))
        break


    Start = trtl.textinput("Ready", "if you are ready to hear the word, enter anything in")
    if (len(Start) > 0):
        index = rand.randrange(len(Lvl1))
        index2 = index
     
#Each word should have its own if statement where if it is pulled, the designated audio plays
        playsound(audio1[index])
#Audio plays to the user and then one more user input asks “do you want to hear it again(a)? If not type in your answer”
        answer = trtl.textinput("Word", "If you want to hear the word again, type any single letter, if not enter your answer")
        answer = answer.lower()
        if (len(answer) > 1):
            if (answer != Lvl1[index]):
                playsound("incorrectnoise.mp3")     
                if (block_num == 1):
                    block3.hideturtle()
                    update_block()
                if (block_num == 2):
                    block2.hideturtle()
                    block3.goto(0,-250)
                    update_block()
                if (block_num == 3):
                    block1.hideturtle()
                    block2.goto(0,-250)
                    block3.goto(0,-100)
                    update_block()
            if (answer == Lvl1[index]):
                writer.clear()
                update_spotscore(0,350)
                playsound("correctnoise.mp3")
                    
            Lvl1.pop(index)
            audio1.pop(index)
        
        if (len(answer) < 2):
            playsound(audio1[index])
            answer = trtl.textinput("Word", "Now enter your answer")
            answer = answer.lower()
            if (answer != Lvl1[index]):
                playsound("incorrectnoise.mp3")     
                if (block_num == 1):
                    block3.hideturtle()
                    update_block()
                if (block_num == 2):
                    block2.hideturtle()
                    block3.goto(0,-250)
                    update_block()
                if (block_num == 3):
                    block1.hideturtle()
                    block2.goto(0,-250)
                    block3.goto(0,-100)
                    update_block()            
            if (answer == Lvl1[index]):
                writer.clear()
                update_spotscore(0,350)
                playsound("correctnoise.mp3")

            Lvl1.pop(index)
            audio1.pop(index)

#writer.goto(-200, 350)
#writer.write("Level 2: Hard")

#Now do the same for LVL2
for step in range (3):
    if (block_num < 1):
        writer.clear()
        writer.goto(-170,300)
        writer.write("YOU LOSE", font= ("Arial", 50, "normal"))
        writer.goto(-240,-275)
        writer.write(f"{Uname}'s Score: {score}", font= ("Arial", 50, "normal"))
        break

    Start = trtl.textinput("Ready", "if you are ready to hear the word, enter anything in")
    if (len(Start) > 0):
        index = rand.randrange(len(Lvl2))
        index2 = index
     
#Each word should have its own if statement where if it is pulled, the designated audio plays
        playsound(audio2[index])
#Audio plays to the user and then one more user input asks “do you want to hear it again(a)? If not type in your answer”
        answer = trtl.textinput("Word", "If you want to hear the word again, type any single letter, if not enter your answer")
        answer = answer.lower()
        if (len(answer) > 1):
            if (answer != Lvl2[index]):
                playsound("incorrectnoise.mp3")     
                if (block_num == 1):
                    block3.hideturtle()
                    update_block()
                if (block_num == 2):
                    block2.hideturtle()
                    block3.goto(0,-250)
                    update_block()
                if (block_num == 3):
                    block1.hideturtle()
                    block2.goto(0,-250)
                    block3.goto(0,-100)
                    update_block()
            if (answer == Lvl2[index]):
                writer.clear()
                update_spotscore(0,350)
                playsound("correctnoise.mp3")
                    
            Lvl2.pop(index)
            audio2.pop(index)
        
        if (len(answer) < 2):
            playsound(audio2[index])
            answer = trtl.textinput("Word", "Now enter your answer")
            answer = answer.lower()
            if (answer != Lvl2[index]):
                playsound("incorrectnoise.mp3")     
                if (block_num == 1):
                    block3.hideturtle()
                    update_block()
                if (block_num == 2):
                    block2.hideturtle()
                    block3.goto(0,-250)
                    update_block()
                if (block_num == 3):
                    block1.hideturtle()
                    block2.goto(0,-250)
                    block3.goto(0,-100)
                    update_block()            
            if (answer == Lvl2[index]):
                writer.clear()
                update_spotscore(0,350)
                playsound("correctnoise.mp3")

            Lvl2.pop(index)
            audio2.pop(index)
    update_round()

writer.clear()
writer.goto(-170, 300)
writer.write("YOU WIN!", font= ("Arial", 50, "normal"))
writer.goto(-190,250)
writer.write(f"{Uname}'s Score: {score}", font= ("Arial", 30, "normal"))

#Once that is working for all three word banks, add the character turtle to the block tower


#Add in code that drops the character by the height of the block when a block is erased


#When character drops down from the final block, it should  disappear and print “You Lose” and their score as well


#If a player gets past all 3 levels of questions, and doesn’t lose then print “You Win” and their score.


#(OPTIONAL) Add a user input at the very beginning asking the user what character it wants to pick

wn.mainloop()
