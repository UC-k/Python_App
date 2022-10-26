# ----------------------------------------
# tbi(tournament-branch-image)
# ----------------------------------------
# 画像は.pyファイルと同じ場所に保存してください
# ----------------------------------------
# ＜分岐で画像を変える＞
# ・画像を置くためにキャンバスを生成
# ・使用する画像を定義
# ・関数「result」で描画
# ・関数「start」で画像の初期化（消去）
import tkinter as tk
# ----------------------------------------
# 関数
# ----------------------------------------
def start():
    # 【★★★追加★★★】画像の消去
    cvs.delete("result")
    # --------------------
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
        radio_btn[i].place(x=200, y=250+80*i)

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
    fase2_1btn.place(x=480, y=520, anchor="c")
    for i in range(2, 4):
        radio_btn[i].place(x=200, y=250+80*(i-2))

def fase2_2(): # fase1 -> No
    var.set(4)
    fase2_2lbl.place(x=300, y=100, anchor="c")
    fase2_2btn.place(x=480, y=520, anchor="c")
    for i in range(4, 6):
        radio_btn[i].place(x=200, y=250+80*(i-4))
        
def branch2():
    fase2_1lbl.place_forget()
    fase2_2lbl.place_forget()
    fase2_1btn.place_forget()
    fase2_2btn.place_forget()
    for i in range(2, 6):
        radio_btn[i].place_forget()
    var_check = var.get()
    if var_check == 2:
        fase3_1()
    elif var_check == 3:
        fase3_2()
    elif var_check == 4:
        fase3_3()
    elif var_check == 5:
        fase3_4()

def fase3_1(): # fase2_1 -> Yes
    var.set(6)
    fase3_1lbl.place(x=300, y=100, anchor="c")
    result_btn.place(x=480, y=520, anchor="c")
    
    for i in range(6, 8):
        radio_btn[i].place(x=200, y=250+80*(i-6))

def fase3_2(): # fase2_1 -> No
    var.set(8)
    fase3_2lbl.place(x=300, y=100, anchor="c")
    result_btn.place(x=480, y=520, anchor="c")
    for i in range(8, 10):
        radio_btn[i].place(x=200, y=250+80*(i-8))

def fase3_3(): # fase2_2 -> Yes
    var.set(10)
    fase3_3lbl.place(x=300, y=100, anchor="c")
    result_btn.place(x=480, y=520, anchor="c")
    for i in range(10, 12):
        radio_btn[i].place(x=200, y=250+80*(i-10))

def fase3_4(): # fase2_2 -> No
    var.set(12)
    fase3_4lbl.place(x=300, y=100, anchor="c")
    result_btn.place(x=480, y=520, anchor="c")
    for i in range(12, 14):
        radio_btn[i].place(x=200, y=250+80*(i-12))


def result():
    fase3_1lbl.place_forget()
    fase3_2lbl.place_forget()
    fase3_3lbl.place_forget()
    fase3_4lbl.place_forget()
    result_btn.place_forget()
    for i in range(14):
        radio_btn[i].place_forget()
    var_check = var.get()

    # 【★★★追加★★★】画像の表示(cvs.create_image)
    if var_check == 6:
        cvs.create_image(300, 300, image=Y3_1_img, tag="result")
        Y3_1_lbl.place(x=300, y=100, anchor="c")
    elif var_check == 7:
        cvs.create_image(300, 300, image=N3_1_img, tag="result")
        N3_1_lbl.place(x=300, y=100, anchor="c")
    elif var_check == 8:
        cvs.create_image(300, 300, image=Y3_2_img, tag="result")
        Y3_2_lbl.place(x=300, y=100, anchor="c")
    elif var_check == 9:
        cvs.create_image(300, 300, image=N3_2_img, tag="result")
        N3_2_lbl.place(x=300, y=100, anchor="c")
    elif var_check == 10:
        cvs.create_image(300, 300, image=Y3_3_img, tag="result")
        Y3_3_lbl.place(x=300, y=100, anchor="c")
    elif var_check == 11:
        cvs.create_image(300, 300, image=N3_3_img, tag="result")
        N3_3_lbl.place(x=300, y=100, anchor="c")
    elif var_check == 12:
        cvs.create_image(300, 300, image=Y3_4_img, tag="result")
        Y3_4_lbl.place(x=300, y=100, anchor="c")
    elif var_check == 13:
        cvs.create_image(300, 300, image=N3_4_img, tag="result")
        N3_4_lbl.place(x=300, y=100, anchor="c")
    again_btn.place(x=480, y=520, anchor="c")
    print(var_check)
