# Python program to create a simple GUI
# Simple Quiz using Tkinter

import tkinter as tk
#import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file for data
import json
from tkinter import filedialog
import random

#class to define the components of the GUI
class Quiz(Menu):
	# This is the first method which is called when a
	# new object of the class is initialized. This method
	# sets the question count to 0. and initialize all the
	# other methoods to display the content and make all the
	# functionalities available
	def __init__(self):
		frame2.pack_forget()
		self.frame1 = Frame(gui)
		self.frame1.pack(side="top", expand=True, fill="both")
		# set question number to 0
		self.q_no=0
		self.end=0
		print(Menu.amount)
		print(Menu.startpos)
		print("Value: ", Menu.range)

		self.random_list = []
		
		self.inputNumbers = range(Menu.startpos, Menu.range)

		print("Value: ", self.inputNumbers)

		self.random_list = random.sample(self.inputNumbers, Menu.amount)

		self.q_no = self.random_list[self.end]

		print(self.random_list)

		
		# assigns ques to the display_question function to update later.
		self.display_title()
		self.display_question()
		
		# opt_selected holds an integer value which is used for
		# selected option in a question.
		self.opt_selected=IntVar()
		
		# displaying radio button for the current question and used to
		# display options for the current question
		self.opts=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
		
		# no of questions
		self.data_size=Menu.amount
		
		# keep a counter of correct answers
		self.correct=0

	def clear(self):
		for widgets in self.frame1.winfo_children():
			widgets.destroy()

	# This method is used to display the result
	# It counts the number of correct and wrong answers
	# and then display them at the end as a message Box
	def display_result(self):
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Oikein: {self.correct}"
		wrong = f"Väärin: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Pisteet(%): {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Tulokset", f"{result}\n{correct}\n{wrong}")


	# This method checks the Answer after we click on Next.
	def check_ans(self, q_no):
		
		# checks for if the selected option is correct
		if self.opt_selected.get() == answer[q_no]:
			# if the option is correct it return true
			return True

	# This method is used to check the answer of the
	# current question by calling the check_ans and question no.
	# if the question is correct it increases the count by 1
	# and then increase the question number by 1. If it is last
	# question then it calls display result to show the message box.
	# otherwise shows next question.
	def next_btn(self):
		
		# Check if the answer is correct
		if self.check_ans(self.q_no):
			
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		
		# Moves to next Question by incrementing the q_no counter

		self.end+=1

		# print(self.q_no)
		# print(self.random_list[self.end])

		print(self.end, self.data_size, Menu.range, self.q_no)
		
		# checks if the q_no size is equal to the data size
		if self.end==self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			self.clear()
			self.frame1.pack_forget()
			
			file = open("results.txt","a")

			print( f"{self.correct} / {self.data_size}", file=file)
			Menu.remove_line("results.txt",1)
			file.close()
			Menu()
		else:
			self.q_no = self.random_list[self.end]
			# shows the next question
			self.display_question()
			self.display_options()


	# This method shows the two buttons on the screen.
	# The first one is the next_button which moves to next question
	# It has properties like what text it shows the functionality,
	# size, color, and property of text displayed on button. Then it
	# mentions where to place the button on the screen. The second
	# button is the exit button which is used to close the GUI without
	# completing the quiz.
	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_button = Button(self.frame1, text="Seuraava",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		next_button.place(x=350,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(self.frame1, text="Sammuta", command=gui.destroy,
		width=8,bg="black", fg="white",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_button.place(x=725,y=50)


	# This method deselect the radio button on the screen
	# Then it is used to display the options available for the current
	# question which we obtain through the question number and Updates
	# each of the options for the current question of the radio button.
	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1
			


	# This method shows the current Question on the screen
	def display_question(self):
		
		# setting the Question properties
		print(self.q_no)
		q_no = Label(self.frame1, text=question[self.q_no], width=60,
		font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)


	# This method is used to Display Title
	def display_title(self):
		
		# The title to be shown
		title = Label(self.frame1, text="Tietovisa",
		width=50, bg="blue",fg="white", font=("ariel", 20, "bold"))
		# place of the title
		title.place(x=0, y=2)


	# This method shows the radio buttons to select the Question
	# on the screen at the specified position. It also returns a
	# list of radio button which are later used to add the options to
	# them.
	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# setting the radio button properties
			radio_btn = Radiobutton(self.frame1,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("ariel",14))
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list
	




class Menu:
	def __init__(self):
		frame2.pack(side="top", expand=True, fill="both")

		self.display_scale()
		self.display_recent()
		self.display_title()
		self.display_guide()
		self.display_buttons()
		#self.display_menu()
	
	def clear(self):
		for widgets in frame2.winfo_children():
			widgets.destroy()
	
	def read_file_from_start(file_path):
		try:
			with open(file_path, 'r') as file:
				content = file.readlines()
				print(content)
			return content
		except FileNotFoundError:
			return []
		
	def display_lines_in_label(file_path, self):
		lines_from_start = Menu.read_file_from_start(file_path)
		lines_from_start.reverse()  # Reverse the list to display lines in reverse order
		self.lines_text = "".join(lines_from_start)
		print(self.lines_text)

	def remove_line(results,lineToSkip):
		with open(results,'r') as read_file:
			lines = read_file.readlines()
		currentLine = 1
		with open(results,'w') as write_file:

			for line in lines:
				if currentLine == lineToSkip:
					pass
				else:
					write_file.write(line)
				currentLine += 1


	def display_recent(self):
		file_path = "results.txt"

		if file_path:
			Menu.display_lines_in_label(file_path, self)


		leaderboard_title = Label(frame2, text="Viimeisin:\n",
		width=9, font=("ariel", 16, "bold"))
		# place of the title
		leaderboard_title.place(x=0, y=100)

		leaderboard = Label(frame2, text=self.lines_text,
		width=10, justify='left', font=("ariel", 14, "bold"))
		# place of the title
		leaderboard.place(x=0, y=130)

	def display_scale(self):
		scale = Scale(frame2, from_=1, to=15, command=Menu.on_scale_changed,
		font=("ariel",16,"bold"))
		scale.pack()
		scale.set('0')
		scale.place(x=270,y=113)

	def display_title(self):
		
		# The title to be shown
		title = Label(frame2, text="Tietovisa",
		width=50, bg="blue",fg="white", font=("ariel", 20, "bold"))
		# place of the title
		title.place(x=0, y=2)

	def display_guide(self):
		
		# setting the Question properties
		q = Label(frame2, text="Valitse aihe:",
		width=71, fg="black", font=("ariel", 14, "bold"))
		
		#placing the option on the screen
		q.place(x=0, y=50)

		# setting the Question properties
		amount = Label(frame2, text="Määrä:",
		font=("ariel", 14, "bold"))
		
		#placing the option on the screen
		amount.place(x=200, y=150)

	def math(self):
		self.clear()
		Menu.startpos = 0
		Menu.range = 30
		Quiz()
	def geography(self):
		self.clear()
		Menu.startpos = 30
		Menu.range = 60
		print("Value: ", Menu.range)
		Quiz()
	def history(self):
		self.clear()
		Menu.startpos = 60
		Menu.range = 90
		Quiz()
	def mixed(self):
		self.clear()
		Menu.startpos = 0
		Menu.range = 90
		Quiz()

	def on_scale_changed(val):
		print(Menu.amount)
		
		Menu.amount = int(val)

	def display_buttons(self):
		Menu.amount = 1

		# The first button is the Next button to move to the
		# next Question
		math = Button(frame2, text="Matikka",command=self.math,
		width=10, bg="red", fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		math.place(x=355,y=100)

		# The first button is the Next button to move to the
		# next Question
		geo = Button(frame2, text="Maantieto",command=self.geography,
		width=10, bg="red", fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		geo.place(x=355,y=150)

		# The first button is the Next button to move to the
		# next Question
		history = Button(frame2, text="Historia",command=self.history,
		width=10, bg="red", fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		history.place(x=355,y=200)

		mixed = Button(frame2, text="Sekoitus",command=self.mixed,
		width=10, bg="red", fg="white",font=("ariel",16,"bold"))
		
		# placing the button on the screen
		mixed.place(x=355,y=250)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(frame2, text="Sammuta", command=gui.destroy,
		width=8,bg="black", fg="white",font=("ariel",16," bold"))
		
		# placing the Quit button on the screen
		quit_button.place(x=725,y=50)




# Create a GUI Window
gui = Tk()

# set the size of the GUI Window
gui.geometry("850x450")

gui.resizable(0, 0)

frame2 = Frame(gui)

# set the title of the Window
gui.title("Tietovisa")


file_path = "results.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()

except FileNotFoundError:
    with open(file_path, "w") as file:
        for i in range(1, 11):
            file.write(f"\n")


# get the data from the json file
with open('data.json', encoding='utf-8') as f:
	data = json.load(f)

# set the question, options, and answer
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])

# create an object of the Quiz Class.
menu = Menu()

# Start the GUI
gui.mainloop()

# END OF THE PROGRAM
