#Goal: Draw Squares with a turtle

import turtle as trtl
#Make a turtle
James = trtl.Turtle()

def drawsquare(length):
    for sides in range(4):
        James.forward(length)
        James.right(90)

drawsquare(23)
James.forward(60)
drawsquare(45)


wn = trtl.Screen()
wn.mainloop()