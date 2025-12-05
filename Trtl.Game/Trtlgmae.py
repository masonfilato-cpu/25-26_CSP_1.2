#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "purple"
score = 0
font_setup = ("Arial", 20, "normal")

#-----initialize turtle-----
score_writer = trtl.Turtle()
score_writer.penup()
box_turtle = trtl.Turtle()
box_turtle.speed(0)
score_writer.speed(0)


meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()
meowl.speed(0)
#-----game functions--------
# Draw the box for the score
def scoreBox():
    # Set up the starting location and pendown
    box_turtle.penup()
    box_turtle.goto(275, 325)
    box_turtle.pendown()

    # Draw the box
    for sides in range(2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(50)
        box_turtle.left(90)

    # Place score_writer where it will write the score
    score_writer.penup()
    score_writer.goto(300, 332)

# Get a score boost, move the turtle randomly
def spot_clicked(x, y):
    change_position()

def change_position():
    # Move the turtle to a random location
    newX = rand.randint(-300, 300)
    newY = rand.randint(-300, 300)
    meowl.goto(newX, newY)
    update_score()

def update_score():
    # Include the global score
    global score
    # Increment the score by 1
    score += 1
    #Clear out the prior score
    score_writer.clear()
    # print the score
    score_writer.write(score, font=font_setup)

#-----events----------------
meowl.onclick(spot_clicked)

scoreBox()
wn = trtl.Screen()
wn.mainloop()