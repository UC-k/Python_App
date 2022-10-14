import tkinter as tk
# ----------------------------------------
# 関数
# ----------------------------------------
def start():
    global cnt
    cnt = 0
    start_lbl.place(x=300, y=200, anchor="c")
    start_btn.place(x=480, y=520, anchor="c")

    q_text.delete("1.0", tk.END)
    q_text.place_forget()
    restart_btn.place_forget()
    end_btn.place_forget()

    print(cnt)


def fase1():
    start_lbl.place_forget()
    start_btn.place_forget()
    for i in range(4):
        radio_btn[i].place(x=150, y=280+50*i)
    q_text.place(x=300, y=150, anchor="c")
    q_text.insert("1.0", question[0])
    q_next1.place(x=480, y=520, anchor="c")

    print(cnt)


def fase2():
    global cnt
    point = var.get()
    cnt += point
    var.set(0)
    q_text.delete("1.0", tk.END)
    q_text.insert("1.0", question[1])
    q_next1.place_forget()
    q_next2.place(x=480, y=520, anchor="c")
    
    print(cnt)


def fase3():
    global cnt
    point = var.get()
    cnt += point
    var.set(0)
    q_text.delete("1.0", tk.END)
    q_text.insert("1.0", question[2])
    q_next2.place_forget()
    q_next3.place(x=480, y=520, anchor="c")

    print(cnt)


def fase4():
    global cnt
    point = var.get()
    cnt += point
    var.set(0)
    q_text.delete("1.0", tk.END)
    q_text.insert("1.0", question[3])
    q_next3.place_forget()
    q_next4.place(x=480, y=520, anchor="c")

    print(cnt)


def result():
    global cnt
    point = var.get()
    cnt += point
    var.set(0)
    q_text.delete("1.0", tk.END)
    rspns = 0
    if (0<=cnt<=2):
        rspns = 0
    elif (3<=cnt<=5):
        rspns = 1 
    elif (6<=cnt<=10):
        rspns = 2
    elif 11<=cnt:
        rspns = 3
    q_text.insert("1.0", answer[rspns])

    q_next4.place_forget()
    for i in range(4):
        radio_btn[i].place_forget()
    
    restart_btn.place(x=480, y=470, anchor="c")
    end_btn.place(x=480, y=520, anchor="c")

    print(cnt)

    
def end():
    root.destroy()
# ----------------------------------------
# ウィンドウの準備
# ----------------------------------------
root = tk.Tk()
root.title("count")
root.geometry("600x600+400+0")
root.resizable(False, False)
# ----------------------------------------
# 質問の準備
# ----------------------------------------
question = [
    "質問1\nここに質問1の内容が入ります。",
    "質問2\nここに質問2の内容が入ります。",
    "質問3\nここに質問3の内容が入ります。",
    "質問4\nここに質問4の内容が入ります。",
    ]
answer = [
    "0点〜2点",
    "3点〜5点",
    "6点〜10点",
    "11点〜"
]
# ----------------------------------------
# ラジオボタンの準備
# ----------------------------------------
radio_btn = [None]*6
ITEM = ["とてもそう思う","そう思う", "あまり思わない", "思わない"]
var = tk.IntVar()
for i in range(4):
    radio_btn[i] = tk.Radiobutton(text=ITEM[i], font=("Helvetica", 36),
                    value=i, variable=var)
# ----------------------------------------
# 変数の準備
# ----------------------------------------
cnt = 0
# ----------------------------------------
# ラベル，ボタンの準備
# ----------------------------------------
start_lbl = tk.Label(text="選択肢に重みがあるタイプ", font=("Futura", 40))
start_btn = tk.Button(text="> start", font=("Helvetica", 40), command=fase1)
q_text = tk.Text(width=40, height=7, font=("System", 20))
q_next1 = tk.Button(text="> next", font=("Helvetica", 40), command=fase2)
q_next2 = tk.Button(text="> next", font=("Helvetica", 40), command=fase3)
q_next3 = tk.Button(text="> next", font=("Helvetica", 40), command=fase4)
q_next4 = tk.Button(text="> next", font=("Helvetica", 40), command=result)
# ----------------------------------------
restart_btn = tk.Button(text="もう一度", font=("Helvetica", 20), command=start)
end_btn = tk.Button(text="終了する", font=("Helvetica", 20), command=end)
# ----------------------------------------
start()
root.mainloop()