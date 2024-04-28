import turtle

Rasimlox = turtle.Turtle()

turtle.setup(500, 500, 0, 0)

turtle.screensize(480, 480, bg ="#ccc")
turtle.tracer(0)
turtle.hideturtle()

def draw_square(x, y, length):
    Rasimlox.penup()
    Rasimlox.home()
    Rasimlox.goto((x, y))
    Rasimlox.color("")
    Rasimlox.pendown()
    
    for storona in range(4):
        Rasimlox.forward(length)
        Rasimlox.right(90)
        
draw_square(-220, 220, 10)      
turtle.done()