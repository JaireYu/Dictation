#Messagebox(弹窗)
import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("My window")
window.geometry("200x200")

def hit_me():
    #messagebox.showinfo(title="Hi", message="Hahaha")
    #messagebox.showwarning(title="Hi", message="Nonono")
    #messagebox.showerror(title="Hi", message="WTF")
    #str = messagebox.askquestion(title="Hi", message="Hahaha") #return yes or no
    #if(str == "yes"):
    #    pass
    #else:
    #    pass
    #print(messagebox.askyesno(title="Hi", message="Hahaha"))    #return True or False
    print(messagebox.askokcancel(title="Hi", message="Hahaha")) #return True or False

tk.Button(window, text="hit me", command=hit_me).pack()

window.mainloop()