
from tkinter import *
from tkinter import ttk


# Creating window
root = Tk()
root.geometry('700x500')
root.config(bg='#2c2c2e')
root.title('Sorting Algorithms Visualization')

# Variables
selected_algorithm = StringVar()

# Frame and labels

frame = Frame(root, width=570, height=110, bg='gray')
frame.grid(row=0, column=0, padx=15, pady=5)

canvas = Canvas(root, width=570, height=365, bg='white')
canvas.grid(row=1, column=0, padx=15, pady=5)

label_1 = Label(frame, text="Select Algorithm", bg='grey')
label_1.grid(row=0, column=0, padx=5, pady=5, sticky=W)

menu = ttk.Combobox(frame, textvariable=selected_algorithm, values =['Bubble','Merge', 'Quick'])
menu.grid(row=0, column=1, padx=5, pady=5)
menu.current(0)

size=Label(frame, text="Size ", bg='grey')
size.grid(row=1, column=0, padx=15, pady=2, sticky=W)
sizeEntry = Entry(frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

minimum =Label(frame, text="Min Value ", bg='grey')
minimum.grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

maximum = Label(frame, text="Max Value ", bg='grey')
maximum.grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)


root.mainloop()
