from tkinter import *

window = Tk()
window.title('Four Shapes Puzzle')

canvas = Canvas(window, width=400, height=400)
canvas.pack()

circle = canvas.create_oval(100, 200, 130, 230, fill='red')
rect = canvas.create_rectangle(50, 50, 70, 80, fill='blue')
triangle = canvas.create_polygon(185, 65, 225, 50, 205, 30, fill='green')
arc = canvas.create_arc(300, 300, 350, 350, start=0, extent=75, fill='purple')
shapes = [circle, rect, triangle, arc]


def left_arrow(event):
    for shape in shapes:
        if canvas.itemcget(shape, "fill") == 'blue':
            canvas.move(shape, -10, 0)
        if canvas.itemcget(shape, "fill") == 'red':
            canvas.move(shape, 0, 10)


def up_arrow(event):
    for shape in shapes:
        if canvas.itemcget(shape, "fill") == 'red':
            canvas.move(shape, 0, -10)
        if canvas.itemcget(shape, "fill") == 'green':
            canvas.move(shape, -10, 0)


def right_arrow(event):
    for shape in shapes:
        if canvas.itemcget(shape, "fill") == 'green':
            canvas.move(shape, 10, 0)
        if canvas.itemcget(shape, "fill") == 'purple':
            canvas.move(shape, 0, -10)


def down_arrow(event):
    for shape in shapes:
        if canvas.itemcget(shape, "fill") == 'purple':
            canvas.move(shape, 0, 10)
        if canvas.itemcget(shape, "fill") == 'blue':
            canvas.move(shape, 10, 0)


next_colours = {'blue': 'red', 'red': 'green', 'green': 'purple', 'purple': 'blue'}


def cycle_colours(event):
    for shape in shapes:
        colour = canvas.itemcget(shape, "fill")
        next_colour = next_colours[colour]
        canvas.itemconfig(shape, fill=next_colour)


canvas.bind_all('<Left>', left_arrow)
canvas.bind_all('<Up>', up_arrow)
canvas.bind_all('<Right>', right_arrow)
canvas.bind_all('<Down>', down_arrow)
canvas.bind_all('c', cycle_colours)

window.mainloop()  # gui main event loop
