import tkinter as tk
import random
# ------------------------------------------------------------------------------
def click():
    label["text"] = random.choice(["大吉", "吉", "中吉", "小吉", "末吉", "凶"])
    label.update()
# ------------------------------------------------------------------------------
root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("600x400+400+100")
root.resizable(False, False)

cvs = tk.Canvas(root, width=600, height=400, bg="skyblue")
cvs.pack()

img = tk.PhotoImage(file='./sample01.png')
cvs.create_image(300, 200, image=img)

# 矩形
# cvs.create_rectangle(x, y, x+width, y+height,
#                     fill=color_in, outline=color_out, width=w, tag=tg)
cvs.create_rectangle(0, 70, 600, 220, fill="white", width=0)

label = tk.Label(root, text="おみくじ", font=("Helvetica",100),
                fg="skyblue", bg="white")
label.place(x=300, y=150, anchor="c")

btn = tk.Button(root, text="引く",font=("Helvetica",30),
                fg="#555555", bg="#ffffff", borderwidth=0,
                cursor="pointinghand", command=click)
btn.place(x=300, y=270, anchor="c")

root.mainloop()