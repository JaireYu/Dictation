import tkinter as tk

window = tk.Tk()
window.title("Window")
window.geometry("200x200")

e = tk.Entry(window, show='*')  #show='*'输入密码时的亚子
e.pack()                        #e是一个Entry

def insert_point():
    var =e.get()
    t.insert("insert", var) #插入在光标处

def insert_end():
    var =e.get()
    t.insert("end", var)    #插入在结尾处

def insert_pos():
    var =e.get()
    t.insert(1.1, var)      #插入在第一行第一个字符后面

b1=tk.Button(window, text="insert point",
             width=15, height=2, command=insert_point)

b1.pack()

b2=tk.Button(window, text="insert end",
             width=15, height=2, command=insert_end)

b2.pack()

t = tk.Text(window, height=2)
t.pack()        #t是文本框

window.mainloop()