# ----------------------------------------
# ウィンドウの準備
# ----------------------------------------
root = tk.Tk()
root.title("Branch")
root.geometry("600x600")
root.resizable(False, False)
# ----------------------------------------
# 【★★★追加★★★】キャンバスの生成
# ----------------------------------------
cvs = tk.Canvas(root, width=600, height=600, bg="white")
cvs.pack()
# ----------------------------------------
# ラジオボタンの準備
# ----------------------------------------
radio_btn = [None]*14
ITEM = ["質問１YES","質問１NO", "質問２YES", "質問２NO", "質問２YES", "質問２NO",
        "質問３YES","質問３NO","質問３YES","質問３NO","質問３YES","質問３NO","質問３YES","質問３NO"]
var = tk.IntVar()
for i in range(14):
    radio_btn[i] = tk.Radiobutton(text=ITEM[i], font=("Helvetica", 36),
                    value=i, variable=var)
# ----------------------------------------
# ラベル，ボタンの準備
# ----------------------------------------
start_lbl = tk.Label(text="ABCD診断", font=("Futura", 100))
start_btn = tk.Button(text="> start", font=("Helvetica", 40), command=fase1)
# ----------------------------------------
fase1_lbl = tk.Label(text="質問１", font=("Futura", 40))
fase1_btn = tk.Button(text="> fase2", font=("Helvetica", 40), command=branch1)
# ----------------------------------------
fase2_1lbl = tk.Label(text="質問２（質問１YES）", font=("Futura", 40))
fase2_2lbl = tk.Label(text="質問２（質問１NO）", font=("Futura", 40))
fase2_1btn = tk.Button(text="> fase3", font=("Helvetica", 40), command=branch2)
fase2_2btn = tk.Button(text="> fase3", font=("Helvetica", 40), command=branch2)
# ----------------------------------------
fase3_1lbl = tk.Label(text="質問３（質問１YES,質問２YES）", font=("Futura", 40))
fase3_2lbl = tk.Label(text="質問３（質問１YES,質問２NO）", font=("Futura", 40))
fase3_3lbl = tk.Label(text="質問３（質問１NO,質問２YES）", font=("Futura", 40))
fase3_4lbl = tk.Label(text="質問3（質問１NO,質問２NO）", font=("Futura", 40))
# ----------------------------------------
result_btn = tk.Button(text="result", font=("Helvetica", 40), command=result)
Y3_1_lbl = tk.Label(text="質問１YES,質問２YES,質問３YES", font=("Futura", 30))
N3_1_lbl = tk.Label(text="質問１YES,質問２YES,質問３NO", font=("Futura", 30))
Y3_2_lbl = tk.Label(text="質問１YES,質問２NO,質問３YES", font=("Futura", 30))
N3_2_lbl = tk.Label(text="質問１YES,質問２NO,質問３NO", font=("Futura", 30))
Y3_3_lbl = tk.Label(text="質問１NO,質問２YES,質問３YES", font=("Futura", 30))
N3_3_lbl = tk.Label(text="質問１NO,質問２YES,質問３NO", font=("Futura", 30))
Y3_4_lbl = tk.Label(text="質問１NO,質問２NO,質問３YES", font=("Futura", 30))
N3_4_lbl = tk.Label(text="質問１NO,質問２NO,質問３NO", font=("Futura", 30))
result_lbl = [Y3_1_lbl,N3_1_lbl,Y3_2_lbl,N3_2_lbl,Y3_3_lbl,N3_3_lbl,Y3_4_lbl,N3_4_lbl]
# ----------------------------------------
again_btn = tk.Button(text="> again", font=("Helvetica", 40), command=start)
# ----------------------------------------
# 【★★★追加★★★】分岐画像の定義
# ----------------------------------------
# Z3_X_img = tk.PhotoImage(file="ここに使用する画像を指定")
Y3_1_img = tk.PhotoImage(file="./1.png")
N3_1_img = tk.PhotoImage(file="./2.png")
Y3_2_img = tk.PhotoImage(file="./3.png")
N3_2_img = tk.PhotoImage(file="./4.png")
Y3_3_img = tk.PhotoImage(file="./5.png")
N3_3_img = tk.PhotoImage(file="./6.png")
Y3_4_img = tk.PhotoImage(file="./7.png")
N3_4_img = tk.PhotoImage(file="./8.png")
# ----------------------------------------
start()
root.mainloop()