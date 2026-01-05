#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()

#-----functions-----
ground_height = -150
def apple_fall():
    apple.penup()
    apple.goto(apple.xcor(), ground_height)
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
wn.onkeypress(apple_fall, "a")



#-----function calls-----
draw_apple(apple)
wn.listen()


wn.mainloop()