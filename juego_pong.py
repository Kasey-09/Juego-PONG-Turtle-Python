from turtle import *
import random
import time


root = Screen()
root.title('PONG')
root.bgcolor('#020439')
root.setup(width=800,height=600)

#Puntuacion de jugadores:
JugadorA = 0
JugadorB = 0

#Jugador A:

rectanguloA = Turtle()
rectanguloA.speed(0)
rectanguloA.penup()
rectanguloA.shape('square')
rectanguloA.color('white')
rectanguloA.shapesize(stretch_wid=5,stretch_len=1)
rectanguloA.goto(-370,0)

#Jugador B:

rectanguloB = Turtle()
rectanguloB.speed(0)
rectanguloB.penup()
rectanguloB.shape('square')
rectanguloB.color('white')
rectanguloB.shapesize(stretch_wid=5,stretch_len=1)
rectanguloB.goto(370,0)

#Barra de separación:

Barra = Turtle()
Barra.speed(0)
Barra.shape('square')
Barra.shapesize(stretch_wid=31,stretch_len=.2)
Barra.color('white')
Barra.penup()

#Pelota:

Pelota = Turtle()
Pelota.speed(0)
Pelota.penup()
Pelota.shape('circle')
Pelota.color('white')

#Movimientos de los jugadores:

#Pelota:

Pelota = Turtle()
Pelota.speed(0)
Pelota.penup()
Pelota.shape('square')
Pelota.color('white')

#Movimiento de los jugadores:

def Up_A():
    y = rectanguloA.ycor()
    y +=20
    rectanguloA.sety(y)

def down_A():
    y = rectanguloA.ycor()
    y -=20
    rectanguloA.sety(y)

def Up_B():
    y = rectanguloB.ycor()
    y +=20
    rectanguloB.sety(y)

def down_B():
    y = rectanguloB.ycor()
    y -=20
    rectanguloB.sety(y)

root.listen()
root.onkeypress(Up_B,'Up')
root.onkeypress(down_B,'Down')
root.onkeypress(Up_A,'w')
root.onkeypress(down_A,'s')

#Modificar el movimiento de la pelota:

Pelota_x = 4
Pelota_y = 4

#Puntuacion:

pen = Turtle()
pen.color('white')
pen.speed(0)
pen.goto(0,260)
pen.penup()
pen.hideturtle()
pen.write(f"Jugador A: {JugadorA}            Jugador B: {JugadorB}",align='center',font=('Impact',20,'bold'))



while True:
    #Configuraciones y puntajes
    root.update()

    Pelota.setx(Pelota.xcor() + Pelota_x)
    Pelota.sety(Pelota.ycor() + Pelota_y)

    if Pelota.ycor()  > 290:
        Pelota_y *=-1

    if Pelota.ycor() < -290:
        Pelota_y *=-1
    
    if Pelota.xcor() > 390:
        Pelota.goto(0,0)
        Pelota_x *=-1
        JugadorA +=1
        pen.clear()
        pen.write(f"Jugador A: {JugadorA}            Jugador B: {JugadorB}",align='center',font=('Impact',20,'bold'))

    if Pelota.xcor() < -390:
        Pelota.goto(0,0)
        Pelota_x *=-1
        JugadorB +=1
        pen.clear()
        pen.write(f"Jugador A: {JugadorA}            Jugador B: {JugadorB}",align='center',font=('Impact',20,'bold'))
    
    #colisiones

    if ((Pelota.xcor() > 360 and Pelota.xcor() < 370)
        and (Pelota.ycor() < rectanguloB.ycor() + 50)
        and (Pelota.ycor() > rectanguloB.ycor() -50)):

        Pelota_x *=-1

    if ((Pelota.xcor() < -360 and Pelota.xcor() > -370)
        and (Pelota.ycor() < rectanguloA.ycor() + 50)
        and (Pelota.ycor() > rectanguloA.ycor() -50)):

        Pelota_x *=-1

    




    

        
        

    
    
 




root.mainloop()














