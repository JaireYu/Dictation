#Menu
import tkinter as tk
window = tk.Tk()
window.title("Window")
window.geometry("200x200")

l = tk.Label(window, text="", bg="yellow")
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text="do"+str(counter))
    counter += 1

menubar = tk.Menu(window) #menubar是window的菜单栏

filemenu = tk.Menu(menubar, tearoff=0)  #filemenu是menubar的一个菜单单元
menubar.add_cascade(label='file', menu=filemenu)    #将上面的菜单单元命名为file，并添加到菜单栏
filemenu.add_command(label="New", command=do_job)   #为菜单单元添加选项
filemenu.add_command(label="Open", command=do_job)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

submenu = tk.Menu(filemenu, tearoff=0) #submenu是filemenu的子菜单
filemenu.add_cascade(label="Edit", menu=submenu, underline=0)   #视filemenu为一个菜单栏，向其中加入子菜单
submenu.add_command(label="Sub1", command=do_job)

window.config(menu=menubar)
window.mainloop()