# importing turtle module
import turtle
print(help(turtle))

# making the window
window = turtle.Screen()
# window a name
window.title("pong game by ayman")

# window customize
# background color
window.bgcolor("black")
# height and weight
window.setup(width=800, height=600)
# stop the screen from refreshing
window.tracer(0)

# stick 1 
stick_1 = turtle.Turtle()
# speed of the stick
stick_1.speed(0) 
# shape of the stick
stick_1.shape("square")
# color of the stick
stick_1.color("red")
# to not make lines in the screen 
stick_1.penup()
# the place of the stick 
stick_1.goto(-350, 0)
# to make the size of the stick
stick_1.shapesize(stretch_wid=5, stretch_len=1)

# stick 2
stick_2 = turtle.Turtle()
# speed of the stick
stick_2.speed(0) 
# shape of the stick
stick_2.shape("square")
# color of the stick
stick_2.color("blue")
# to not make lines in the screen 
stick_2.penup()
# the place of the stick 
stick_2.goto(350, 0)
# to make the size of the stick
stick_2.shapesize(stretch_wid=5, stretch_len=1)

# ball
ball = turtle.Turtle()
# speed of the ball
ball.speed(0) 
# shape of the ball
ball.shape("circle")
# color of the stick
ball.color("yellow")
# to not make lines in the screen 
ball.penup()
# the place of the ball 
ball.goto(0, 0)
# the movement of the ball
# the speed of the ball in weight (right - left)
ball.dx = 0.25
# the speed of the ball in height (up - down)
ball.dy = 0.25

# score 
winning_score = 3
red_player = 0
blue_player = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-160,260)
score.write(f"red player = {red_player} blue player ={blue_player}", font=("Courier",15,"normal"))


# functions
# moving sticks 
def stick_1_up():
    # get the coordinate of stick 1
    y =stick_1.ycor()
    # set y to increase by 20
    y += 20
    # give the stick new coordinate 
    stick_1.sety(y)
def stick_1_down():
    # get the coordinate of stick 1
    y =stick_1.ycor()
    # set y to decrease by 20
    y -= 20
    # give the stick new coordinate  
    stick_1.sety(y)


def stick_2_up():
    # get the coordinate of stick 2
    y =stick_2.ycor()
    # set y to increase by 20
    y += 20
    # give the stick new coordinate  
    stick_2.sety(y)
def stick_2_down():
    # get the coordinate of stick 2
    y =stick_2.ycor()
    # set y to decrease by 20
    y -= 20
    # give the stick new coordinate  
    stick_2.sety(y)

# keyboard bindings
# to make the window to expect inputs from keybourd
window.listen()
# if user pressed 'w' button call the function of up stick 1
window.onkeypress(stick_1_up,"w") 
# if user pressed 'w' button call the function of down stick 1
window.onkeypress(stick_1_down,"s") 
# if user pressed 'arrow up' button call the function of up stick 2
window.onkeypress(stick_2_up,"Up") 
# if user pressed 'arrow down' button call the function of down stick 2
window.onkeypress(stick_2_down,"Down") 

# the loop of the game
while True:
    # update the screen every loop
    window.update()
    
    # move the ball
    # ball starts at 0 and everytime loops run --> +0.1 x
    ball.setx(ball.xcor() + ball.dx)
    # ball starts at 0 and everytime loops run --> +0.1 y
    ball.sety(ball.ycor() + ball.dy)

    # border check 
    # top border +300px, bottom border -300px, ball is 20px.
    if ball.ycor() > 290:  # if ball is at the top border.
        ball.sety(290)  # set y coordinate +290
        ball.dy *= -1  # reverse direction, making 0.1 ---> -0.1

    if ball.ycor() < -290:  # if ball is at bottom border
        ball.sety(-290)  # set y coordinate -290
        ball.dy *= -1  # reverse direction, making -0.1 ---> 0.1

    if ball.xcor() > 390 :  # if ball is at right border
        ball.goto(0, 0)  # return ball to the center
        ball.dx *= -1  # reverse the x direction
        red_player += 1
        score.clear()
        score.write(f"red player = {red_player} blue player ={blue_player}", font=("Courier",15,"normal"))
    
    if ball.xcor() < -390 :  # if ball is at right border
        ball.goto(0, 0)  # return ball to the center
        ball.dx *= -1  # reverse the x direction
        blue_player += 1
        score.clear()
        score.write(f"red player = {red_player} blue player ={blue_player}", font=("Courier",15,"normal"))

    # ball and stick
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < stick_2.ycor() + 40 and ball.ycor() > stick_2.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1

    if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < stick_1.ycor() + 40 and ball.ycor() > stick_1.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1
    
    # check if there is winner
    if red_player == winning_score or blue_player == winning_score:
        # check who is the winner
        if red_player == winning_score:
            winner = "Red player"
        else:
            winner = "Blue player"
        score.clear() # update the score
        score.goto(0,260) # the place of text
        score.write(f"{winner} wins!", align="center", font=("Courier", 15, "normal")) # display who is the winner
        break # stop the game by breaking up from the loop

# makes the turtle screen on until click on it with mouse
window.exitonclick() 
        