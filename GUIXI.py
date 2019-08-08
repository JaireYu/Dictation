#place objects
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("My window")
window.geometry("200x200")
"""""""""   #方法1: pack+side
tk.Label(window, text=1).pack(side="top")
tk.Label(window, text=1).pack(side="bottom")
tk.Label(window, text=1).pack(side="left")
tk.Label(window, text=1).pack(side="right")
"""

"""""""""   #方法2: grid + row + column
for i in range(4):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, 
        padx=10, pady=10) #padx, pady是用作扩展每一个label的占地面积，是可选选项
"""
#方法3：place + pixel(x, y)
tk.Label(window, text=1).place(x=10, y=100, anchor="nw") #anchor对于图片效果明显指出铆定的角
window.mainloop()