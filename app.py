from turtle import *
import random
# content color
# color("red")

# begin_fill()
# increase pen size
# dot(20)
# pencolor("blue")
# change background color
bgcolor("pink")
# for changing speed
# speed(2)
# change title
title("My Turtle Program")
# cloning turtle 
clone()
player_one = Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.shapesize(1)
player_one.penup()
player_one.goto(-300, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-300,-100)


player_one.goto(300, 60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-300, 100)

player_two.goto(300, -140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-300, -100)


random_list = [1,2,3,4,5,6]


for i in range(20):
    if player_one.pos() >= (300,100):
        print("Player One Wins!!")
        break
    elif player_two.pos() >= (300, -100):
        print("Player Two Wins!!")
        break
    else:
        player_one_turn = input("Press 'Enter' to roll the die for 1st player ")
        player_one_die = random.choice(random_list)
        print("The result of the die roll is: ")
        print(player_one_die)
        print("The number of steps will be: ")
        print(20*player_one_die)
        player_one.forward(20*player_one_die)
        
        if player_one.pos() < (300,100):



            player_two_turn = input("Press 'Enter' to roll the die for 2nd player ")
            player_two_die = random.choice(random_list)
            print("The result of the die roll is: ")
            print(player_two_die)
            print("The number of steps will be: ")
            print(20*player_two_die)
            player_two.forward(20*player_two_die)

        







done()





