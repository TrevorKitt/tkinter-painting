from tkinter import *

window = Tk()
window.title("My Window")

canvas = Canvas(window, width=400, height=500)
canvas.pack()

oval_x = 100
oval_y = 50
oval_x_size = 50
oval_y_size = 150

# x1, y1, x2, y2
#RGB
#999
#A1F
#0123456789
#0123456789ABCDEF
canvas.config(bg='lightblue')

my_rectangle = canvas.create_rectangle(50,50,100,200, fill='#A912F2')

canvas.create_oval(oval_x,oval_y,oval_x + oval_x_size, oval_y + oval_y_size, fill='lightblue')
canvas.create_polygon(150,90,200,90, 175, 40, fill='lime')

canvas.create_arc(250, 100, 300, 150, start=0, extent=75, fill='purple')

colour_entry = Entry(window)
colour_entry.pack()

def change_colour():
    new_colour = colour_entry.get()
    canvas.itemconfig(my_rectangle, fill=new_colour)


button = Button(window, text="Change Colour", command=change_colour)
button.pack()


def make_it_blue(event):
    canvas.itemconfig(my_rectangle, fill='darkblue')


def move_rect_left(event):
    canvas.move(my_rectangle, -10, 0)


canvas.bind_all('b', make_it_blue)
canvas.bind_all('<Left>', move_rect_left)
window.mainloop()