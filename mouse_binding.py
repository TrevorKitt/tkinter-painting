from tkinter import *

window = Tk()
window.title('my gui')

canvas = Canvas(window, width=400, height=400)
canvas.pack()

circle = canvas.create_oval(100, 200, 160, 230, fill='red')
blue_rect = canvas.create_rectangle(50, 50, 70, 80, fill='blue')


def move_character(event):
    canvas.move(blue_rect, 10, 0)


def move_character_back(event):
    canvas.move(blue_rect, -10, 0)

        
canvas.bind_all('<Button-1>', move_character)
canvas.bind_all('<Button-3>', move_character_back)

window.mainloop()  # gui main event loop
