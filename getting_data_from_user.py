from tkinter import *


def convert():
    if inch_data.get() != "":
        cm_string = str(int(inch_data.get())*2.54)
        cm_display.configure(text=cm_string)


window = Tk()
window.title('Inch to cm Converter')

inch_data = Entry(window, text="")
inch_data.pack()

cm_display = Label(window, text="")
cm_display.pack()

button = Button(window, text='Convert to cm', command=convert)
button.pack()

window.mainloop()

#add a button and a an text Entry box to your window.
#When a colour is typed into that text box and the button is clicked, change a shape on the screen to match that colour