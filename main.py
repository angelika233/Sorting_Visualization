from tkinter import *
from tkinter import ttk
import random


# Generating random numbers
def Generate_number():
    try:
        min = int(minEntry.get())
    except:
        min = 0
    try:
        max = int(maxEntry.get())
    except:
        max = 20
    try:
        size = int(sizeEntry.get())
    except:
        size = 10

    if min < 0:
        min = 0
    if max < min or max > 100:
        max = 20
    if size < 3 or size > 30:
        size = 10

    data = []
    for i in range(0, size):
        data.append(random.randrange(min, max + 1))

    Draw(data)


# Drawing dataset on canvas
def Draw(data):
    canvas.delete("all")
    canv_h = 360
    canv_w = 570
    width = canv_w / (len(data) + 1)
    spacing = 5
    offset = 30
    normalized = [i / max(data) for i in data]
    for i, height in enumerate(normalized):
        x0 = i * width + offset + spacing
        y0 = canv_h - height * 300
        x1 = (i + 1) * width + offset
        y1 = canv_h

        canvas.create_rectangle(x0, y0, x1, y1, fill='#5b34eb')
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]))


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

menu = ttk.Combobox(frame, textvariable=selected_algorithm, values=['Bubble', 'Merge', 'Quick'])
menu.grid(row=0, column=1, padx=5, pady=5)
menu.current(0)


size = Label(frame, text="Size ", bg='grey')
size.grid(row=0, column=2, padx=15, pady=2, sticky=W)
sizeEntry = Entry(frame)
sizeEntry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

minimum = Label(frame, text="Min Value ", bg='grey')
minimum.grid(row=1, column=0, padx=5, pady=5, sticky=W)
minEntry = Entry(frame)
minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

maximum = Label(frame, text="Max Value ", bg='grey')
maximum.grid(row=1, column=2, padx=5, pady=5, sticky=W)
maxEntry = Entry(frame)
maxEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

button = Button(frame, text="Start Generating", command=Generate_number, bg='#5d4c9e')
button.grid(row=1, column=4, padx=55, pady=5)


root.mainloop()
