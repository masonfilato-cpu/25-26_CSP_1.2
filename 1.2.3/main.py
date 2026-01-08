import turtle as trtl
import random as rand


apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50
current_letter = "a"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def reset_apple(active_apple):
#Generate a random number and pop that index
#The letter we pop becomes the letter on the apple
    length_of_list = len(letters)
    if(length_of_list != 0):
        index = rand.randint(0, length_of_list)
        current_letter = letters.pop(rand.randint(0,len(letters)))
        #Finish First
        active_apple.goto()
        draw_apple(active_apple, current_letter)


wn.bgpic("background.gif")
apple = trtl.Turtle()
wn.tracer(False)
apple.penup()

# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, current_letter):
  active_apple.shape(apple_image)
  draw_letter(current_letter, active_apple)
  wn.update()

def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)

def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 60, "bold"))
  active_apple.setpos(remember_position)

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.


#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.



draw_apple(apple)
wn.onkeypress(drop_apple, "a")



wn.listen()
trtl.mainloop()