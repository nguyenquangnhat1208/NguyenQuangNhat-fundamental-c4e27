from turtle import *
speed(0)

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

color('red')

begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
forward(100)
end_fill()

color('blue')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
forward(100)
end_fill()

color('brown')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
forward(100)
end_fill()

color('yellow')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
forward(100)
end_fill()

color('grey')
begin_fill()
for i in range(2):
    forward(100)
    left(90)
    forward(150)
    left(90)
end_fill()

mainloop()