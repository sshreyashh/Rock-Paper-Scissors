# Import Required Library
from tkinter import *
import random

# Create Object
obj = Tk()
# Set geometry
obj.geometry("600x400")

# Set title
obj.title("Rock Paper Scissor Game")

# Computer Value
c_choice = {"0":"Rock","1":"Paper","2":"Scissor"} 
# Reset The Game
def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text = "Player")
	l3.config(text = "Computer")
	l4.config(text = "")

# Disable the Button
def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

# If player selected rock
def isrock():
	c_v = c_choice[str(random.randint(0,2))]
	if c_v == "Rock":
		res = "Its a tie."
	elif c_v=="Scissor":
		res = "Player Wins!"
	else:
		res = "Computer Wins!"
	l4.config(text = res)
	l1.config(text = "Rock")
	l3.config(text = c_v)
	button_disable()

# If player selected paper
def ispaper():
	c_v = c_choice[str(random.randint(0, 2))]
	if c_v == "Paper":
		res = "Its a tie."
	elif c_v=="Scissor":
		res = "Computer Wins!"
	else:
		res = "Player Wins!"
	l4.config(text = res)
	l1.config(text = "Paper")
	l3.config(text = c_v)
	button_disable()

# If player selected scissor
def isscissor():
	c_v = c_choice[str(random.randint(0,2))]
	if c_v == "Rock":
		res = "Computer Wins!"
	elif c_v == "Scissor":
		res = "Its a tie."
	else:
		res = "Player Wins!"
	l4.config(text = res)
	l1.config(text = "Scissor")
	l3.config(text = c_v)
	button_disable()

# Add Labels, Frames and Button
Label(obj,text = "Rock Paper Scissor",font = "normal 20 bold",fg = "brown").pack(pady = 20)
frame = Frame(obj)
frame.pack()

l1 = Label(frame,text = "Player",font = 10)
l2 = Label(frame,text = "   VS	",font = "normal 10 bold")
l3 = Label(frame, text = "Computer", font = 10)

l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack()

l4 = Label(obj,text = "",font = "normal 20 bold",bg = "white",width = 15 ,borderwidth = 2,relief = "solid")
l4.pack(pady = 20)

f1 = Frame(obj)
f1.pack()

b1 = Button(f1, text = "Rock",font = 10, width = 7,command = isrock)
b2 = Button(f1, text = "Paper ",font = 10, width = 7,command = ispaper)
b3 = Button(f1, text = "Scissor",font = 10, width = 7,command = isscissor)

b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)

Button(obj, text = "Reset Game",font = 10, fg = "white",bg = "black", command = reset_game).pack(pady = 20)

# Execute Tkinter
obj.mainloop()
