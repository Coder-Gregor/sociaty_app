import flet as f
import sqlite3

k=int(0)
f_assessment=int(0) 
f_power=int(0)
f_achtivity=int(0)

def main(page: f.Page):                    #описание главного окна
    page.title="..."
    page.theme_mode='dark'
    page.vertical_alignment=f.MainAxisAlignment.CENTER
    page.horizontal_alignment=f.CrossAxisAlignment.CENTER
    page.scroll = "auto"


    def rg_trance(e):  #переход к регистрации
        page.clean()
        page.add(reg_panel)
        page.update()


    def en_trance(e):   #переход ко входу
        page.clean()
        page.add(ent_panel)
        page.update()

    def goback(e):      #назад
        page.clean()
        page.add(account_panel)
        page.update()


    def reg(e):        
        db=sqlite3.connect('BASE')               
        cur = db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            login TEXT,
            pass TEXT,
            f_assessment TEXT,
            f_power TEXT,
            f_achtivity TEXT
        )""")
        cur.execute(f"INSERT INTO users VALUES(NULL, '{reglf.value}','{regpf.value}',NULL,NULL,NULL)")

        db.commit()
        db.close()

        reglf.value = ''                               #очистка полей, сообщение о регистрации
        regpf.value = ''
        reg_but.text = 'Вы зарегистрированы!'

        page.clean()
        page.add(start_test_panel)

        page.update()

        
        
    def ent(e):                               #вход
        db=sqlite3.connect('BASE')
        cur = db.cursor()
      
        cur.execute(f"SELECT * FROM users WHERE login = '{reglf.value}' AND pass ='{regpf.value}'")        
        if cur.fetchone() != None:
            reglf.value = ''
            regpf.value = ''
            ent_but.text = 'Вы авторизовались!'

            page.clean()
            page.add(chats_panel)

            
            page.update()
        else:
            ent_but.text = 'Данные введены некоректно:('
            page.update()


        db.commit()
        db.close()

    def test(e):                    #тест
        page.clean()
        page.add(test_panel)
        page.update()
        

            #cистема начисления баллов 
    def add3(e):
        global k, f_assessment, f_power, f_achtivity
        if k < 7:
            f_assessment += 3
        elif 7 <= k < 14:
            f_power += 3
        else:
            f_achtivity += 3
        k += 1
        print(f_assessment,f_power,f_achtivity)
    def add2(e):       
        global k, f_assessment, f_power, f_achtivity
        if k < 7:
            f_assessment += 2
        elif 7 <= k < 14:
            f_power += 2
        else:
            f_achtivity += 2
        k += 1
        print(f_assessment,f_power,f_achtivity)
    def add1(e):       
        global k, f_assessment, f_power, f_achtivity
        if k < 7:
            f_assessment += 1
        elif 7 <= k < 14:
            f_power += 1
        else:
            f_achtivity += 1
        k += 1
        print(f_assessment,f_power,f_achtivity)
    def add0(e):       
        global k, f_assessment, f_power, f_achtivity
        if k < 7:
            f_assessment += 0
        elif 7 <= k < 14:
            f_power += 0
        else:
            f_achtivity += 0
        k += 1
        print(f_assessment,f_power,f_achtivity)
    def rem1(e):       
        global k, f_assessment, f_power, f_achtivity
        if k < 7:
            f_assessment -= 1
        elif 7 <= k < 14:
            f_power -= 1
        else:
            f_achtivity -= 1
        k += 1
        print(f_assessment,f_power,f_achtivity)
    def rem2(e):       
        global k, f_assessment, f_power, f_achtivity
        if k < 7:
            f_assessment -= 2
        elif 7 <= k < 14:
            f_power -= 2
        else:
            f_achtivity -= 2
        k += 1
        print(f_assessment,f_power,f_achtivity)
    def rem3(e):       
        global k, f_assessment, f_power, f_achtivity
        if k < 7:
            f_assessment -= 3
        elif 7 <= k < 14:
            f_power -= 3
        else:
            f_achtivity -= 3
        k += 1
        print(f_assessment,f_power,f_achtivity)
    
   

#чаты
    def chats(e):
        db=sqlite3.connect('BASE')
        cur = db.cursor()
        
        cur.execute(f"INSERT INTO users VALUES(NULL, '{reglf.value}','{regpf.value}','{f_assessment}','{f_power}','{f_achtivity}')")

        db.commit()
        db.close()
        
        page.clean()
        page.add(chats_panel)

    #переход к поиску пользователей со схожими результатами

    def looking_for_compatibility_person(e):
        

        page.clean()
        page.add(compatibility_panel)
        
    def add_this_frend(e):
        pass   

    #описание кнопок


    reglf=f.TextField(label='логин',width=500)
    regpf=f.TextField(label='пароль',width=500,password=True)
    reg_but1=f.ElevatedButton(text='Зарегистрироваться', width=500, on_click=rg_trance) #переход на страницу регистриции
    ent_but1=f.ElevatedButton(text='Войти', width=500,on_click=en_trance)  #переход на страницу авторизации
    reg_but=f.ElevatedButton(text='Зарегистрироваться',on_click=reg,width=500) #непосредственно регистрация
    ent_but=f.ElevatedButton(text='Войти',on_click=ent,width=500) #непосредственно вход
    back_but=f.ElevatedButton(text='Назад',width=500,on_click=goback)
    test_start_but=f.ElevatedButton(text='Начать',width=900,on_click=test)
    add3_but=f.ElevatedButton(text='+3', on_click=add3)
    add2_but=f.ElevatedButton(text='+2',on_click=add2)
    add1_but=f.ElevatedButton(text='+1',on_click=add1)
    add0_but=f.ElevatedButton(text='0',on_click=add0)
    rem1_but=f.ElevatedButton(text='-1',on_click=rem1)
    rem2_but=f.ElevatedButton(text='-2',on_click=rem2)
    rem3_but=f.ElevatedButton(text='-3',on_click=rem3)
    end_of_test_but=f.ElevatedButton(text='Завершить',on_click=chats)
    add_frends_but=f.ElevatedButton(text='Добавить друзей',on_click=looking_for_compatibility_person)
    make_proposal_but=f.IconButton(f.icons.ADD, on_click=add_this_frend)



    account_panel=f.Row(
            [
                f.Column(
                    [
                    f.Text('Добро пожаловать!',size=55,color="blue100"),
                    ent_but1,
                    reg_but1
                    ]
                )
            ],
            alignment=f.MainAxisAlignment.CENTER
        
        )

    reg_panel=f.Row(
            [
                f.Column(
                    [
                    f.Text('Придумайте логин и пароль (можно использовать номер телефона, почту и т.д.)',size=13,color="blue100"),
                    reglf,
                    regpf,
                    reg_but,
                    back_but
                    ]
                )
            ],
            alignment=f.MainAxisAlignment.CENTER
        )

    ent_panel=f.Row(
            [
                f.Column(
                    [
                    f.Text('Введите данные для авторизации...',size=15,color="blue100"),
                    reglf,
                    regpf,
                    ent_but,
                    back_but
                    ]
                )
            ],
            alignment=f.MainAxisAlignment.CENTER
        )

    start_test_panel=f.Row(
            [
                f.Column(
                    [
                        f.Text('                                  Аккаунт создан! Теперь неблольшое тестирование для лучшего подбора друзей;)',size=15), 
                        f.Text('Вам будут предложены качества человека, вы выбираете насколько часто в вас проявляется предложенное качество...',size=15),
                        f.Text('3 — проявляется очень сильно и очень часто, 2 — выражено достаточно заметно и часто встречается,',size=15),
                        f.Text('1 — проявляется иногда и слабо, 0 — трудно сказать, есть и то, и другое...',size=15),
                        test_start_but
                    ]        
                )
            ],
            alignment=f.MainAxisAlignment.CENTER
        )
    
    test_panel=f.Column(
                [                 
                    f.Text('                                                Тест(уровень дифференциации)',size=25),
                    f.Row([f.Text('обаятельный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('непривлекательный',size=15)]),
                    f.Row([f.Text('добросовестный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('безответственный',size=15)]),
                    f.Row([f.Text('добрый',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('эгоистичный',size=15)]),
                    f.Row([f.Text('отзывчивый',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('черствый',size=15)]),
                    f.Row([f.Text('справедливый',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('несправедливый',size=15)]),
                    f.Row([f.Text('дружелюбный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('враждебный',size=15)]),
                    f.Row([f.Text('честный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('неискренний',size=15)]),

                    f.Row([f.Text('разговорчивый',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('молчаливыйый',size=15)]),
                    f.Row([f.Text('открытый',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('замкнутый',size=15)]),
                    f.Row([f.Text('деятельный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('пассивный',size=15)]),
                    f.Row([f.Text('энергичный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('вялый',size=15)]),
                    f.Row([f.Text('суетливый',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('спокойный',size=15)]),
                    f.Row([f.Text('общительный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('нелюдимый',size=15)]),
                    f.Row([f.Text('раздражительный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('невозмутимый',size=15)]),

                    f.Row([f.Text('упрямый',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('уступчивый',size=15)]),
                    f.Row([f.Text('сильный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('слабый',size=15)]),
                    f.Row([f.Text('независимый',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('зависимый',size=15)]),
                    f.Row([f.Text('решительный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('нерешительный',size=15)]),
                    f.Row([f.Text('напряженный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('расслабленный',size=15)]),
                    f.Row([f.Text('уверенный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('неуверенный',size=15)]),
                    f.Row([f.Text('самостоятельный',size=15),add3_but,add2_but,add1_but,add0_but,rem1_but,rem2_but,rem3_but,f.Text('несамостоятельный',size=15)]),
                    end_of_test_but
                ],alignment=f.MainAxisAlignment.CENTER
            )
        
    
    chats_panel=f.Row(
        [
            f.Text('Ваши чаты'),
            add_frends_but
        ],
        alignment=f.MainAxisAlignment.CENTER
    )

    compatibility_panel=f.Row(
        [
            f.Text('люди, с уровнем дифференциации, близким вашему:'),

        ],
        alignment=f.MainAxisAlignment.CENTER
    )
      
      #для переходов между вкладками
    
    def navigate(e):
        index = page.navigation_bar.selected_index
        page.clean()

        if index == 0: page.add(account_panel)
        elif index == 1: page.add(ent_panel)
        elif index ==2: page.add(test_panel)
    
    page.navigation_bar = f.NavigationBar(
      destinations=[
            f.NavigationBarDestination(icon=f.icons.VERIFIED_USER,label="Регистрация/Вход в аккаунт") 
      ], on_change=navigate
    )

    page.add(account_panel)

f.app(target=main)