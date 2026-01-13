import turtle as trtl
import random as rand

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200 #Location of the ground
apple_letter_x_offset = -25 #Horizontal Offset
apple_letter_y_offset = -50 #Vertical Offset
current_letter = "a" #Current letter
screen_width = 400 #Width of screen
screen_height = 400 #Heitght of screen

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


wn.bgpic("background.gif")
apple = trtl.Turtle()
wn.tracer(False)
apple.penup()

def reset_apple(active_apple):
    # Generate a random number - > pop that index
    # The letter we pop, becomes the letter on the apple
    #Get global variable
    global current_letter
    #How many letters are left
    length_of_list = len(letters)
    #If we aren't out
    if(length_of_list != 0):
        #Pick a random number
        index = rand.randint(0, length_of_list)
        #Set the random letter to our current letter
        current_letter = letters.pop(index)
        # Goto: x and y -> randomize each
        #active_apple.goto(rand.randint(-(screen_width)/2, (screen_width)/2), rand.randint(-(screen_height) / 2, (screen_height) / 2))
        active_apple.goto(200,200)
        draw_apple(active_apple, current_letter)


# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple, current_letter):
  active_apple.shape(apple_image)
  active_apple.showturtle()
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
  active_apple.color("black")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_position)

def check_apple_a():
    if(current_letter == "a"):
        drop_apple()
def check_apple_b():
    if(current_letter == "b"):
        drop_apple()
def check_apple_c():
    if(current_letter == "c"):
        drop_apple()
def check_apple_d():
    if(current_letter == "d"):
        drop_apple()
def check_apple_e():
    if(current_letter == "e"):
        drop_apple()
def check_apple_f():
    if(current_letter == "f"):
        drop_apple()
def check_apple_g():
    if(current_letter == "g"):
        drop_apple()
def check_apple_h():
    if(current_letter == "h"):
        drop_apple()
def check_apple_i():
    if(current_letter == "i"):
        drop_apple()
def check_apple_j():
    if(current_letter == "j"):
        drop_apple()
def check_apple_k():
    if(current_letter == "k"):
        drop_apple()
def check_apple_l():
    if(current_letter == "l"):
        drop_apple()
def check_apple_m():
    if(current_letter == "m"):
        drop_apple()
def check_apple_n():
    if(current_letter == "n"):
        drop_apple()
def check_apple_o():
    if(current_letter == "o"):
        drop_apple()
def check_apple_p():
    if(current_letter == "p"):
        drop_apple()
def check_apple_q():
    if(current_letter == "q"):
        drop_apple()
def check_apple_r():
    if(current_letter == "r"):
        drop_apple()
def check_apple_s():
    if(current_letter == "s"):
        drop_apple()
def check_apple_t():
    if(current_letter == "t"):
        drop_apple()
def check_apple_u():
    if(current_letter == "u"):
        drop_apple()
def check_apple_v():
    if(current_letter == "v"):
        drop_apple()
def check_apple_w():
    if(current_letter == "w"):
        drop_apple()
def check_apple_x():
    if(current_letter == "x"):
        drop_apple()
def check_apple_y():
    if(current_letter == "y"):
        drop_apple()
def check_apple_z():
    if(current_letter == "z"):
        drop_apple()


draw_apple(apple, current_letter)

wn.onkeypress(check_apple_a, "a")
wn.onkeypress(check_apple_b, "b")
wn.onkeypress(check_apple_c, "c")
wn.onkeypress(check_apple_d, "d")
wn.onkeypress(check_apple_e, "e")
wn.onkeypress(check_apple_f, "f")
wn.onkeypress(check_apple_g, "g")
wn.onkeypress(check_apple_h, "h")
wn.onkeypress(check_apple_i, "i")
wn.onkeypress(check_apple_j, "j")
wn.onkeypress(check_apple_k, "k")
wn.onkeypress(check_apple_l, "l")
wn.onkeypress(check_apple_m, "m")
wn.onkeypress(check_apple_n, "n")
wn.onkeypress(check_apple_o, "o")
wn.onkeypress(check_apple_p, "p")
wn.onkeypress(check_apple_q, "q")
wn.onkeypress(check_apple_r, "r")
wn.onkeypress(check_apple_s, "s")
wn.onkeypress(check_apple_t, "t")
wn.onkeypress(check_apple_u, "u")
wn.onkeypress(check_apple_v, "v")
wn.onkeypress(check_apple_w, "w")
wn.onkeypress(check_apple_x, "x")
wn.onkeypress(check_apple_y, "y")
wn.onkeypress(check_apple_z, "z")


wn.listen()
trtl.mainloop()