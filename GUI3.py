#Listbox
import tkinter as tk

window = tk.Tk()
window.title("Window")
window.geometry("200x200")

var1=tk.StringVar()
label = tk.Label(window, bg="yellow", width=4, textvariable=var1)
label.pack()

def print_word():
    var =lb.get(lb.curselection())  #获取listbox中的选中项
    var1.set(var)   #设置label的显示为listbox的选中项

b1=tk.Button(window, text="insert point",
             width=15, height=2, command=print_word)

b1.pack()

var2=tk.StringVar() #下面是设置listbox的三种方式元组，后面插入和索引插入
var2.set((11,22,33,44))
lb = tk.Listbox(window,listvariable=var2)
list_items =[1,2,3,4]
for item in list_items:
    lb.insert('end', item)
lb.insert(1, 'first')   #在listbox的第一位插入
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()