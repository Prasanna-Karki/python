import turtle
import random
turtle.getscreen().bgcolor("black")
#starting position
player1=turtle.Turtle()
player1.color("green")
player1.shape("turtle")
player1.penup()
player1.goto(-200,100)
player2=player1.clone()
player2.color("red")
player2.penup()
player2.goto(-200,-100)
#finishing point
player1.goto(300,60)
player1.pendown()
player1.circle(40)
player1.penup()
player1.goto(-200,100)
player2.goto(300,-140)
player2.pendown()
player2.circle(40)
player2.penup()
player2.goto(-200,-100)
#game code
die=[1,2,3,4,5,6]

for i in range(20):
    if player1.pos() >= (300,100):
        print("player1 wins")
        break
    elif player2.pos()>=(300,-100):
        print("player2 wins")
        break
    else:
        player1_turn=input("press 'enter' to roll the dice")
        die_outcome=random.choice(die)
        print("the result of die is :",die_outcome)
        print("the no of steps will be :", 20*die_outcome)
        player1.fd(20*die_outcome)
        player2_turn=input("press 'enter' to roll the die")
        die_outcome2= random.choice(die)
        print("the result of the die is:", die_outcome2)
        print("the no. of steps will be:", 20*die_outcome2)
        player2.fd(20*die_outcome2)

