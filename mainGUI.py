#coding=utf-8
import GetAudio
import tkinter as tk
from tkinter import font
import os
import Translate
import time
import _thread
from tkinter import messagebox
window = tk.Tk()
window.title('Jaire\'s Dictation')
window.geometry("1920x1080")

frm = tk.Frame(window)  #主框架
frm.pack()

frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)   #主框架的基础上创建两个Frame
frm_l.pack(side = "left")   #一个放在左边
frm_r.pack(side = "right")  #另一个放在右边

ft = tk.font.Font(family='Times New Roman', size=35, weight=tk.font.BOLD)   #显示大号英文
ft1 = tk.font.Font(family='Times New Roman', size=16, weight=tk.font.BOLD)  #
ft2 = tk.font.Font(family='Segoe UI', size=10, weight=tk.font.BOLD) #英文功能显示
ft3 = tk.font.Font(family='Consolas', size=14, weight=tk.font.BOLD) #Entry
ft4 = tk.font.Font(family='Times New Roman', size=20, weight=tk.font.BOLD)  #Listbox
ft5 = tk.font.Font(family='MV Boli', size=20, weight=tk.font.BOLD) #功能指示
ft6 = tk.font.Font(family='黑体', size=10)  #汉语标签

entry1 = tk.Entry(window, width=20, font=ft3)
entry1.insert(0,"在此输入文件名")
entry1.place(x=50, y=50, anchor="nw")

var2=tk.StringVar()
var2.set(())
lb = tk.Listbox(window,listvariable=var2, font=ft1, bd=4, height=25, width=26)
lb.place(x=50, y=100, anchor="nw")

var1=tk.StringVar()
label = tk.Label(window, width=20,bg="Honeydew", height=1, textvariable=var1, font=ft, anchor='nw')
label.place(x=400, y=50, anchor="nw")

var3=tk.StringVar()
label2 = tk.Label(window, bg="yellow",width=65, height=12, textvariable=var3, font=ft4, anchor='nw')
label2.place(x=400, y=150, anchor="nw")

label3 = tk.Label(window, bg="yellow", font= ft6, width=8, height=1, text="学习模式", anchor='nw')
label3.place(x=1000, y=50, anchor="nw")

label4 = tk.Label(window, bg="yellow", font= ft6, width=6, height=1, text="已开始", anchor='nw')
label4.place(x=1000, y=85, anchor="nw")

sp = GetAudio.youdao()
wordlist = []
translate = []

timevar = tk.IntVar()
timevar.set(3)

def Change_time(v):
    timevar.set(float(v))

s = tk.Scale(window, label="", from_=1, to_=7, orient=tk.HORIZONTAL, length=400, showvalue=1,
             tickinterval=1, resolution=0.01, command=Change_time, font=ft2)  #方向，间隔，精度，函数
s.place(x=1000, y=650, anchor='nw')

modevar = tk.IntVar()   #mode标志位0，学习模式， 1，自测模式， 2， 听写模式
modevar.set(0)

Pause = False

def NewList():
    str = messagebox.askquestion(title="Attention", message="Do you want to replace the current wordlist?")  # return yes or no
    if(str == "yes"):
        global wordlist
        wordlist = []
        global translate
        translate = []
        var2.set(())
        var1.set("")
        var3.set("")
    else:
        pass

def Quit():
    str = messagebox.askquestion(title="EXIT", message="Quit anyway?")  # return yes or no
    if(str == "yes"):
        window.quit()
    else:
        pass

menubar = tk.Menu(window) #menubar是window的菜单栏

filemenu = tk.Menu(menubar, tearoff=0)  #filemenu是menubar的一个菜单单元
menubar.add_cascade(label='WordList', menu=filemenu)    #将上面的菜单单元命名为file，并添加到菜单栏
filemenu.add_command(label="New", command=NewList)   #为菜单单元添加选项
menubar.add_cascade(label="Exit", command=Quit)
window.config(menu=menubar)

