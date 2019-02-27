from turtle import * 

shape("turtle")
color("green","orange")
speed(0)

begin_fill()
for i in range(36):
    circle(100)
    left(10)
end_fill()    

mainloop()