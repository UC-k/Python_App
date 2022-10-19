import tkinter as tk
# --------------------
# 関数
# --------------------
def start():
    global flg
    flg = 0
    ttl_lbl.place(x=300, y=30, anchor="c")
    for i in range(10):
        check_btn[i].place(x=160, y=80+60*i, anchor="nw")
    end_btn.place(x=500, y=660, anchor="c")
    check()

def check():
    global flg
    if flg == 0:
        for i in range(10):
            if var[i].get() == True:
                answer_lbl[i].place(x=180, y=110+60*i, anchor="nw")
            elif var[i].get() == False:
                answer_lbl[i].place_forget()
        root.after(100, check)
    else:
        return

# after処理をとめる
def flg_up():
    global flg
    flg += 1
    after_end()

def after_end():
    for i in range(10):
        ttl_lbl.place_forget()
        check_btn[i].place_forget()
        answer_lbl[i].place_forget()
    end_btn.place_forget()
    end_lbl.place(x=300, y=350, anchor="c")

# --------------------
# 変数
# --------------------
flg = 0
# --------------------
# ウィンドウ
# --------------------
root = tk.Tk()
root.title("ボタンで隠れたり見えたりするやつ")
root.geometry("600x700")
root.config(bg="white")
root.resizable(False, False)
# --------------------
# ウィジェット
# --------------------
ttl_lbl = tk.Label(root, text="ここにタイトルを表示", font=("System", 36),
                    fg="#1212aa", bg="white")

var = [None]*10
question = [
    "質問1の内容を表示します",
    "質問2の内容を表示します",
    "質問3の内容を表示します",
    "質問4の内容を表示します",
    "質問5の内容を表示します",
    "質問6の内容を表示します",
    "質問7の内容を表示します",
    "質問8の内容を表示します",
    "質問9の内容を表示します",
    "質問10の内容を表示します"
]
check_btn = [None]*10
for i in range(10):
    var[i] = tk.BooleanVar()
    var[i].set(False)
    check_btn[i] = tk.Checkbutton(root, font=("System", 16), variable=var[i],
                                fg="grey", bg="white", text=question[i])

answer = [
    "質問1の答え",
    "質問2の答え",
    "質問3の答え",
    "質問4の答え",
    "質問5の答え",
    "質問6の答え",
    "質問7の答え",
    "質問8の答え",
    "質問9の答え",
    "質問10の答え"
]
answer_lbl = [None]*10
for i in range(10):
    answer_lbl[i] = tk.Label(root, font=("system", 16),
                            fg="red", bg="white", text=answer[i])

end_btn = tk.Button(root, text="after処理を止める", 
                    fg="green", highlightbackground="white", command=flg_up)

end_lbl = tk.Label(text="End", font=("Helvetica", 40), fg="orangered", bg="white")
# --------------------
start()
root.mainloop()