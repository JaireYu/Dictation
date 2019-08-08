#MuliChooseButton(Radiobutton)
import tkinter as tk

window = tk.Tk()
window.title("Window")
window.geometry("200x200")

var1=tk.StringVar()
label = tk.Label(window, bg="yellow", width=40, text="empty")
label.pack()

def print_selection():
    label.config(text="you have selected the option" + var1.get())  #设置

r1 = tk.Radiobutton(window, text="Option A",
                    variable=var1, value = 'A',
                    command=print_selection)    #当选择这个button时，var1就会被赋值为A
r1.pack()

r2 = tk.Radiobutton(window, text="Option B",
                    variable=var1, value = 'B',
                    command=print_selection)    #当选择这个button时，var1就会被赋值为B
r2.pack()

r3 = tk.Radiobutton(window, text="Option C",
                    variable=var1, value = 'C',
                    command=print_selection)    #当选择这个button时，var1就会被赋值为C
r3.pack()



window.mainloop()