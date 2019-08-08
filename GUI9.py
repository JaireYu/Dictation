#Frame: 框架，主要用来归置部件
import tkinter as tk
window = tk.Tk()
window.title('My window')
window.geometry("200x200")
tk.Label(window, text="on the window").pack()

frm = tk.Frame(window)  #主框架
frm.pack()

frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)   #主框架的基础上创建两个Frame
frm_l.pack(side = "left")   #一个放在左边
frm_r.pack(side = "right")  #另一个放在右边

tk.Label(frm_l, text="On the frm_l1").pack()
tk.Label(frm_l, text="On the frm_l2").pack()    #左边放两个label
tk.Label(frm_r, text="On the frm_r1").pack()    #右边放两个Label

window.mainloop()