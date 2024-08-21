from tkinter import * # main window
import easygui # input dialog for user to input state
from PIL import ImageTk, Image # background img
import pandas as pd # csv reader library

root = Tk()
root.geometry("725x491+700+170") # the same size as the blank states img size and spawn window at certain location
root.title("USA State Quiz")
root.resizable(False, False)

stateMap = ImageTk.PhotoImage(Image.open("blank_states_img.gif"))

my_label = Label(image=stateMap)
my_label.place(x=0, y=0)

df = pd.read_csv('50_states.csv', sep=',') # read csv with seperator of comma

states = [tuple(x) for x in df.values]
guessedStates = []

while len(guessedStates) < 50:
	userAnswer = easygui.enterbox("Name a US state")

	for x in range(len(states)):
		state = states[x][0]

		if (str(userAnswer).lower() not in guessedStates) and (str(userAnswer).lower() == str(state).lower()):
			stateLabel = Label(root, text=state)
			stateLabel.place(x=states[x][1], y=states[x][2])

			guessedStates.append(state.lower())
			root.title(f"USA State Quiz {len(guessedStates)} / 50")

	try: # logic to check if main window is destroyed
		root.winfo_exists()
	except:
		break

root.mainloop()