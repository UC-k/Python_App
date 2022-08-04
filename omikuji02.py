import tkinter as tk
import random
# ------------------------------------------------------------------------------
def click():
    label["text"] = random.choice(["大吉", "吉", "中吉", "小吉", "末吉", "凶"])
    label.update()
# ------------------------------------------------------------------------------
root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("500x500+400+100")
root.configure(bg="#323232")
root.resizable(False, False)

label = tk.Label(root, text="おみくじ", font=("Helvetica",100),
                fg="skyblue", bg=None)
label.place(x=250, y=180, anchor="c")

btn = tk.Button(root, text="引く",font=("Helvetica",30),
                fg="#555555", bg="#ffffff", borderwidth=0,
                cursor="pointinghand", command=click)
btn.place(x=250, y=350, anchor="c")

root.mainloop()