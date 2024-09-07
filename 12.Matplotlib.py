from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import tkinter

tk = tkinter.Tk()
tk.title("Matplotlib")
tk.geometry("400x200")

def plots():
    x=np.random.normal(20000,2000,4000)
    plt.hist(x,50)
    plt.show()

btn = Button(tk, text="Plot Graph", command = plots)
btn.pack()



tk.mainloop()
