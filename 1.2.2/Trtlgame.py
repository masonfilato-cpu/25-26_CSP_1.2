#-----import statements-----
import turtle as trtl
import random as rand
import turtle as Timer
import turtle as wn
import random as Random_Color

import leaderboard as lb
#-----game configuration----
spot_color = ["red", "blue", "green", "orange", "purple", "gold"]
score = 0
sizes = [1,2,3,4,5,6]
font_setup = ("Arial", 20, "normal")
new_color = Random_Color.choice(spot_color)
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input("What is your name?")


score_writer = trtl.Turtle()
score_writer.penup()
box_turtle = trtl.Turtle()
box_turtle.speed(0)
score_writer.speed(0)

Timer.hideturtle()

wn.bgcolor("orange")

meowl = trtl.Turtle()
meowl.shape("circle")
rand.choice(spot_color)

meowl.shapesize(3)
meowl.penup()
meowl.speed(0)

counter =  Timer.Turtle()
counter.hideturtle()
box_turtle.hideturtle()
score_writer.hideturtle()
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
    global timer_up
    if timer_up == False:
        change_position()
        meowl.color(str(new_color))
        change_size_randomly(meowl, sizes)
    else:
        meowl.hideturtle()

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
#Start countdown and update
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def change_size_randomly(turtle_instance, size_list):
    new_size = rand.choice(size_list)
    turtle_instance.shapesize(new_size)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global meowl

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, meowl, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, meowl, score)












#-----events----------------
meowl.onclick(spot_clicked)

scoreBox()
wn = trtl.Screen()

wn.ontimer(countdown, counter_interval)
wn.mainloop()