def continueplay():
    global Pause
    Pause = False
    while ((modevar.get() == 2) & (Pause == False)):
        label4.config(text = "已开始")
        path = lb.get(lb.curselection())
        word = path.strip()
        GetAudio.play(word, sp)
        var1.set(str(path))
        var3.set(translate[list(lb.curselection())[0]].strip())
        time.sleep(timevar.get())
        curindex = lb.curselection()
        templist = list(curindex)
        lb.select_clear((templist[0]))
        lb.selection_set((templist[0] + 1))


def play():
    if(modevar.get() == 0):
        path = lb.get(lb.curselection())
        word=path.strip()
        GetAudio.play(word, sp)
        var1.set(str(path))
        var3.set(translate[list(lb.curselection())[0]].strip())
    elif(modevar.get() == 1):
        path = lb.get(lb.curselection())
        word = path.strip()
        GetAudio.play(word, sp)
        var1.set(str(path))
        var3.set("")
    else:
        _thread.start_new_thread(continueplay, ())

def DownloadWordlist():
    global sp
    var = entry1.get()
    sp.downloadwords("{}.txt".format(str(var)))
    fr = open("{}.txt".format(str(var)))
    global wordlist
    wordlist=fr.readlines()
    var2.set(tuple(wordlist))
    global translate
    translate = Translate.Translate("{}.txt".format(str(var)), sp)

def movetonext():
    curindex = lb.curselection()
    templist = list(curindex)
    lb.select_clear((templist[0]))
    lb.selection_set((templist[0]+1))
    play()

def movetolast():
    curindex = lb.curselection()
    templist = list(curindex)
    lb.select_clear((templist[0]))
    lb.selection_set((templist[0]-1))
    play()

def pause():
    global Pause
    if(Pause == False):
        Pause = True
        label4.config(text = "已暂停")

def GetChinese():
    var3.set(translate[list(lb.curselection())[0]].strip())

btn1 = tk.Button(window, text = "Download", command=DownloadWordlist, width=10, font=ft2)
btn1.place(x=255, y=50, anchor="nw")

btn2 = tk.Button(window, text="play", width=7, height=1, command=play, font = ft2)
btn2.place(x=500, y=670, anchor='nw')

btn3 = tk.Button(window, text="next", width=7, height=1, command=movetonext, font = ft2)
btn3.place(x=700, y=670, anchor='nw')

btn4 = tk.Button(window, text="last", width=7, height=1, command=movetolast, font = ft2)
btn4.place(x=400, y=670, anchor='nw')

btn5 = tk.Button(window, text="pause", width=7, height=1, command=pause, font = ft2)
btn5.place(x=600, y=670, anchor='nw')

btn6 = tk.Button(window, text="Chinese", width=7, height=1, command=GetChinese, font = ft2)
btn6.place(x=800, y=670, anchor='nw')

def show_mode():
    if(modevar.get() == 0):
        label3.config(text="学习模式")  #设置
    elif(modevar.get() == 1):
        label3.config(text="自测模式")
    else:
        label3.config(text="听写模式")

label5 = tk.Label(window, text="Choose Mode", width=11,height=1, font=ft5)
label5.place(x=1100, y=70, anchor="nw")

label5 = tk.Label(window, text="Function Buttons", width=27,height=1, font=ft5)
label5.place(x=400, y=580, anchor="nw")

label5 = tk.Label(window, text="Dictation Speed", width=15,height=1, font=ft5)
label5.place(x=1050, y=580, anchor="nw")

r1 = tk.Radiobutton(window, text="Learning",
                    variable=modevar, value = 0, font=ft2,
                    command=show_mode)    #当选择这个button时，var1就会被赋值为A
r1.place(x=1300, y=50, anchor="nw")

r2 = tk.Radiobutton(window, text="Test self",
                    variable=modevar, value = 1, font=ft2,
                    command=show_mode)    #当选择这个button时，var1就会被赋值为B
r2.place(x=1300, y=80, anchor="nw")

r3 = tk.Radiobutton(window, text="Dictation",
                    variable=modevar, value = 2, font=ft2,
                    command=show_mode)    #当选择这个button时，var1就会被赋值为C
r3.place(x=1300, y=110, anchor="nw")
window.mainloop()

