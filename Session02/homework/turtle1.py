from turtle import * 

shape("turtle")
color("red")

left(60)

for i in range(4):
    for i in range(2):
        forward(100)
        left(60)
        forward(100)
        left(120)

    left(90)


mainloop()