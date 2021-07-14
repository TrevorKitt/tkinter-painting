from tkinter import *

window = Tk()
window.title('tkinter face')

canvas = Canvas(window, width=600, height=600)
canvas.pack()

# eyes
eye_w = 55  # eye width. Measures across from one outer edge to the other
edge_w = 2  # edge width. Thickness of the outer edge
pupil_w = 13  # pupil width
pid = (eye_w - pupil_w) / 2  # pupil inner distance. This is how far into the inner part of the eye the edge of the pupil will be
# left eye
le_l_edge = 140  # position for the left edge of the left eye
le_t_edge = 150  # position for the top edge of the left eye
le_outer = canvas.create_oval(le_l_edge, le_t_edge, le_l_edge + eye_w, le_t_edge + eye_w, fill='black')  # black rim
le_inner = canvas.create_oval(le_l_edge + edge_w, le_t_edge + edge_w,
                              le_l_edge + eye_w - edge_w, le_t_edge + eye_w - edge_w, fill='white')  # white inside
le_pupil = canvas.create_oval(le_l_edge + pid, le_t_edge + pid, le_l_edge + pid + pupil_w,
                              le_t_edge + pid + pupil_w, fill='black')  # black pupil
# right eye
re_l_edge = 240  # position for the left edge of the right eye
re_t_edge = 150  # position for the top edge of the right eye
re_outer = canvas.create_oval(re_l_edge, re_t_edge, re_l_edge + eye_w, re_t_edge + eye_w, fill='black')  # black rim
re_inner = canvas.create_oval(re_l_edge + edge_w, re_t_edge + edge_w,
                              re_l_edge + eye_w - edge_w, re_t_edge + eye_w - edge_w, fill='white')  # white inside
re_pupil = canvas.create_oval(re_l_edge + pid, re_t_edge + pid, re_l_edge + pid + pupil_w,
                              re_t_edge + pid + pupil_w, fill='black')  # black pupil


def left_arrow(event):
    pd = 5
    canvas.coords(le_pupil, le_l_edge + pd, le_t_edge + pid, le_l_edge + pd + pupil_w,
                              le_t_edge + pid + pupil_w)
    canvas.coords(re_pupil, re_l_edge + pd, re_t_edge + pid, re_l_edge + pd + pupil_w,
                  re_t_edge + pid + pupil_w)


def up_arrow(event):
    pd = 5
    canvas.coords(le_pupil, le_l_edge + pid, le_t_edge + pd, le_l_edge + pid + pupil_w,
                  le_t_edge + pd + pupil_w)
    canvas.coords(re_pupil, re_l_edge + pid, re_t_edge + pd, re_l_edge + pid + pupil_w,
                  re_t_edge + pd + pupil_w)


def right_arrow(event):
    pd = 5
    canvas.coords(le_pupil, le_l_edge + eye_w - edge_w - pupil_w - pd, le_t_edge + pid, le_l_edge + eye_w - edge_w - pd,
                  le_t_edge + pid + pupil_w)
    canvas.coords(re_pupil, re_l_edge + eye_w - edge_w - pupil_w - pd, re_t_edge + pid, re_l_edge + eye_w - edge_w - pd,
                  re_t_edge + pid + pupil_w)


def down_arrow(event):
    pd = 5
    canvas.coords(le_pupil, le_l_edge + pid, le_t_edge + eye_w - edge_w - pupil_w - pd, le_l_edge + pid + pupil_w,
                  le_t_edge + eye_w - edge_w - pd)
    canvas.coords(re_pupil, re_l_edge + pid, re_t_edge + eye_w - edge_w - pupil_w - pd, re_l_edge + pid + pupil_w,
                  re_t_edge + eye_w - edge_w - pd)


def space(event):
    canvas.coords(le_pupil, le_l_edge + pid, le_t_edge + pid, le_l_edge + pid + pupil_w, le_t_edge + pid + pupil_w)
    canvas.coords(re_pupil, re_l_edge + pid, re_t_edge + pid, re_l_edge + pid + pupil_w, re_t_edge + pid + pupil_w)


def print_message(event):
    canvas.create_text(300, 100, fill='darkblue', font='Ariel 20 italic', text="Hmm... where did I put my glasses?")


canvas.bind_all('<Left>', left_arrow)
canvas.bind_all('<Up>', up_arrow)
canvas.bind_all('<Right>', right_arrow)
canvas.bind_all('<Down>', down_arrow)
canvas.bind_all('<space>', space)
canvas.bind_all('p', print_message)

window.mainloop()  # gui main event loop
