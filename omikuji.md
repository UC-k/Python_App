# 1. CUIについて

## CUIとは
CUI（Character User Interface）とは、文字によるコマンド入力方式のインターフェイスのこと。

## 乱数生成
Pythonではrandomモジュールを使用することによって乱数を生成することができる。

## リスト
変数を数や文字列を入れる箱とすると、リストとはその箱に番号をつけて管理するもの。リストは他の言語の配列にあたる。<br>
リストの中１つ１つを要素という。また、何番目かを管理する番号のことを添え字（インデックス）という。

## おみくじアプリ(CUI)
**omikuji01.py**
``` python
# randomモジュールのインポート
import random
# リストからランダムにひとつ選び、変数に格納
result = random.choice(["大吉", "吉", "中吉", "小吉", "末吉", "凶"])
# 結果を表示
print(result)
```

---
<br>


# 2. GUIについて

## GUIとは
GUI（Graphical User Interface）とは、コンピュータの画面上に表示されるウィンドウやアイコン、ボタン、プルダウンメニューなどを使い、マウスなどのポインティングデバイスで操作できるインターフェースのこと。

## tkinterとは
tkinterとは、Pythonでグラフィック関連（表示・操作）のソフトウェアを開発するためのライブラリである。<br>
PythonでGUIを扱うためのライブラリはいくつか存在する。中でもtkinterはPythonの標準ライブラリのため、比較的導入が容易であり、デスクトップアプリケーションの開発に向いている。<br>
tkinterの他には図を描画することに特化したturtleや、ゲーム開発に特化したPygameなどがある。

## tkinterの使い方
### ＜ウィンドウ＞
**ウィンドウの表示**
``` python
# モジュールをインポート
import tkinter
# ウィンドウの部品（オブジェクト）を作成
root = tkinter.Tk()
# ウィンドウを表示するメソッド（ループ：アプリの待機とイベントの処理）
root.mainloop()
```
**ウィンドウのタイトルとサイズの指定**
``` python
# モジュールのインポート
import tkinter
# ウィンドウのオブジェクト作成
root = tkinter.Tk()
# ウィンドウタイトルを指定
root.title("ウィンドウタイトル")
# ウィンドウサイズの指定("幅x高さ")
root.geometry("600x400")
# ウィンドウを表示
root.mainloop()
```
**備考**
``` python
# ウィンドウは初期位置・最小サイズ・最大サイズ・サイズ変動不可などの指定が可能
# 初期位置の指定（"幅x高さ+横+縦"）
root.geometry("600x400+100+200")
# 最小サイズを指定
root.minsize(width=100,height=200)
# 最大サイズを指定
root.maxsize(width=800,height=400)
# サイズ変動不可
root.resizable(False, False)
```

### ＜ラベル＞
ラベルとは、文字列を表示する部品である。<br>
Label( )でラベルを作成し、place( )で配置する。<br>
**ラベルの生成と配置**
``` python
import tkinter
root = tkinter.Tk()
root.title("ラベルの生成と配置")
root.geometry("600x400")
# ラベル
label = tkinter.Label(root, text="ラベルテキスト", font=("System", 18))
label.place(x=300, y=200, anchor="c")

root.mainloop()
```
**備考**
```
ラベル変数名　= tkinter.Label(ウィンドウオブジェクト, text="テキスト",
                            font=("フォント名", フォントサイズ))
ラベルの変数名.place(x=X座標, y=Y座標, anchor="配置場所")
```
**使えるフォントについて**<br>
tkinterで表示する文字にはフォントを指定することができますが、使用するPCによって表示できる
フォントは異なる。次のコードを実行して使用できるフォントを調べることができる。
``` python
import tkinter
import tkinter.font
root = tkinter.Tk()
print(tkinter.font.families())
```

### ＜ボタン＞
### ＜キャンバス＞
### ＜画像＞
