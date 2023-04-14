import turtle
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")


ball=turtle.Turtle()
ball.shape("circle")
ball.color("green")
ball.penup()
ball.speed(0)
ball.goto(0,200)  #top point of bouncing ball
ball.dy=0         #it is also for hight to jumping


gravity=0.1

while True:
    ball.dy -=gravity
    ball.sety(ball.ycor()+ball.dy)


    #create for a bounce
    if ball.ycor()< -300:     #bottum point
        ball.dy*=-1
