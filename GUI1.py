import tkinter as tk
window = tk.Tk()
window.title("My window")
window.geometry("200x100")

var = tk.StringVar()
label = tk.Label(window, textvariable=var,
                 bg="green", font=("Arial", 12), width=15, height=2)
label.pack()    #自动放置部件

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("You hit me")
    else:
        on_hit = False
        var.set("")
btn = tk.Button(window, text="Click me", width=15, height=2, command=hit_me)
btn.pack()
btn["text"] = "Click me"

window.mainloop()

