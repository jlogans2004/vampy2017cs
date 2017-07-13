import turtle as t

f=t.forward

l=t.left

t.speed(2)

Size = 200

t.color('green', 'green')

def square(Size):
	f(Size)
	
	l(90)
	
	f(Size)
	
	l(90)
	
	f(Size)
	
	l(90)
	
	f(Size)
	
	l(90)

def triangle(Size):
	f(Size)
	l(120)
	f(Size)
	l(120)
	f(Size)
	l(120)


def dog(Size):
	square(Size)
	f(Size/10)
	l(240)
	triangle(Size/4)
	l(120)
	f(Size*0.8)
	l(240)
	triangle(Size/4)
	l(120)
	f(Size/10)
	l(90)
	f(Size*0.8)
	l(270)
	square(Size*0.4)
	f(Size*0.1)
	t.penup()
	l(90)
	f(Size*0.1)
	t.pendown()
	t.right(90)
	f(Size*0.2)
	t.penup()
	l(90)
	f(Size*0.2)
	l(90)
	f(Size*0.05)
	t.pendown()
	f(Size*0.025)
	t.penup()
	f(Size*0.05)
	t.pendown()
	f(Size*0.025)
	t.color('white','white')

dog(Size)
	
t.exitonclick()
