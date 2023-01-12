#assignment 1
#Rui-Jia Meng

import turtle


def my_artwork():
    """()->NoneType
    display a imagine according to the turtle code.

    """
    
    astro=turtle.Turtle()
    astro.color("black","purple")
    astro.speed("fast")
    astro.begin_fill()
    astro.pensize(5)
    astro.right(80)
    astro.forward(150)
    astro.circle(100,160)
    astro.forward(150)
    astro.circle(127,200)
    astro.end_fill()


    astro.penup()
    astro.goto(0,300)
    astro.pendown()
    astro.begin_fill()
    astro.forward(100)
    astro.left(80)
    astro.forward(215)
    astro.left(80)
    astro.forward(100)
    astro.left(100)
    astro.forward(247)
    astro.end_fill()



    #eyes
    astro.color("black","red")
    astro.penup()
    astro.goto(200,290)
    astro.pendown()
    astro.begin_fill()
    astro.circle(30)
    astro.end_fill()


    astro.penup()
    astro.goto(50,290)
    astro.pendown()
    astro.begin_fill()
    astro.circle(30)
    astro.end_fill()



    astro.penup()
    astro.goto(90,-50)
    astro.pendown()
    for i in range(16):
        astro.pensize(1)
        astro.right(50)
        astro.forward(70)



    name=turtle.Turtle()
    name.penup()
    name.goto(110,20)
    name.pendown()
    name.color("blue")
    name.pensize(5)
    name.circle(30,180)
    name.left(90)
    name.forward(100)
    name.backward(45)
    name.left(37)
    name.forward(60)

    body=turtle.Turtle()
    body.penup()
    body.goto(125,192)
    body.pendown()
    body.pensize(20)
    body.right(90)
    body.forward(40)
    body.penup()
    body.goto(-10,30)
    body.pendown()
    body.right (90)
    body.circle(200,50)
    body.penup()
    body.goto(255,45)
    body.pendown()
    body.left(180)
    body.circle(200,40)
    body.penup()
    body.goto(70,-220)
    body.pendown()
    body.right(220)
    body.forward(40)
    body.penup()
    body.goto(180,-220)
    body.pendown()
    body.left(70)
    body.forward(40)

    body2=turtle.Turtle()
    body2.color("black","black")
    body2.speed("fast")
    body2.pensize(5)
    body2.penup()
    body2.begin_fill()
    body2.goto(300,180)
    body2.pendown()
    body2.circle(30)
    body2.end_fill()
    body2.penup()
    body2.goto(300,230)
    body2.pendown()
    body2.left(75)
    body2.pensize(10)
    body2.speed("slow")
    body2.forward(50)
    body2.penup()
    body2.goto(290,230)
    body2.pendown()
    body2.left(50)
    body2.pensize(10)
    body2.forward(50)
    body2.penup()
    body2.goto(30,-300)
    body2.pendown()
    body2.begin_fill()
    for i in range(4):
        body2.forward(50)
        body2.right(90)
    body2.end_fill()    
    body2.penup()
    body2.goto(200,-300)
    body2.pendown()
    body2.begin_fill()
    for i in range(4):
        body2.forward(50)
        body2.right(90)
    body2.end_fill()   

    body2.penup()
    body2.goto(-160,-38)
    body2.pendown()
    

    def weapon(lenght,times):
        """(float,float)->NoneType
        display a picture in which its shape follows the lenght and times.
        """
        for i in range(times):
            body2.forward(lenght)
            body2.left(160)
    weapon(200,17)


my_artwork()


















