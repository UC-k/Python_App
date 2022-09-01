# tkinter ウィジェット説明
|ウィジェット名|説明|
|:-:|:-|
|Label|文字列やイメージを表示できる|
|Button|押すとイベントを起こすボタンが表示できる|
|Canvas|線や円などの図形、画像などを描画できる|
|PhotoImage|画像を表示できる|
|Entry|1行の文字列入力ボックスを表示できる|
|Text|複数行の文字列入力ボックスを表示できる|
|Checkbutton|複数選択できる選択肢を表示できる|
|Radiobutton|１つ選択できる選択肢を表示できる|

<br>
<br>

# anchor 位置
|nw (northwest)|n (north)|ne (northeast)|
|:-:|:-:|:-:|
|w (west)|c (center)|e (east)|
|sw (southwest)|s (south)|se (southeast)|

<br>
<br>

# Label オプション
|オプション引数|説明|値|
|:-:|:-|:-|
|anchor|配置位置の指定|[「anchor 位置」で説明](#anchor-位置)|
|bg, background|背景色|カラーコード, 色名|
|bd, borderwidth|ボーダーの幅の指定|数値（px）|
|cursor|カーソルの形の指定|[詳しくはここを参照](https://www.tcl.tk/man/tcl/TkCmd/cursors.html)|
|font|フォントのタイプ, サイズ, 太さを指定|フォント名, サイズ, 太さ|
|fg, foreground|フォントの色を指定|カラーコード, 色名|
|height|ラベルの高さ|数値|
|width|ラベルの幅|数値|
|image|ラベルに貼る画像ファイルの指定|画像のパス|
|compound|ラベルに画像を貼る場合のテキストの位置|center, top, bottom, left, right|
|justify|複数行テキストの寄せ位置|center(default), left, right|
|padx|枠とテキストとの間の横の空白|数値|
|pady|枠とテキストとの間の縦の空白|数値|
|relief|ラベル枠を指定|flat(default), raised, sunken, groove, ridge|
|takefocus|フォーカスの指定|0（ない）, 1（ある）|
|text|表示する文字列を指定|文字列|
underline|アンダーライン|True, False|
|wraplength|複数行の場合の改行幅|数値|

<br>
<br>

# Button オプション
|オプション引数|説明|
|:-:|:-|
|text|ボタンに表示するテキスト|
|textvariable|表示するテキスト（tk.StringVar( )のインスタンス）|
|font|テキストのフォント・サイズ・太さ|
|fg, foreground|通常時の文字色|
|activeforeground|ボタン押下時の文字色|
|anchor|文字列の配置位置|
|justify|複数行に渡った場合の文字揃え|
|height|ボタンの縦幅|
|width|ボタンの横幅|
|bg, background|ボタンの背景色|
|activebackground|ボタン押下時の背景色|
|padx|横方向のボタンの内部余白|
|pady|縦方向のボタンの内部余白|
|relief|ボタンのボーダースタイル|
|command|ボタン押下時のイベント処理|
|state|ボタンの状態|
|repeatdelay|ボタン押下時のクリック判定秒数|
|repeatinterval|ボタン長押し時のクリック判定秒数|

<br>
<br>

# Entry　オプション
|オプション引数|説明|
|:-:|:-|
|fg, foreground|入力される文字色|
|bg, background|テキストボックス内の背景色|
|bd, borderwidth|枠線のサイズ（default：2px）|
|width|横幅を指定（半角の文字数）|
|font|テキストのフォントタイプ, 大きさの指定|
|command|テキストボックス内に変更がある度に呼び出す関数|
|cursor|マウスホバー時のカーソルの種類|
|state|状態を指定|
|textvariable|テキストを変数で指定|
|justify|テキストの入力位置（default：left）|
|relief|テキストボックスのボーダーデザイン|
|show|テキスト入力時に指定した文字を入力文字の代わりに表示|

<br>
<br>

# config
メインウィンドウやウィジェットのオプション引数の値を変更したい際に「config」を使用することができる。
<br>

**メインウィンドウの背景色を変更する例**
``` python
import tkinter as tk

root = tk.Tk()
root.config(bg = "blue")
root.mainloop()
```
<br>

**ラベルの文字列をボタンと関数によって変更する例**
``` python
import tkinter as tk
# ボタンの状態を管理するフラグ
btn_flg = 0
# マウスがボタン内にある場合のボタンの状態
def btn_in(self):
    btn.config(fg="blue")
# マウスがボタン外にある場合のボタンの状態
def btn_out(self):
    btn.config(fg="green")
# ボタンがクリックされたときのイベント
def click():
    global btn_flg
    if btn_flg == 0:
        label.config(text="変更後")
        btn_flg = 1
    elif btn_flg == 1:
        label.config(text="変更前")
        btn_flg = 0
# メインウィンドウの生成
root = tk.Tk()
root.geometry("300x300")
root.config(bg="#323232")
# ラベルの生成
label = tk.Label(text="変更前", font=("System", 24), bg="#323232")
label.place(x=150, y=120, anchor="c")
# ボタンの生成
btn = tk.Button(text="ボタン", fg="green", activeforeground="red", command=click)
btn.bind("<Enter>", btn_in)
btn.bind("<Leave>", btn_out)
btn.place(x=150, y=170, anchor="c")

root.mainloop()
```

<br>
<br>

# bind処理の追加
同一のトリガー（例の場合、ボタン）に対し、追加でイベントを紐づけたい場合は、オプションを指定した後に「"+"」を追記する。これを付けない場合、上書きされて最後に定義したイベントのみが実行される。<br>
**bindを使用する際は、関数に引数（self）が必要となることを忘れずに！！**
<br>

``` python
import tkinter as tk

def btn_in(self):
    btn.config(text="福は内")
def cui_in(self):
    print("福は内")

root = tk.Tk()
root.geometry("300x300")

btn = tk.Button(text="鬼は外")
btn.bind("<Enter>", btn_in)
btn.bind("<Motion>", cui_in, "+")
btn.place(x=150, y=170, anchor="c")

root.mainloop()
```
<br>

# bind　イベント
|イベント|説明|
|:-|:-|
|<1>, < Button-1 >, < ButtonPress >|左クリック|
|<2>, < Button-2 >|ホイールクリック|
|<3>, < Button-3 >|右クリック|
|< Double-1 >|ダブルクリック|
|< ButtonRelease >|クリックを離したとき|
|< x >, < KeyPress-X >|xキーを入力したとき|
|< Control-c >|Controlとcキーが押されたとき|
|< Enter >|マウスカーソルがウィジェット内に入ったとき|
|< Leave >|マウスカーソルがウィジェット内を出たとき|
|< Motion >|ウィジェット内でカーソルが動いたとき|