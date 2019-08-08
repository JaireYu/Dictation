#checkbottun
import tkinter as tk

window = tk.Tk()
window.title("Window")
window.geometry("200x200")

label = tk.Label(window, bg="yellow", width=40, text="empty")
label.pack()

def print_selection():
    if((var1.get() == 1) & (var2.get() == 1)):
        label.config(text="I love both")  #设置
    elif ((var1.get() == 1) & (var2.get() == 0)):
        label.config(text="I love {}".format("Python"))
    elif ((var1.get() == 0) & (var2.get() == 1)):
        label.config(text="I love {}".format("C++"))
    else:
        label.config(text="I love neither")

var1 = tk.IntVar()
var2 = tk.IntVar()
cb1 = tk.Checkbutton(window, text="Python", variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
cb2 = tk.Checkbutton(window, text="C++", variable=var2, onvalue=1, offvalue=0,
                    command=print_selection)
cb1.pack()
cb2.pack()

window.mainloop()