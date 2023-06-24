#coding:utf-8
import tkinter as tk

#window
root = tk.Tk()
root.geometry("600x500")

#canvas
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x=0, y=0)
for x in 600:

    #circle
    canvas.create_oval(x -20, 200 - 20, x + 20, 200 + 20)
    #line
    canvas.create_line(x, 220, x, 250)
    canvas.create_line(x, 227, x + 30, 215)
    canvas.create_line(x, 227, x-30, 215)
    canvas.create_line(x, 250, x+25, 290)
    canvas.create_line(x, 250, x-25, 290)

root.mainloop()