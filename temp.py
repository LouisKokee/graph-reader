import tkinter as tk
from Class_tkinter import *
from PIL import ImageTk, Image

HEIGHT = 700
WIDTH = 1000
source_image_path = 'source_figures/xaPre_height_mvw.png'

root = tk.Tk()



# set initial size
canvas = tk.Canvas(root, height=HEIGHT, width=HEIGHT)
canvas.pack()

# --- frame 1 ---
frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.4)

button = tk.Button(frame, text='ma nibba')
button.place(x=50, y=50)

label = tk.Label(frame, text='Label test lol', bg='yellow')
label.pack()

entry = tk.Entry(frame, bg='green')
entry.pack()

# --- frame 2: full picture ---
frame2 = tk.Frame(root, bg='yellow')
frame2.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.9)

img = ImageTk.PhotoImage(Image.open(source_image_path))
image_window = ScrollableImage(frame2, image=img)
image_window.pack()

root.mainloop()