

import pyttsx3
engine = pyttsx3.init()
engine.say("hello   welcome   to   this  program  .. you must to say a word .., rock  ,,   paper   , or  scissors  . ")
engine.runAndWait()
print("__________________________________")
import random

# print("hello welcome to this program ")
x = random.randint(0, 2)
# import pyttsx3
# engine = pyttsx3.init()
# engine.say( x*2)
# engine.runAndWait()
# در اینجا به این کار را به عهده سیستم گذاشتیم و سیستم از 1 تا 2 هر عددی را که خواست میگوید
# print(x*2)
rock = 0
paper = 1
scissors = 2
engine = pyttsx3.init()
engine.say ("say please!")  
engine.runAndWait() 
player1 = input('=>>>>>>   ')
player2 = x
if x == 0:
    engine = pyttsx3.init()
    engine.say("rock")
    engine.runAndWait()
    print("rock")
elif x == 1:
    engine = pyttsx3.init()
    engine.say("paper")
    engine.runAndWait()
    print("paper")
elif x == 2:
    engine = pyttsx3.init()
    engine.say("scissors")
    engine.runAndWait()
    print("scissors")


if player1 == "rock" and player2 == 0:
    print("thats a tie ...")
elif player1 == "rock" and player2 == 1:
    print('player2 wins ...')
elif player1 == "rock" and player2 == 2:
    print('player1 wins ...')
if player1 == "paper" and player2 == 0:
    print("player1 wins ...")
elif player1 == "paper" and player2 == 1:
    print('thats a tie ...')
elif player1 == "paper" and player2 == 2:
    print('player2 wins...')
if player1 == "scissors" and player2 == 0:
    print("player2 wins....")
elif player1 == "scissors" and player2 == 1:
    print('player1 wins....')
elif player1 == "scissors" and player2 == 2:
    print('thats a tie.....')


engine = pyttsx3.init()
engine.say("do you  want   to play again???????")
engine.runAndWait()

w = input()
no='no'
yes="yes"
if w == no :
    for  k in range(1):
        engine = pyttsx3.init()
        engine.say("ok ,      so  you  are agree to finish  the  game.")
        engine.runAndWait()
        print("-----------------------------------") 
        engine = pyttsx3.init()
        engine.say ("editer  ,, by  parsa  sarkhosh")  
        print("editer,, by  parsa  sarkhosh")
        engine.runAndWait() 
        break
        # print(k)
elif w != no and  w == yes:
    engine = pyttsx3.init()
    engine.say("ok   so  lets play again")
    engine.runAndWait()
    print('----------------------')
    y = random.randint(1, 3)
    engine = pyttsx3.init()
    engine.say ("say please!")  
    engine.runAndWait() 
    
    player1=input('=>>>>>>   ')
    player3 = y
    if y == 1:
        engine = pyttsx3.init()
        engine.say("rock")
        engine.runAndWait()
        print("rock")
    elif y == 2:
        engine = pyttsx3.init()
        engine.say("paper")
        engine.runAndWait()
        print("paper")
    elif y == 3:
        engine = pyttsx3.init()
        engine.say("scissors")
        engine.runAndWait()
        print("scissors")
    if player1 == "rock" and player3 == 1:
        print("thats a tie ...")
    elif player1 == "rock" and player3 == 2:
        print('player2 wins ...')
    elif player1 == "rock" and player3 == 3:
        print('player1 wins ...')
    if player1 == "paper" and player3 == 1:
        print("player1 wins ...")
    elif player1 == "paper" and player3 == 2:
        print('thats a tie ...')
    elif player1 == "paper" and player3 == 3:
        print('player2 wins...')
    if player1 == "scissors" and player3 == 1:
        print("player2 wins....")
    elif player1 == "scissors" and player3 == 2:
        print('player1 wins....')
    elif player1 == "scissors" and player3 == 3:
        print('thats a tie.....')
    engine = pyttsx3.init()
    engine.say("  do you want to play again???????")
    engine.runAndWait()
    
    ve=input()
    r="yes"
    c='no'

    if ve == c :
        for  p in range(1):
            engine = pyttsx3.init()
            engine.say(" ok  goood  ")
            engine.runAndWait()
            print("-----------------------------------") 
            engine = pyttsx3.init()
            engine.say ("editer  ,, by  parsa  sarkhosh")  
            print("editer by , parsa  sarkhosh")
            engine.runAndWait() 
            break
        # print(k)
    elif ve != c and  w == r:
        engine = pyttsx3.init()
        engine.say("  very  bad,,    we play alot   ,but ,   if you say , lets  play again")
        engine.runAndWait()
        print("----------------------")
        p = random.randint(2, 4)
        engine = pyttsx3.init()
        engine.say ("say please!")  
        engine.runAndWait() 
    
        player1=input('=>>>>>>>   ')
        player4 = p
        if p == 2:
            engine = pyttsx3.init()
            engine.say("rock")
            engine.runAndWait()
            print("rock")
        elif p == 3:
            engine = pyttsx3.init()
            engine.say("paper")
            engine.runAndWait()
            print("paper")
        elif p == 4:
            engine = pyttsx3.init()
            engine.say("scissors")
            engine.runAndWait()
            print("scissors")
        if player1 == "rock" and player4 == 2:
            print("thats a tie ...")
        elif player1 == "rock" and player4 == 3:
            print('player2 wins ...')
        elif player1 == "rock" and player4 == 4:
            print('player1 wins ...')
        if player1 == "paper" and player4 == 2:
            print("player1 wins ...")
        elif player1 == "paper" and player4 == 3:
            print('thats a tie ...')
        elif player1 == "paper" and player4 == 4:
            print('player2 wins...')
        if player1 == "scissors" and player4 == 2:
            print("player2 wins....")
        elif player1 == "scissors" and player4 == 3:
            print('player1 wins....')
        elif player1 == "scissors" and player4 == 4:
            print('thats a tie.....')

        engine = pyttsx3.init()
        engine.say(" we   played   the last  game    ..    , and    it   was   good")
        engine.runAndWait() 
        print("-----------------------------------") 
        engine = pyttsx3.init()
        engine.say ("editer  ,, by  parsa  sarkhosh")  
        print("editer by , parsa  sarkhosh")
        engine.runAndWait() 
        

