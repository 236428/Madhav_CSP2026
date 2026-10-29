#Setup
import turtle as trtl
import turtle as t
import turtle as T
import turtle as tu
import random as rand
block1 = t.Turtle()
block2 = T.Turtle()
block3 = tu.Turtle()
from playsound3 import playsound

#Import the lava/volcano background
wn = trtl.Screen()
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
Lvl1 = ["bird","blue","book","cat","dog","fish","frog","hand","house","jump","milk","red","stop","sun","tree"]
Lvl2 = []
Lvl3 = []

#Get audio files for each of the words
audio1 = ["bird.mp3","blue.mp3","book.mp3","cat.mp3","dog.mp3","fish.mp3","frog.mp3","hand.mp3","house.mp3","jump.mp3","milk.mp3","red.mp3","stop.mp3","sun.mp3","tree.mp3"]



#Add user input to ask what the user’s name is, store it for later
Uname = trtl.textinput("User Name", "Please enter your name")

#Add one more input to ask if user is ready, if yes pull a random word from list 1
Start = trtl.textinput("Ready", "This is a spelling bee game, you have three lives and the words will get progressively harder, if you are ready to hear the first word, enter: r")
if (Start == "r"):
    index = rand.randrange(len(Lvl1))
    #Each word should have its own if statement where if it is pulled, the designated audio plays
    playsound(audio1[index])
    #Audio plays to the user and then one more user input asks “do you want to hear it again(a)? If not type in your answer”
    answer = trtl.textinput("Word", "If you want to hear the word again, type any single letter, if not enter your answer")
    if (answer < len(2)):
        playsound(audio1[index])
        answer = trtl.textinput("Word", "Now enter your answer")
        
    if (answer != Lvl1[index]):
        block1.hideturtle()
        block2.goto(0,-250)
        block3.goto(0,-100)
    Lvl1.pop(index)

#Add if statement, if answer is “a” play the audio, if not it will accept the given input as the answer


#One more if statement check if the answer input is spelled correctly


#If false then erase one block from the tower


#put this all into a loop, that runs five times and does same thing for the second word bank and for the third bank 


#Make it so that every time a word is pulled it is also popped from the list so you don’t get it twice


#Once that is working for all three word banks, add the character turtle to the block tower


#Add in code that drops the character by the height of the block when a block is erased


#When character drops down from the final block, it should  disappear and print “You Lose” and their score as well


#If a player gets past all 3 levels of questions, and doesn’t lose then print “You Win” and their score.


#(OPTIONAL) Add a user input at the very beginning asking the user what character it wants to pick

wn.mainloop()
