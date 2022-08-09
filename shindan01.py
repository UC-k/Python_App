import tkinter as tk
# ------------------------------------------------------------------------------
# 変数宣言
bool_var = [None]*12
check_btn = [None]*12
ITEM = [
    "CUIについて理解した",
    "GUIについて理解した",
    "乱数生成について理解し、乱数を生成できる",
    "リスト（配列）について理解した",
    "関数について理解し、関数を自作できる",
    "tkinterで画面を生成できる",
    "tkinterで文字や画像、ボタンを配置できる",
    "チェックボタンの仕様について理解している",
    "おみくじアプリのプログラムの流れを把握している",
    "コードを見れば内容が把握できる",
    "自分でアプリを設計して開発できる",
    "Pythonが好きである"
]
# チェックボタンの数＋１用意する
RESULT = [
    "もう一度最初から勉強しよう…\nでも次はきっと理解できるさ！！",# チェック0個のとき
    "１つでもチェックできたのならそれはもう大きな一歩さ！！\nでももう一度勉強し直そう！",# チェック1個のとき
    "ちょ、冗談きついぜ。\n君はまだ第一形態ってわけかい？",# チェック2個のとき
    "星３つッ！\nって喜んでいる場合じゃないよ〜",# チェック3個のとき
    "苦しゅうない。表を上げい。\nせめて半分はチェック入れれるようにせよ。",# チェック4個のとき
    "折り返し地点まであと少し！\nどこが理解できていないかしっかり把握して再挑戦！",# チェック5個のとき
    "半分は理解できたってことだよ。\nそう半分。ここからが本番。",# チェック6個のとき
    "半分以上理解できた君は上出来だ！\nあれ？もしかして「Pythonが好きである」で半分超えた感じ？",# チェック7個のとき
    "いいね！\n基本はもう完璧かな？\n今の君なら応用にも対応できるぜ。",# チェック8個のとき
    "もうちょい！もうちょいなのよ〜。\nここまできたら極めよう！",# チェック9個のとき
    "グッジョブ！！\nほぼ理解できた君にはイキリパイソニスタの称号を授けよう！！",# チェック10個のとき
    "いいよ、いい感じ！！\nあと少しで完璧だ！！",# チェック11個のとき
    "すばらしい！！！！\nよっ！！Pythonマスター！！"# チェック12個のとき
]
# ------------------------------------------------------------------------------
# start
def start():
    global flg
    cvs.create_image(300, 300, image=start_img, tag="start")
    start_btn.place(x=300, y=530, anchor="c")
# main
def main():
    # 画面整理
    cvs.delete("start")
    start_btn.place_forget()
    # チェックボタン等の配置
    for i in range(12):
        check_btn[i].place(x=130, y=60+40*i, anchor="nw")
    main_btn.place(x=500, y=550, anchor="c")
    how_txt.place(x=300, y=30, anchor="c")
# result
def check():
    # 画面整理
    for i in range(12):
        check_btn[i].place_forget()
    main_btn.place_forget()
    how_txt.place_forget()
    # 診断
    cnt = 0
    for i in range(12):
        if bool_var[i].get():
            cnt += 1
    per = int(cnt/12 * 100)
    # 結果表示
    result_txt.insert("1.0", "あなたのPython習熟度は"+str(per)+"%です。\n\n"
                    +RESULT[cnt])
    result_txt.place(x=300, y=200, anchor="c")
    # もう一度やるかやめるか
    again_btn.place(x=420, y=550, anchor="c")
    end_btn.place(x=520, y=550, anchor="c")
# again or end
def again():
    # 画面整理
    result_txt.delete("1.0", tk.END)
    result_txt.place_forget()
    again_btn.place_forget()
    end_btn.place_forget()
    for i in range(12):
        bool_var[i].set(False)
    # 診断画面に戻る
    main()
def end():
    root.destroy()
# ------------------------------------------------------------------------------
root = tk.Tk()
root.title("Python習熟度診断アプリ")
root.geometry("600x600+300+100")
root.resizable(False, False)
# ------------------------------------------------------------------------------
cvs = tk.Canvas(root, width=600, height=600, bg="#323232")
cvs.pack()
# ------------------------------------------------------------------------------
# ウィジェットの準備
# 画像
start_img = tk.PhotoImage(file="./shindan/start.png")
# ボタン
start_btn = tk.Button(text="START", font=("Futura", 30), cursor="pointinghand",
                    fg="#3271A1", bg="#FFFFFF", command=main)
main_btn = tk.Button(text="診断する", font=("System", 20), cursor="pointinghand",
                    fg="grey", bg="white", command=check)
again_btn = tk.Button(text="もう一度", font=("System", 10), cursor="pointinghand",
                        fg="#323232", bg="#FFFFFF", command=again)
end_btn = tk.Button(text="終了する", font=("System", 10), cursor="pointinghand",
                    fg="#323232", bg="#FFFFFF", command=end)
# チェックボタン
for i in range(12):
    bool_var[i] = tk.BooleanVar()
    bool_var[i].set(False)
    check_btn[i] = tk.Checkbutton(text=" "+ITEM[i], font=("System", 16),
                                fg="white", bg="#323232", variable=bool_var[i])
# テキスト
how_txt = tk.Label(text="当てはまるもの全てにチェックを入れよう", font=("System", 22),
                    fg="skyblue", bg="#323232")
result_txt = tk.Text(width=30, height=7, font=("System", 24))
# ------------------------------------------------------------------------------
start()
root.mainloop()