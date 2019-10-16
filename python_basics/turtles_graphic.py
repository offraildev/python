import turtle

def draw_square(turtle_obj):
    for i in range(4):
        turtle_obj.forward(100)
        turtle_obj.right(90)

def draw_art():
    # init window and assign color
    window = turtle.Screen()
    window.bgcolor('blue')
    # init brad to draw squares
    brad = turtle.Turtle()
    brad.color('red')
    brad.shape('circle')
    brad.speed(30)
    # move brad to draw circles
    deg = 5
    while deg < 360:
        draw_square(brad)
        brad.right(deg)
        deg += 5
    # init angie to draw circle   
    # angie = turtle.Turtle()
    # angie.shape('arrow')
    # angie.color('red')
    # angie.circle(100) 
    
    window.exitonclick()

draw_art()
