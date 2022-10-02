# ウィジェットの削除方法

ウィジェットを削除する方法は，メインウィンドウに配置するもの，キャンバスに配置するもので異なる。<br>
メインウィンドウに配置するものの例として，ボタンやラベルが挙げられる。<br>
キャンバスに配置するものの例として，画像や矩形が挙げられる。<br>

<br>

## メインウィンドウに配置するウィジェットの削除方法
1. 変数名.destroy(　)
2. 変数名.place_forget(　)

<br>

１のdestroyでは，ウィジェットそのものを破壊してしまうので，再配置不可になる。<br>
２のplace_forgetでは，ウィジェットの配置を忘れる（＝一時的に隠す）ので，再配置可能である。<br>

<br>

## キャンバスに配置するウィジェットの削除方法
1. cvs.create_hoge(..., tag="タグ")でタグ付けする。その後，cvs.delete("タグ")で削除
2. cvs.delete("all")で削除

<br>

１でタグを付けることによって，cvs.delete(　)のカッコ内にタグ名を指定して削除することができる。<br>
２では，タグありなし関係なく，キャンバス上に配置されているものを全て削除することができる。<br>

<br>

<br>

## ウィジェット削除と復元の例
`注意：コード内で使用している画像（pythonのロゴ）をダウンロードして実行する必要あり。`<br>
[使用する画像のダウンロードはこちらをクリック](https://github.com/UC-k/Python_App/blob/main/logo.png)


``` python
import tkinter as tk

def c_img():
    cvs.create_image(150, 200, image=img_1, tag="hoge")
def d_img():
    cvs.delete("hoge")

def e_plc():
    entry.place(x=450, y=260, anchor="c")
def e_pfg():
    # entry.destroy()
    entry.place_forget()

# -----------------------------------------------------------------------------
root = tk.Tk()
root.title("ウィジェットの削除方法")
root.geometry("600x600+300+100")
root.config(bg="black")

cvs = tk.Canvas(root, width=300, height=600, bg="white")
cvs.place(x=0, y=0, anchor="nw")

# label -----------------------------------------------------------------------
r_lbl = tk.Label(root, text="root", font=("Futura", 30), fg="white", bg="black")
r_lbl.place(x=450, y=50, anchor="c")

c_lbl = tk.Label(root, text="cvs", font=("Futura", 30), fg="black", bg="white")
c_lbl.place(x=150, y=50, anchor="c")
# -----------------------------------------------------------------------------

# button ----------------------------------------------------------------------
r_btn = tk.Button(root, text="delete", font=("Futura"), fg="black",
                command=e_pfg)
r_btn.place(x=450, y=550, anchor="c")
rc_btn = tk.Button(root, text="create", font=("Futura"), fg="black",
                command=e_plc)
rc_btn.place(x=450, y=500, anchor="c")

c_btn = tk.Button(root, text="delete", font=("Futura"), fg="black", 
                command=d_img)
c_btn.place(x=150, y=550, anchor="c")
cc_btn = tk.Button(root, text="create", font=("Futura"), fg="black",
                command=c_img)
cc_btn.place(x=150, y=500, anchor="c")
# -----------------------------------------------------------------------------¬

# image -----------------------------------------------------------------------
img_1 = tk.PhotoImage(file="./logo.png")
cvs.create_image(150, 200, image=img_1, tag="hoge")
img_2 = tk.PhotoImage(file="./logo.png")
cvs.create_image(150, 350, image=img_2)
# -----------------------------------------------------------------------------¬

# Entry ------------------------------------------------------------------------
entry = tk.Entry(root, width=10, fg="white", bg="#323232")
entry.place(x=450, y=260, anchor="c")
entry.insert(tk.END, "あいうえお")
entry.focus_set()
# -----------------------------------------------------------------------------¬
root.mainloop()
```