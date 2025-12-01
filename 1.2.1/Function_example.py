#Goal: Draw Squares with a turtle

import turtle as trtl
#Make a turtle
James = trtl.Turtle()

def drawsquare():
    for sides in range(4):
        James.forward(30)
        James.right(90)

drawsquare()
James.forward(60)
drawsquare()


wn = trtl.Screen()
wn.mainloop()