import tkinter as tk
# ----------------------------------------
# 関数
# ----------------------------------------
def start():
    for i in result_lbl:
        i.place_forget()
    again_btn.place_forget()
    var.set(0)
    start_lbl.place(x=300, y=200, anchor="c")
    start_btn.place(x=300, y=350, anchor="c")

def fase1():
    start_lbl.place_forget()
    start_btn.place_forget()
    fase1_lbl.place(x=300, y=100, anchor="c")
    fase1_btn.place(x=480, y=520, anchor="c")
    for i in range(0, 2):
        radio_btn[i].place(x=250, y=250+80*i)

def branch1():
    fase1_lbl.place_forget()
    fase1_btn.place_forget()
    for i in range(0, 2):
        radio_btn[i].place_forget()
    var_check = var.get()
    if var_check == 0:
        fase2_1()
    elif var_check == 1:
        fase2_2()

def fase2_1(): # fase1 -> Yes
    var.set(2)
    fase2_1lbl.place(x=300, y=100, anchor="c")
    result_btn.place(x=480, y=520, anchor="c")
    for i in range(2, 4):
        radio_btn[i].place(x=250, y=250+80*(i-2))

def fase2_2(): # fase1 -> No
    var.set(4)
    fase2_2lbl.place(x=300, y=100, anchor="c")
    result_btn.place(x=480, y=520, anchor="c")
    for i in range(4, 6):
        radio_btn[i].place(x=250, y=250+80*(i-4))

def result():
    fase2_1lbl.place_forget()
    fase2_2lbl.place_forget()
    result_btn.place_forget()
    for i in range(6):
        radio_btn[i].place_forget()
    var_check = var.get()
    if var_check == 2:
        A_lbl.place(x=300, y=300, anchor="c")
    elif var_check == 3:
        B_lbl.place(x=300, y=300, anchor="c")
    elif var_check == 4:
        C_lbl.place(x=300, y=300, anchor="c")
    elif var_check == 5:
        D_lbl.place(x=300, y=300, anchor="c")
    again_btn.place(x=480, y=520, anchor="c")
# ----------------------------------------
# ウィンドウの準備
# ----------------------------------------
root = tk.Tk()
root.title("Branch")
root.geometry("600x600")
root.resizable(False, False)
# ----------------------------------------
# ラジオボタンの準備
# ----------------------------------------
radio_btn = [None]*6
ITEM = ["AorB","CorD", "A", "B", "C", "D"]
var = tk.IntVar()
for i in range(6):
    radio_btn[i] = tk.Radiobutton(text=ITEM[i], font=("Helvetica", 36),
                    value=i, variable=var)
# ----------------------------------------
# ラベル，ボタンの準備
# ----------------------------------------
start_lbl = tk.Label(text="ABCD診断", font=("Futura", 100))
start_btn = tk.Button(text="> start", font=("Helvetica", 40), command=fase1)
# ----------------------------------------
fase1_lbl = tk.Label(text="AorBorCorD", font=("Futura", 80))
fase1_btn = tk.Button(text="> fase2", font=("Helvetica", 40), command=branch1)
# ----------------------------------------
fase2_1lbl = tk.Label(text="AorB", font=("Futura", 80))
fase2_2lbl = tk.Label(text="CorD", font=("Futura", 80))
# ----------------------------------------
result_btn = tk.Button(text="result", font=("Helvetica", 40), command=result)
A_lbl = tk.Label(text="A", font=("Futura", 80))
B_lbl = tk.Label(text="B", font=("Futura", 80))
C_lbl = tk.Label(text="C", font=("Futura", 80))
D_lbl = tk.Label(text="D", font=("Futura", 80))
result_lbl = [A_lbl, B_lbl, C_lbl, D_lbl]
# ----------------------------------------
again_btn = tk.Button(text="> again", font=("Helvetica", 40), command=start)
# ----------------------------------------
start()
root.mainloop()