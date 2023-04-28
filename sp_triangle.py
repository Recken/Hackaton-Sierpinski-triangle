import turtle
import math

turtle.tracer()
#turtle.tracer(100, 0)	# hides the movement of the turtle
turtle.setworldcoordinates(0, 0, 700, 700)	# space for drawing
#turtle.hideturtle()	# hides the arrow while drawing
turtle.setposition(50,50)

def draw_triangle(ax, ay, bx, by, cx, cy):
	turtle.color("red", "yellow")
	turtle.begin_fill()
	turtle.goto(cx, cy)
	turtle.left(120)
	diagonal = math.sqrt((bx/2)**2 + by**2)
	print(diagonal)
	turtle.goto(bx,by)
	turtle.left(120)
	turtle.goto(ax,ay)
	turtle.end_fill()
	#turtle.done()
	pass



draw_triangle(50, 50, 350, 650, 650, 50)
# initial position for the triangle
# en vez de ocupar 700x700 va de 50x650 tanto para x como y

turtle.exitonclick()

print("hello world")
