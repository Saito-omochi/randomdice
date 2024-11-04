import flet as ft
import numpy as np

def main(page):
    #初期設定
    page.title = "ランダムダイス"  # タイトル
    page.window.width = 500  # 幅
    page.window.height = 600  # 高さ
    page.theme = ft.Theme(color_scheme_seed="green")

    #初期値を設定
    global num1,num2,TFpi
    resultlist = []
    count_dict = {}
    TFpi = False
    num1 = 1
    num2 = 10

    #各種関数
    def on_change_dropdown1(e):
        global num1
        num1 = int(e.control.value)

    def on_change_dropdown2(e):
        global num2
        num2 = int(e.control.value)
    
    def on_change_checkbox(e):
        global TFpi
        TFpi = e.control.value
    
    def on_click_reset(e):
        t.value = ""
        l.value = ""
        c.value = ""
        o.value = ""
        resultlist.clear()
        count_dict.clear()
        page.update()

    def result(e):
        global num1, num2, TFpi
        p = 0
        if num1 == 1:
            p = int(((num2+1)*num1)-1)
        else:
            p = int(((num2+1)*num1-(num1-1)) - num1)

        def make_random(num1, num2):
            randomnum = 0
            for i in range(num1):
                r2 = np.random.randint(1,num2+1)
                randomnum += r2
            return randomnum

        if TFpi == False:#通常処理
            r = make_random(num1, num2)
            resultlist.append(r)
            if num1 == 1:
                count_dict = {i: resultlist.count(i) for i in range(1, (num2+1)*num1)}
            else:
                count_dict = {i: resultlist.count(i) for i in range(num1, ((num2+1)*num1-(num1-1)))}
            t.value = r
            l.value = str(resultlist)
            c.value = str(count_dict)
            page.update()
        else:#一度出た値は出さないモード
            if len(resultlist) == p:
                o.value = "全ての数字が出ました"
                page.update()
            else:
                r = make_random(num1, num2)
                while r in resultlist:
                    r = make_random(num1, num2)
                if r not in resultlist:
                    resultlist.append(r)

                if num1 == 1:
                    count_dict = {i: resultlist.count(i) for i in range(1, (num2+1)*num1)}
                else:
                    count_dict = {i: resultlist.count(i) for i in range(num1, ((num2+1)*num1-(num1-1)))}
                t.value = r
                l.value = str(resultlist)
                c.value = str(count_dict)
            page.update()

    #部品配置
    page.add(
        ft.Column([
            ft.Checkbox(label = "一度出た値は出さないモード", value = False, on_change = on_change_checkbox),
            ft.Row([
                ft.Dropdown(
                    label="dice",
                    hint_text="1",
                    options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
                    on_change = on_change_dropdown1,
                    width = 100,
                    value = 1
                ),
                ft.Text("d"),
                ft.Dropdown(
                    label="dice",
                    hint_text="1",
                    options=[ft.dropdown.Option(str(i)) for i in range(1, 101)],
                    width = 100,
                    on_change = on_change_dropdown2,
                    value = 10
                ),
            ],),
            ft.Row([
                ft.ElevatedButton(
                    text="GO!",
                    on_click = result, 
                ),
                ft.ElevatedButton(
                    text="Reset",
                    on_click = on_click_reset,
                )
            ])
        ])
    )
    o = ft.Text()
    t = ft.Text()
    l = ft.Text(selectable=True)
    c = ft.Text()
    page.add(t, l, c, o)

ft.app(target=main)
