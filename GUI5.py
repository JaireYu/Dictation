#Scale(Number changing)
import tkinter as tk

window = tk.Tk()
window.title("Window")
window.geometry("200x200")

var1=tk.StringVar()
label = tk.Label(window, bg="yellow", width=40, text="empty")
label.pack()

def print_selection(v): #v是隐含的参数
    label.config(text="you have selected the option" + v)  #设置

s = tk.Scale(window, label="Try me", from_=5, to_=10, orient=tk.HORIZONTAL, length=200, showvalue=0,
             tickinterval=3, resolution=0.01, command=print_selection)  #方向，间隔，精度，函数
s.pack()

window.mainloop()