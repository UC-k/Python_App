import tkinter as tk
# --------------------
# 関数
# --------------------
def start():
    # 初期化
    reset()
    # 配置
    start_lbl.place(x=400, y=200, anchor="c")
    start_btn.place(x=700, y=350, anchor="c")

def check(var, a, b, c, d):
    global count
    point = var.get()
    if point == 0:count += a
    elif point == 1:count += b
    elif point == 2:count += c
    elif point == 3:count += d

def result_check():
    global count, result_number
    if count <= 40:
        result_number = 0
    elif 40 < count < 120:
        result_number = 1
    elif 120 <= count:
        result_number = 2

def fase1():
    # 消去
    start_lbl.place_forget()
    start_btn.place_forget()
    # 配置
    question_lbl[0].place(x=400, y=50, anchor="c")
    for i in range(4):
        radio_btn_1[i].place(x=300, y=100+50*i, anchor="nw")
    next_btn1.place(x=700, y=350, anchor="c")

def fase2():
    # 消去
    question_lbl[0].place_forget()
    for i in range(4):
        radio_btn_1[i].place_forget()
    next_btn1.place_forget()
    # チェック
    check(var_1, 10, 20, 30, 40)
    print(count)
    # 配置
    question_lbl[1].place(x=400, y=50, anchor="c")
    for i in range(4):
        radio_btn_2[i].place(x=300, y=100+50*i, anchor="nw")
    next_btn2.place(x=700, y=350, anchor="c")

def fase3():
    # 消去
    question_lbl[1].place_forget()
    for i in range(4):
        radio_btn_2[i].place_forget()
    next_btn2.place_forget()
    # チェック
    check(var_2, 30, 0, 0, 10)
    print(count)
    # 配置
    question_lbl[2].place(x=400, y=50, anchor="c")
    for i in range(4):
        radio_btn_3[i].place(x=300, y=100+50*i, anchor="nw")
    next_btn3.place(x=700, y=350, anchor="c")

def fase4():
    global result_number
    # 消去
    question_lbl[2].place_forget()
    for i in range(4):
        radio_btn_3[i].place_forget()
    next_btn3.place_forget()
    # チェック
    check(var_2, 0, 40, 0, 10)
    print(count)
    # 結果チェック
    result_check()
    # 配置
    result_lbl[result_number].place(x=400, y=200, anchor="c")
    # もう一度 or 終了
    again_btn.place(x=570, y=350, anchor="c")
    end_btn.place(x=700, y=350, anchor="c")

def again():
    global result_number
    result_lbl[result_number].place_forget()
    again_btn.place_forget()
    end_btn.place_forget()
    start()

def end():
    root.destroy()

def reset():
    global count, result_number
    # 初期化
    var_1.set(0)
    var_2.set(0)
    var_3.set(0)
    count = 0
    result_number = 0

# --------------------
# ウィンドウ
# --------------------
root = tk.Tk()
root.title("ラジオボタンの項目が変わるやつ")
root.geometry("800x400")
root.config(bg="white")
root.resizable(False, False)
# --------------------
# 変数
# --------------------
count = 0
# --------------------
# ウィジェット
# --------------------
# スタート画面
start_lbl = tk.Label(text="選択肢変わるやつ", font=("Helvetica", 28),
                    fg="black", bg="white")
start_btn = tk.Button(text="はじめる", font=("Helvetica", 16), command=fase1)
# 質問テキスト(ラベル)
question = [
    "ここに１番目の質問が入ります",
    "ここに２番目の質問が入ります",
    "ここに３番目の質問が入ります"
]
result_number = 0
question_lbl = [None]*3
for i in range(3):
    question_lbl[i] = tk.Label(text=question[i], font=("Helvetica", 24),
                                fg="black", bg="white")

# ラジオボタン_1
ITEM_1 = [
    "質問１の選択肢１",
    "質問１の選択肢２",
    "質問１の選択肢３",
    "質問１の選択肢４"
    ]
radio_btn_1 = [None]*4
var_1 = tk.IntVar()
for i in range(4):
    radio_btn_1[i] = tk.Radiobutton(text=ITEM_1[i], font=("Helvetica", 22),
                    value=i, variable=var_1, fg="grey", bg="white")
# 「次へ」ボタン1
next_btn1 = tk.Button(text="次へ", font=("Helvetica", 16), command=fase2)

# ラジオボタン_2
ITEM_2 = [
    "質問２の選択肢１",
    "質問２の選択肢２",
    "質問２の選択肢３",
    "質問２の選択肢４"
    ]
radio_btn_2 = [None]*4
var_2 = tk.IntVar()
for i in range(4):
    radio_btn_2[i] = tk.Radiobutton(text=ITEM_2[i], font=("Helvetica", 22),
                    value=i, variable=var_2, fg="grey", bg="white")
# 「次へ」ボタン2
next_btn2 = tk.Button(text="次へ", font=("Helvetica", 16), command=fase3)

# ラジオボタン_3
ITEM_3 = [
    "質問３の選択肢１",
    "質問３の選択肢２",
    "質問３の選択肢３",
    "質問３の選択肢４"
    ]
radio_btn_3 = [None]*4
var_3 = tk.IntVar()
for i in range(4):
    radio_btn_3[i] = tk.Radiobutton(text=ITEM_3[i], font=("Helvetica", 22),
                    value=i, variable=var_3, fg="grey", bg="white")
# 「次へ」ボタン3
next_btn3 = tk.Button(text="次へ", font=("Helvetica", 16), command=fase4)

# 結果
result = [
    "結果の表示その１",
    "結果の表示その２",
    "結果の表示その３"
]
result_lbl = [None]*3
for i in range(3):
    result_lbl[i] = tk.Label(text=result[i], font=("Helvetica", 20),
                            fg="red", bg="white")

# もう一度 or 終了
again_btn = tk.Button(text="もう一度", font=("Helvetica", 18), command=again)
end_btn = tk.Button(text="終了する", font=("Helvetica", 18), command=end)
# --------------------
start()
root.mainloop()