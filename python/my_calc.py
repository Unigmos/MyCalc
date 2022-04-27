#-------------------------------------------------------------------------------
# Name:         MyCalc_Python
# Purpose:      電卓が作りたくなったので作っただけ
#
# Author:       Shaneron
#
# Created:      15/04/2022
# Copyright:    (c) Shaneron 2022
#-------------------------------------------------------------------------------

# ライブラリのimport
try:
    import tkinter as tk
    from tkinter import messagebox
except ModuleNotFoundError as NO_MODULE_ERROR:
    print(f"ModuleNotFoundError:{NO_MODULE_ERROR}")

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # ×ボタンでの終了
        master.protocol("WM_DELETE_WINDOW", self.close_app)

        # 出力欄の定義
        self.ans_data = tk.StringVar()
        self.ans_box = tk.Label(textvariable=self.ans_data, background='#ffffff', font=("", 60), anchor=tk.E).grid(rowspan=2, columnspan=4 ,row=0, column=0, sticky=tk.NW+tk.NE+tk.S)

        #メニューバー
        menu_bar = tk.Menu(master)
        master.config(menu=menu_bar)

        # 親メニュー
        config_menu = tk.Menu(master, tearoff=False)
        menu_bar.add_cascade(label="設定", menu=config_menu)

        # 子メニュー(設定)
        config_menu.add_command(label="小数点以下設定", command=self.set_decimal)

        # ボタン配置
        sym_1 = tk.Button(master, text='(', command=lambda:self.set_text(str_data="(")).grid(row=2, column=0, sticky=tk.NW+tk.NE+tk.S)
        sym_2 = tk.Button(master, text=')', command=lambda:self.set_text(str_data=")")).grid(row=2, column=1, sticky=tk.NW+tk.NE+tk.S)
        sym_3 = tk.Button(master, text='%', command=lambda:self.set_text(str_data="%")).grid(row=2, column=2, sticky=tk.NW+tk.NE+tk.S)
        sym_4 = tk.Button(master, text='C', command=self.clear_text).grid(row=2, column=3, sticky=tk.NW+tk.NE+tk.S)

        num_7 = tk.Button(master, text='7', command=lambda:self.set_text(str_data="7")).grid(row=3, column=0, sticky=tk.NW+tk.NE+tk.S)
        num_8 = tk.Button(master, text='8', command=lambda:self.set_text(str_data="8")).grid(row=3, column=1, sticky=tk.NW+tk.NE+tk.S)
        num_9 = tk.Button(master, text='9', command=lambda:self.set_text(str_data="9")).grid(row=3, column=2, sticky=tk.NW+tk.NE+tk.S)
        sym_5 = tk.Button(master, text='/', command=lambda:self.set_text(str_data="/")).grid(row=3, column=3, sticky=tk.NW+tk.NE+tk.S)

        num_4 = tk.Button(master, text='4', command=lambda:self.set_text(str_data="4")).grid(row=4, column=0, sticky=tk.NW+tk.NE+tk.S)
        num_5 = tk.Button(master, text='5', command=lambda:self.set_text(str_data="5")).grid(row=4, column=1, sticky=tk.NW+tk.NE+tk.S)
        num_6 = tk.Button(master, text='6', command=lambda:self.set_text(str_data="6")).grid(row=4, column=2, sticky=tk.NW+tk.NE+tk.S)
        sym_6 = tk.Button(master, text='*', command=lambda:self.set_text(str_data="*")).grid(row=4, column=3, sticky=tk.NW+tk.NE+tk.S)

        num_1 = tk.Button(master, text='1', command=lambda:self.set_text(str_data="1")).grid(row=5, column=0, sticky=tk.NW+tk.NE+tk.S)
        num_2 = tk.Button(master, text='2', command=lambda:self.set_text(str_data="2")).grid(row=5, column=1, sticky=tk.NW+tk.NE+tk.S)
        num_3 = tk.Button(master, text='3', command=lambda:self.set_text(str_data="3")).grid(row=5, column=2, sticky=tk.NW+tk.NE+tk.S)
        sym_7 = tk.Button(master, text='-', command=lambda:self.set_text(str_data="-")).grid(row=5, column=3, sticky=tk.NW+tk.NE+tk.S)

        num_0 = tk.Button(master, text='0', command=lambda:self.set_text(str_data="0")).grid(row=6, column=0, sticky=tk.NW+tk.NE+tk.S)
        sym_8 = tk.Button(master, text='.', command=lambda:self.set_text(str_data=".")).grid(row=6, column=1, sticky=tk.NW+tk.NE+tk.S)
        sym_9 = tk.Button(master, text='=', command=self.calc).grid(row=6, column=2, sticky=tk.NW+tk.NE+tk.S)
        sym_10 = tk.Button(master, text='+', command=lambda:self.set_text(str_data="+")).grid(row=6, column=3, sticky=tk.NW+tk.NE+tk.S)

        # 行引き伸ばし
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)
        master.rowconfigure(3, weight=1)
        master.rowconfigure(4, weight=1)
        master.rowconfigure(5, weight=1)
        master.rowconfigure(6, weight=1)

        # 列引き伸ばし
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        master.columnconfigure(3, weight=1)

        # 初期文字列の定義
        self.text_box=""

        # 小数点桁数の初期値定義
        self.decimal_data = 3

    # アプリケーションの終了
    def close_app(self):
        close_ans = messagebox.askyesno(title="確認", message="ウィンドウを閉じますか？")
        # はい(yes)選択時のみ終了する
        if close_ans:
            self.master.destroy()

    # 文字列のセット
    def set_text(self, str_data):
        self.text_box += str_data
        self.ans_data.set(self.text_box)

    # 入力文字列のリセット
    def clear_text(self):
        self.text_box = ""
        self.ans_data.set("")

    # 演算処理
    def calc(self):
        try:
            ans = eval(self.text_box)
            self.ans_data.set(f"{ans:.{self.decimal_data}f}")
        except SyntaxError:
            messagebox.showerror(title="SyntaxError!!", message=f"{SyntaxError}\n不正な式です。")

    # 小数点設定
    def set_decimal(self):
        self.set_decimal_window = tk.Toplevel()
        self.set_decimal_window.geometry("250x200")
        self.set_decimal_window.title("小数点以下設定")
        self.set_decimal_window.resizable(width=False, height=False)

        # 小数点以下桁数設定(ラベル・エントリー)
        decimal_label = tk.Label(self.set_decimal_window, text="小数点以下桁数").grid(row=0, column=0, padx=5)
        self.decimal_entry = tk.Entry(self.set_decimal_window, width=20, textvariable=self.decimal_data)
        self.decimal_entry.insert(tk.END, self.decimal_data)
        self.decimal_entry.grid(row=0, column=1)

        # 反映ボタン
        tk.Button(self.set_decimal_window, text="OK", relief="groove", command=lambda:self.set_decimal_data(data=self.decimal_entry.get())).grid(row=3, column=1)

    # 小数点設定反映
    def set_decimal_data(self, data):
        # 子ウィンドウ(ダイアログ)の削除
        try:
            self.set_decimal_window.destroy()
        except:
            pass
        self.decimal_data = data
        print(self.decimal_data)


def main():
    # App初期設定・実行
    widget = tk.Tk()
    widget.geometry("600x400")
    widget.minsize(width=300, height=200)
    widget.title("MyCalc")
    app = App(master=widget)
    app.mainloop()

if __name__ == '__main__':
    main()
