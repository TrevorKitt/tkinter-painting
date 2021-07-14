from tkinter import *

window = Tk()
window.title('my gui')

canvas = Canvas(window, width=400, height=400)
canvas.pack()

circle = canvas.create_oval(100,200,130,230, fill='red')
blue_rect = canvas.create_rectangle(50,50,70,80,fill ='blue')


def move_circle(event):
    key = event.keysym
    if key == "Right":
        canvas.move(circle, 10,0)
    elif key == "Left":
        canvas.move(circle, -10,0)


colours = ['blue', 'red', 'yellow', 'green', 'purple', 'black', 'orange']


def change_colour_blue(event):
    canvas.itemconfig(circle, fill='blue')


def change_colour_red(event):
    canvas.itemconfig(circle, fill='red')


def cycle_colour(event):
    colour = canvas.itemcget(circle, "fill")
    index = colours.index(colour)
    index += 1
    if index == len(colours):
        index = 0
    canvas.itemconfig(circle, fill=colours[index])


canvas.bind_all('<Key>', move_circle)
canvas.bind_all('b', change_colour_blue)
canvas.bind_all('r', change_colour_red)
canvas.bind_all('c', cycle_colour)

window.mainloop()  # gui main event loop
