# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:14:48 2020

@author: sushmita singh

"""

import turtle
import time
import random
delay = 0.2
score =0
high_score=0
'''set up the screen'''
wn= turtle.Screen()
wn.title('Snake game by:@SUSHMITA SINGH')
wn.bgcolor("silver")
wn.setup(width=600, height=600)
wn.tracer(0) #this turn of screeen updates

'''snake head'''
head = turtle.Turtle()
head.speed(0)
head.color("black")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction='stop'


'''list for snake body'''
segement=[]#use in main loop

'''score display '''
pen= turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()
pen.goto(0,280)
pen.shape("square")
pen.color("yellow")
pen.write("SCORE : 0  HIGHSCORE: 0", align="center" ,font=("Arial",10,"normal"))

'''snake food'''
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,200)
food.direction='stop'
food.shapesize(0.9)

'''function for change the direction of snake'''
def go_up():
    if head.direction!= "down":#if we are going down than can"t go up
        head.direction= "up"
def go_down():
    if head.direction!= "up":#if we are going up than can"t go up
        head.direction= "down"
def go_right():
    if head.direction!= "left":#if we are going right than can"t go up
        head.direction= "right"
def go_left():
    if head.direction!= "right":#if we are going left than can"t go up
        head.direction= "left"    


'''function for moving snake'''
def move():
    if head.direction=="up":
        y= head.ycor()
        head.sety(y + 20)
    if head.direction=="down":
        y= head.ycor()
        head.sety(y - 20)
    if head.direction=="left":
     x= head.xcor()
     head.setx(x - 20)
    if head.direction=="right":
        x= head.xcor()
        head.setx(x + 20)
        
        
'''keyboard binging:connects key press with particular function'''
wn.listen()#listen the key press
wn.onkeypress(go_up,"Up")#we can use "w"
wn.onkeypress(go_down,"Down")#we can use "s"
wn.onkeypress(go_right,"Right")#we can use "d"
wn.onkeypress(go_left,"Left")#we can use "a"


'''main game loop'''
while True:
    wn.update()
    
    '''check the collision of snake to the border'''
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
         time.sleep(0.1)
         head.goto(0,0)
         head.shape("square")
         head.direction="stop"
         
         for seg in segement:#hide the body
             seg.goto(10000,10000)
             
         segement.clear()# remove body from head
         score=0
         pen.clear()    
         pen.write(" SCORE : {}  HIGHSCORE: {}".format(score,high_score), align="center" ,font=("Arial",10,"normal"))#applying values to score
    '''check the collision of snake head to the body'''
    for seg in segement:
        if seg.distance(head)<20:
            time.sleep(0.1)
            head.goto(0,0)
            head.shape("square")
            head.direction="stop"
            
            for seg in segement:#hide the body
                seg.goto(10000,10000)
             
            segement.clear()# remove body from head   
             
            '''reset the score after collision'''
            score=0
            pen.clear()    
            pen.write(" SCORE : {}  HIGHSCORE: {}".format(score,high_score), align="center" ,font=("Arial",10,"normal"))#applying values to score
        
    '''check is the snake is come in contact with food'''
    if head.distance(food)<20:
        #move the food to a random spot when snake comes in contct
        x= random.randint(-270,270)
        y= random.randint(-270.,270)
        food.goto(x,y)
        
        '''making the body of snake'''
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("green")
        new_segment.penup()
        new_segment.shape("circle")
        segement.append(new_segment)
        
        '''shoten the delay time,increse the movement speed after every eat'''
        delay =delay-0.001
        
        '''increse score'''
        score += 10 
        if score> high_score:
            high_score= score# storing high score
        pen.clear()    
        pen.write(" SCORE : {}  HIGHSCORE: {}".format(score,high_score), align="center" ,font=("Arial",10,"normal"))#applying values to score
    
    '''move the end segement first in reverse order'''
    for index in range(len(segement)-1,0,-1):
        x=segement[index-1].xcor()
        y =segement[index-1].ycor()
        segement[index].goto(x,y)
   
    '''move he segement to the head.so to attach the body with head'''
    if len(segement)>0:
        x= head.xcor()
        y=head.ycor()
        segement[0].goto(x,y)
        head.shape("circle")#changing shape of head when snake eat food
        
    
     
     
    move()#calling move function
    time.sleep(delay)#delaying time for seeing the action

wn.mainloop()



