while True :#line:1
    from colorama import Fore ,Style #line:2
    g =Style .BRIGHT +Fore .GREEN #line:3
    w =Style .BRIGHT +Fore .WHITE #line:4
    try :#line:5
        import subprocess #line:6
        import sys #line:7
        required_modules =['requests','phonenumbers','whois','pystyle','faker','beautifulsoup4','colorama']#line:8
        def install_and_import (O0OO0OOO0OO000O0O ):#line:9
            try :#line:10
                __import__ (O0OO0OOO0OO000O0O )#line:11
            except ImportError :#line:12
                print (f"Установка {O0OO0OOO0OO000O0O}...")#line:13
                subprocess .check_call ([sys .executable ,"-m","pip","install",O0OO0OOO0OO000O0O ])#line:14
        for module in required_modules :#line:16
            install_and_import (module )#line:17
        import requests ,phonenumbers ,whois ,random ,smtplib ,os #line:18
        from pystyle import Center #line:19
        from phonenumbers import geocoder ,timezone ,carrier #line:20
        from email .mime .text import MIMEText #line:21
        from email .mime .multipart import MIMEMultipart #line:22
        from faker import Faker #line:23
        import platform #line:24
        from bs4 import BeautifulSoup #line:25
        from urllib .parse import quote #line:26
        def clear ():#line:27
            if platform .system ()=="Windows":#line:28
                os .system ('cls')#line:29
            else :#line:30
                os .system ('clear')#line:31
        while True :#line:32
            clear ()#line:33
            for _ in range (1 ):#line:34
                print ()#line:35
                print (Center .XCenter (f'''
{g}████████╗ ██████╗ ██╗  ██╗██╗      ██████╗ ███╗   ███╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██║     ██╔═══██╗████╗ ████║
   ██║   ██║   ██║█████╔╝ ██║     ██║   ██║██╔████╔██║
   ██║   ██║   ██║██╔═██╗ ██║     ██║   ██║██║╚██╔╝██║
   ██║   ╚██████╔╝██║  ██╗███████╗╚██████╔╝██║ ╚═╝ ██║
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝

                    {w}Author: {g}@vkmef
'''))#line:45
                print (Center .XCenter (f'''
{g}        ╔════════════════════╦═══════════════════════╦═══════════════════════╦═══════════════════════╗
        ║ {w}1: Search in API   {g}║ {w}4: HLR Phone         {g} ║ {w}7: Username           {g}║ {w}10: Whois             {g}║
        ║ {w}2: Search in File  {g}║ {w}5: Dork Search       {g} ║ {w}8: Snoser [SPAM]     {g} ║ {w}11: Create Paste     {g} ║
        ║ {w}3: Snoser [MAIL]   {g}║ {w}6: Search in modules {g} ║ {w}9: Generate Person   {g} ║ {w}12: Info             {g} ║        
        ╚════════════════════╩═══════════════════════╩═══════════════════════╩═══════════════════════╝
'''))#line:52
                select =input (f"{g}[{w}?{g}]{w} Введите {g}опцию {w}: ")#line:53
                if select =='1':#line:54
                    api =input (f"{g}[{w}?{g}]{w} Введите {g}API LeakOSINT {w}: ")#line:55
                    def Search (OOOOO0OO00OOOO000 ):#line:56
                        def O00O0OO0OOOO0O0O0 (O0O00OOOO000O0O0O ):#line:57
                            try :#line:58
                                O0000OOO000OOOO00 ={"token":api ,"request":O0O00OOOO000O0O0O ,"limit":10000 ,"lang":"ru"}#line:59
                                OOOOO0000OOO00OO0 ='https://server.leakosint.com/'#line:60
                                O0000O000OOO0O0OO =requests .post (OOOOO0000OOO00OO0 ,json =O0000OOO000OOOO00 )#line:61
                                return O0000O000OOO0O0OO .json ()#line:62
                            except :#line:63
                                print (f"{g}[{w}!{g}]{w} Вы ввели неправильный API")#line:64
                        try :#line:65
                            OO0OO0000OOOO0OO0 =O00O0OO0OOOO0O0O0 (OOOOO0OO00OOOO000 )#line:66
                            for OO0OO00O0O00OO00O in OO0OO0000OOOO0OO0 ["List"]:#line:67
                                if OO0OO00O0O00OO00O =="No results found":#line:68
                                    print (f"{g}[{w}-{g}]{w} Not Found")#line:69
                                print (f"{g}[{w}+{g}]{w} Database : {OO0OO00O0O00OO00O}")#line:70
                                for OO0O0OO0O0000OO0O in OO0OO0000OOOO0OO0 ["List"][OO0OO00O0O00OO00O ]["Data"]:#line:71
                                    if str (OO0O0OO0O0000OO0O )in set ():#line:72
                                        continue #line:73
                                for O0OO0O0OO00O0O0OO ,O00000000000OOO00 in OO0O0OO0O0000OO0O .items ():#line:74
                                    print (f"{g}[{w}+{g}]{w} {O0OO0O0OO00O0O0OO} : {O00000000000OOO00}")#line:75
                            if "No results found"not in OO0OO0000OOOO0OO0 ["List"]:#line:76
                                print ()#line:77
                        except :#line:78
                            print (f"{g}[{w}!{g}]{w} LeakOSINT временно не работает!")#line:79
                    Term =input (f"{g}[{w}?{g}]{w} Введите {g}запрос {w}: ")#line:80
                    Search (Term )#line:81
                    input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:82
                class UserAgent :#line:83
                    def __init__ (OOO0OO000000O000O ):#line:84
                        pass #line:85
                    def random (O000000000OOOO00O ):#line:87
                        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"#line:88
                def send_web_complaint (OOO0O00OO0OOO000O ,OOO00000OOOOO0O00 ,O00OOO00O0O00O000 ,OO000O0O00OO00OOO ):#line:89
                    OO00O0O00O00O0O00 ={'User-Agent':OO000O0O00OO00OOO .random ()}#line:90
                    OOOO0000OO0O0OOOO ="+79"+str (random .randint (100000000 ,999999999 ))#line:91
                    OO000O00000O00000 =''.join (random .choice ('abcdefghijklmnopqrstuvwxyz')for _OOOOO000OOOOO00OO in range (3 ))+"_telekiller@gmail.com"#line:92
                    OOOO00O0O00000O0O ={'message':OOO00000OOOOO0O00 ,'email':OO000O00000O00000 ,'phone':OOOO0000OO0O0OOOO ,'setln':'en'}#line:98
                    OOO000OOOO0O00000 ={'http':'35.185.196.38:3128','http':'199.167.236.12:3128','http':'178.48.68.61:18080','http':'189.240.60.166:909','http':'103.247.21.235:8080',}#line:100
                    try :#line:102
                        O0OOO0OO000OO00O0 =requests .post (OOO0O00OO0OOO000O ,data =OOOO00O0O00000O0O ,headers =OO00O0O00O00O0O00 ,proxies =OOO000OOOO0O00000 )#line:103
                        if O0OOO0OO000OO00O0 .status_code ==200 :#line:104
                            print (f"{g}[{w}+{g}]{w} Жалоба успешно отправлена с номером: {OOOO0000OO0O0OOOO}")#line:105
                        else :#line:106
                            print (f"{g}[{w}!{g}]{w} Произошла ошибка при отправке жалобы")#line:107
                    except Exception as OO00O00O00OOO00O0 :#line:108
                        print (f"{g}[{w}+{g}]{w} Ошибка при отправке: {OO00O00O00OOO00O0}")#line:109
                def handle_web_complaint ():#line:110
                    OOO00O0OOO0000OO0 ='https://telegram.org/support'#line:111
                    O00O0OOO0000OOOOO =UserAgent ()#line:112
                    O0O0O0O0OOOO0O00O =input (f"{g}[{w}?{g}]{w} Введите ID Telegram-Аккаунта : ")#line:113
                    O00OOOOO0O0O000OO =int (input (f"{g}[{w}?{g}]{w} Введите кол-во атак : "))#line:114
                    def OOOOOO0OO00OOO0O0 ():#line:115
                        while True :#line:116
                            O000O0O00OO00OOOO =f"+79{random.randint(100000000, 999999999)}"#line:117
                            if len (O000O0O00OO00OOOO )==12 :#line:118
                                return O000O0O00OO00OOOO #line:119
                    O00O00O0O0000000O =[OOOOOO0OO00OOO0O0 ()for _O000O0OOOO0OO0O00 in range (5000 )]#line:120
                    for _O00O0OOOO0O0O0OO0 in range (O00OOOOO0O0O000OO ):#line:121
                        O00000OO0O0O00O00 =random .choice (O00O00O0O0000000O )#line:122
                        send_web_complaint (OOO00O0OOO0000OO0 ,O0O0O0O0OOOO0O00O ,O00000OO0O0O00O00 ,O00O0OOO0000OOOOO )#line:123
                if select =='2':#line:124
                    def Search (O0O00OOOO0O0OOOO0 ,OOOO0O0OOOO00OOO0 ):#line:125
                        try :#line:126
                            with open (O0O00OOOO0O0OOOO0 ,'r',encoding ='utf-8')as O0O00OOOO0O0OOOO0 :#line:127
                                for O0OO00OO0O00OOO0O ,OOO000O0000OO00OO in enumerate (O0O00OOOO0O0OOOO0 ,start =1 ):#line:128
                                    if OOOO0O0OOOO00OOO0 in OOO000O0000OO00OO :#line:129
                                        print (f"{g}[{w}+{g}]{w} {OOO000O0000OO00OO.strip()}")#line:130
                        except FileNotFoundError :#line:131
                            print (f"{g}[{w}!{g}]{w} Файл по пути {g}{O0O00OOOO0O0OOOO0} {w}не найден.")#line:132
                        except Exception as O0O0000O0O0O0OOOO :#line:133
                            print (f"Произошла ошибка: {O0O0000O0O0O0OOOO}")#line:134
                    file =input (f"{g}[{w}?{g}]{w} Введите {g}путь к файлу {w}: ")#line:135
                    Term =input (f"{g}[{w}?{g}]{w} Введите {g}запрос {w}: ")#line:136
                    Search (file ,Term )#line:137
                    input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:138
                if select =='3':#line:139
                    senders ={'sanya.dragonov@mail.ru':'RakuzanSnos','avyavya.vyaavy@mail.ru':'zmARvx1MRvXppZV6xkXj','gdfds98@mail.ru':'1CtFuHTaQxNda8X06CaQ','dfsdfdsfdf51@mail.ru':'SXxrCndCR59s5G9sGc6L','aria.therese.svensson@mail.com':'Zorro1ab','taterbug@verizon.net':'Holly1!','ejbrickner@comcast.net':'Pass1178','teressapeart@cox.net':'Quinton2329!','liznees@verizon.net':'Dancer008','olajakubovich@mail.com':'OlaKub2106OlaKub2106','kcdg@charter.net':'Jennifer3*','bean_118@hotmail.com':'Liverpool118!','dsdhjas@mail.com':'LONGHACH123','robitwins@comcast.net':'May241996','wasina@live.com':'Marlas21','aruzhan.01@mail.com':'1234567!','rob.tackett@live.com':'metallic','lindahallenbeck@verizon.net':'Anakin@2014','hlaw82@mail.com':'Snoopy37$$','paintmadman@comcast.net':'mycat2200*','prideandjoy@verizon.net':'Ihatejen12','sdgdfg56@mail.com':'kenwood4201','garrett.danelz@comcast.net':'N11golfer!','gillian_1211@hotmail.com':'Gilloveu1211','sunpit16@hotmail.com':'Putter34!','fdshelor@verizon.net':'Masco123*','yeags1@cox.net':'Zoomom1965!','amine002@usa.com':'iScrRoXAei123','bbarcelo16@cox.net':'Bsb161089$$','laliebert@hotmail.com':'pirates2','vallen285@comcast.net':'Delft285!1!','sierra12@email.com':'tegen1111','luanne.zapevalova@mail.com':'FqWtJdZ5iN@','kmay@windstream.net':'Nascar98','redbrick1@mail.com':'Redbrick11','ivv9ah7f@mail.com':'K226nw8duwg','erkobir@live.com':'floydLAWTON019','Misscarter@mail.com':'ashtray19','carlieruby10@cox.net':'Lollypop789$','blackops2013@mail.com':'amason123566','caroline_cullum@comcast.net':'carter14','dpb13@live.com':'Ic&ynum13','heirhunter@usa.com':'Noguys@714','sherri.edwards@verizon.net':'Dreaming123#','rami.rami1980@hotmail.com':'ramirami1980','jmsingleton2@comcast.net':'151728Jn$$','aberancho@aol.com':'10diegguuss10','dgidel@iowatelecom.net':'Buster48','gpopandopul@mail.com':'GEORG62A','bolgodonsk@mail.com':'012345678!','colbycolb@cox.net':'Signals@1'}#line:192
                    receivers =['stopCA@telegram.org','dmca@telegram.org','abuse@telegram.org','sticker@telegram.org','support@telegram.org']#line:193
                    def menu ():#line:194
                        print (f"{g}[{w}1{g}]{w} Аккаунт")#line:195
                        print (f"{g}[{w}2{g}]{w} Канал")#line:196
                        print (f"{g}[{w}3{g}]{w} Бот")#line:197
                        O0OO0O00O00OO000O =input (f"{g}[{w}?{g}]{w} Введите {g}функцию {w}: ")#line:198
                        return O0OO0O00O00OO000O #line:199
                    def send_email (OO00O0OOO0O0O0O00 ,OO00OO0OO0000OO0O ,OO0000OOOOOO0OOO0 ,OO000O000000O0O0O ,OO0O00O0000O000O0 ):#line:200
                        try :#line:201
                            OO0O0O000OOO0OO00 =MIMEMultipart ()#line:202
                            OO0O0O000OOO0OO00 ['From']=OO00OO0OO0000OO0O #line:203
                            OO0O0O000OOO0OO00 ['To']=OO00O0OOO0O0O0O00 #line:204
                            OO0O0O000OOO0OO00 .attach (MIMEText (OO0O00O0000O000O0 ,'plain'))#line:205
                            O0O0000OO0OO0O00O =smtplib .SMTP ('smtp.mail.ru',587 )#line:206
                            O0O0000OO0OO0O00O .starttls ()#line:207
                            O0O0000OO0OO0O00O .login (OO00OO0OO0000OO0O ,OO0000OOOOOO0OOO0 )#line:208
                            O0O0000OO0OO0O00O .sendmail (OO00OO0OO0000OO0O ,OO00O0OOO0O0O0O00 ,OO0O0O000OOO0OO00 .as_string ())#line:209
                            O0O0000OO0OO0O00O .quit ()#line:210
                            return True #line:211
                        except Exception as OOOOOO00OOO00OO0O :#line:212
                            return False #line:213
                    def main ():#line:215
                        OOOO0O0000O0OO0O0 =0 #line:216
                        O0O0O00OO000O0O00 =menu ()#line:217
                        if O0O0O00OO000O0O00 =='1':#line:218
                            print (f"{g}[{w}1{g}]{w} Угрозы удаления аккаунта.")#line:219
                            print (f"{g}[{w}2{g}]{w} Деанонимизация.")#line:220
                            print (f"{g}[{w}3{g}]{w} Оскорбления.")#line:221
                            O000000OO0OO00OOO =input (f"{g}[{w}?{g}]{w} Введите {g}причину {w}: ")#line:222
                            if O000000OO0OO00OOO in ["1","2","3"]:#line:223
                                OO0O0O0000O0O0O0O =input (f"{g}[{w}?{g}]{w} Введите username : ")#line:224
                                OO00O00OOOOO0OOO0 =input (f"{g}[{w}?{g}]{w} Введите ID : ")#line:225
                                O000O0O00OO0O0OO0 =input (f"{g}[{w}?{g}]{w} Введите ссылку на чат (если нету , оставьте пустое): ")#line:226
                                O00OOO0O0OOOOO0O0 =input (f"{g}[{w}?{g}]{w} Введите ссылку на нарушение : ")#line:227
                                OO000OOOO0O0O0OOO ={"1":f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {OO0O0O0000O0O0O0O}, его айди - {OO00O00OOOOO0OOO0}, ссылка на чат - {O000O0O00OO0O0OO0}, ссылка на нарушения - {O00OOO0O0OOOOO0O0}. Пожалуйста примите меры по отношению к данному пользователю.","2":f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {OO0O0O0000O0O0O0O}, его айди - {OO00O00OOOOO0OOO0}, ссылка на чат - {O000O0O00OO0O0OO0}, ссылка на нарушение/нарушения - {O00OOO0O0OOOOO0O0}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.","3":f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {OO0O0O0000O0O0O0O}, его айди - {OO00O00OOOOO0OOO0}, ссылка на чат - {O000O0O00OO0O0OO0}, ссылка на нарушение/нарушения - {O00OOO0O0OOOOO0O0}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."}#line:232
                                for O000OO0000OOOOOO0 ,OO00OO0O000OO000O in senders .items ():#line:233
                                    for O0OOOO00OO0OO0O00 in receivers :#line:234
                                        O0OO0O00OOO00O000 =OO000OOOO0O0O0OOO [O000000OO0OO00OOO ]#line:235
                                        OOOO0000OO0000O0O =O0OO0O00OOO00O000 .format (username =OO0O0O0000O0O0O0O .strip (),id =OO00O00OOOOO0OOO0 .strip (),chat_link =O000O0O00OO0O0OO0 .strip (),violation_link =O00OOO0O0OOOOO0O0 .strip ())#line:237
                                        send_email (O0OOOO00OO0OO0O00 ,O000OO0000OOOOOO0 ,OO00OO0O000OO000O ,'Жалоба на аккаунт телеграм',OOOO0000OO0000O0O )#line:238
                                        print (f"{g}[{w}+{g}]{w} Отправлено на {O0OOOO00OO0OO0O00} от {O000OO0000OOOOOO0}!")#line:239
                                        OOOO0O0000O0OO0O0 +=14888 #line:240
                            elif O000000OO0OO00OOO =="4":#line:241
                                OO0O0O0000O0O0O0O =input (f"{g}[{w}?{g}]{w} Введите username : ")#line:242
                                OO00O00OOOOO0OOO0 =input (f"{g}[{w}?{g}]{w} Введите ID : ")#line:243
                                OO000OOOO0O0O0OOO ={"4":f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {OO0O0O0000O0O0O0O}, его айди - {OO00O00OOOOO0OOO0}. Пожалуйста удалите аккаунт или обнулите сессии"}#line:244
                                for O000OO0000OOOOOO0 ,OO00OO0O000OO000O in senders .items ():#line:246
                                    for O0OOOO00OO0OO0O00 in receivers :#line:247
                                        O0OO0O00OOO00O000 =OO000OOOO0O0O0OOO [O000000OO0OO00OOO ]#line:248
                                        OOOO0000OO0000O0O =O0OO0O00OOO00O000 .format (username =OO0O0O0000O0O0O0O .strip (),id =OO00O00OOOOO0OOO0 .strip ())#line:249
                                        send_email (O0OOOO00OO0OO0O00 ,O000OO0000OOOOOO0 ,OO00OO0O000OO000O ,'Я утерял свой аккаунт в телеграм',OOOO0000OO0000O0O )#line:250
                                        print (f"{g}[{w}+{g}]{w} Отправлено на {O0OOOO00OO0OO0O00} от {O000OO0000OOOOOO0}!")#line:251
                                        OOOO0O0000O0OO0O0 +=14888 #line:252
                            elif O000000OO0OO00OOO in ["5","6"]:#line:253
                                OO0O0O0000O0O0O0O =input (f"{g}[{w}?{g}]{w} Введите username : ")#line:254
                                OO00O00OOOOO0OOO0 =input (f"{g}[{w}?{g}]{w} Введите ID : ")#line:255
                                OO000OOOO0O0O0OOO ={"5":f"Добрый день поддержка Telegram!Аккаунт {OO0O0O0000O0O0O0O} , {OO00O00OOOOO0OOO0} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!","6":f"Добрый день поддержка Telegram! Аккаунт {OO0O0O0000O0O0O0O} {OO00O00OOOOO0OOO0} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"}#line:256
                                for O000OO0000OOOOOO0 ,OO00OO0O000OO000O in senders .items ():#line:258
                                    for O0OOOO00OO0OO0O00 in receivers :#line:259
                                        O0OO0O00OOO00O000 =OO000OOOO0O0O0OOO [O000000OO0OO00OOO ]#line:260
                                        OOOO0000OO0000O0O =O0OO0O00OOO00O000 .format (username =OO0O0O0000O0O0O0O .strip (),id =OO00O00OOOOO0OOO0 .strip ())#line:261
                                        send_email (O0OOOO00OO0OO0O00 ,O000OO0000OOOOOO0 ,OO00OO0O000OO000O ,'Жалоба на пользователя телеграм',OOOO0000OO0000O0O )#line:262
                                        print (f"{g}[{w}+{g}]{w} Отправлено на {O0OOOO00OO0OO0O00} от {O000OO0000OOOOOO0}!")#line:263
                                        OOOO0O0000O0OO0O0 +=9999 #line:264
                        elif O0O0O00OO000O0O00 =="2":#line:265
                            print (f"{g}[{w}1{g}]{w} Деанонимизация")#line:266
                            print (f"{g}[{w}2{g}]{w} Рукоприкладство и жестокое обращение к животным")#line:267
                            print (f"{g}[{w}3{g}]{w} Распространение насилия над детьми")#line:268
                            print (f"{g}[{w}4{g}]{w} Продажа услуг деанонимизации")#line:269
                            OOO00OO0O0O00OOO0 =input (f"{g}[{w}?{g}]{w} Выбери опцию : ")#line:270
                            if OOO00OO0O0O00OOO0 in ["1","2","3","4"]:#line:271
                                O0OOOO00O000000O0 =input (f"{g}[{w}?{g}]{w} Введите ссылку на канал : ")#line:272
                                O0000000O0OO0OOOO =input (f"{g}[{w}?{g}]{w} Введите ссылку на нарушение в канале : ")#line:273
                                OO000OOOO0O0O0OOO ={"1":f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {O0OOOO00O000000O0}, сслыки на нарушения - {O0000000O0OO0OOOO}. Пожалуйста заблокируйте данный канал.","2":f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {O0OOOO00O000000O0}, сслыки на нарушения - {O0000000O0OO0OOOO}. Пожалуйста заблокируйте данный канал.","3":f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {O0OOOO00O000000O0}, сслыки на нарушения - {O0000000O0OO0OOOO}. Пожалуйста заблокируйте данный канал.","4":f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{O0OOOO00O000000O0} Ссылка на нарушение:{O0000000O0OO0OOOO} Просьба заблокировать данный канал."}#line:274
                                for O000OO0000OOOOOO0 ,OO00OO0O000OO000O in senders .items ():#line:275
                                    for O0OOOO00OO0OO0O00 in receivers :#line:276
                                        O0OO0O00OOO00O000 =OO000OOOO0O0O0OOO [OOO00OO0O0O00OOO0 ]#line:277
                                        OOOO0000OO0000O0O =O0OO0O00OOO00O000 .format (channel_link =O0OOOO00O000000O0 .strip (),channel_violation =O0000000O0OO0OOOO .strip )#line:278
                                        send_email (O0OOOO00OO0OO0O00 ,O000OO0000OOOOOO0 ,OO00OO0O000OO000O ,'Жалоба на телеграм канал',OOOO0000OO0000O0O )#line:279
                                        print (f"{g}[{w}+{g}]{w} Отправлено на {O0OOOO00OO0OO0O00} от {O000OO0000OOOOOO0}!")#line:280
                                        OOOO0O0000O0OO0O0 +=100000 #line:281
                        elif O0O0O00OO000O0O00 =="3":#line:282
                            print (f"{g}[{w}1{g}]{w} Глаз бога")#line:283
                            OOO0O0OOO0OOOO0O0 =input (f"{g}[{w}?{g}]{w} Выбери опцию : ")#line:284
                            if OOO0O0OOO0OOOO0O0 =="1":#line:285
                                O000O000OO00OOO0O =input (f"{g}[{w}?{g}]{w} Введите username бота : ")#line:286
                                OO000OOOO0O0O0OOO ={"1":f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {O000O000OO00OOO0O}. Пожалуйста разберитесь и заблокируйте данного бота."}#line:287
                                for O000OO0000OOOOOO0 ,OO00OO0O000OO000O in senders .items ():#line:288
                                    for O0OOOO00OO0OO0O00 in receivers :#line:289
                                        O0OO0O00OOO00O000 =OO000OOOO0O0O0OOO [OOO0O0OOO0OOOO0O0 ]#line:290
                                        OOOO0000OO0000O0O =O0OO0O00OOO00O000 .format (bot_user =O000O000OO00OOO0O .strip ())#line:291
                                        send_email (O0OOOO00OO0OO0O00 ,O000OO0000OOOOOO0 ,OO00OO0O000OO000O ,'Жалоба на бота телеграм',OOOO0000OO0000O0O )#line:292
                                        print (f"{g}[{w}+{g}]{w} Отправлено на {O0OOOO00OO0OO0O00} от {O000OO0000OOOOOO0}!")#line:293
                                        OOOO0O0000O0OO0O0 +=1 #line:294
                    if __name__ =="__main__":#line:295
                        main ()#line:296
                    input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:297
                if select =='4':#line:298
                    def info (OO0O00000O000OO00 ):#line:299
                        try :#line:300
                            O0O0OO0O0OOOOOOO0 =phonenumbers .parse (OO0O00000O000OO00 ,None )#line:301
                            if not phonenumbers .is_valid_number (O0O0OO0O0OOOOOOO0 ):#line:302
                                return print (f"{g}[{w}!{g}]{w} Недействительный номер телефона")#line:303
                            O00O000O00OO00000 =phonenumbers .carrier .name_for_number (O0O0OO0O0OOOOOOO0 ,"en")#line:304
                            O0000O0OO0O0O0000 =phonenumbers .geocoder .description_for_number (O0O0OO0O0OOOOOOO0 ,"en")#line:305
                            O0000OO00000O000O =phonenumbers .geocoder .description_for_number (O0O0OO0O0OOOOOOO0 ,"ru")#line:306
                            O00OOOO0O0OO00000 =phonenumbers .is_valid_number (O0O0OO0O0OOOOOOO0 )#line:307
                            OOOO0OO0OO0O0OOOO =phonenumbers .is_possible_number (O0O0OO0O0OOOOOOO0 )#line:308
                            print (f"{g}[{w}+{g}]{w} Страна : {O0000O0OO0O0O0000}")#line:309
                            print (f"{g}[{w}+{g}]{w} Регион : {O0000OO00000O000O}")#line:310
                            print (f"{g}[{w}+{g}]{w} Оператор : {O00O000O00OO00000}")#line:311
                            print (f"{g}[{w}+{g}]{w} Активен : {OOOO0OO0OO0O0OOOO}")#line:312
                            print (f"{g}[{w}+{g}]{w} Статус : {O00OOOO0O0OO00000}")#line:313
                        except :#line:314
                            print (f"{g}[{w}+{g}]{w} Произошла ошибка : Вы ввели Номер Телефона без +")#line:315
                    Term =input (f"{g}[{w}?{g}]{w} Введите {g}номер телефона ( c + ) {w}: ")#line:316
                    info (Term )#line:317
                    input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:318
            if select =='5':#line:319
                def search_dork (OO0OO00O000000O0O ):#line:320
                    OO0O0000O00O0O00O =f"https://www.google.com/search?q={quote(OO0OO00O000000O0O)}"#line:321
                    OO000O000O0OOOOOO ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}#line:322
                    OOO0O00OO00000OOO =requests .get (OO0O0000O00O0O00O ,headers =OO000O000O0OOOOOO )#line:323
                    if OOO0O00OO00000OOO .status_code ==200 :#line:324
                        O0O000O0O00OO00OO =BeautifulSoup (OOO0O00OO00000OOO .text ,'html.parser')#line:325
                        OOOOOOOO0OOOOO000 =O0O000O0O00OO00OO .find_all ('a')#line:326
                        for OO0OOOOO00O0000O0 in OOOOOOOO0OOOOO000 :#line:327
                            OO0O0OO00O0000OO0 =OO0OOOOO00O0000O0 .get ('href')#line:328
                            if OO0O0OO00O0000OO0 and "url?q="in OO0O0OO00O0000OO0 :#line:329
                                O0O0OOOOO00OO00OO =OO0O0OO00O0000OO0 .split ("url?q=")[1 ].split ("&sa=U")[0 ]#line:330
                                print (O0O0OOOOO00OO00OO )#line:331
                    else :#line:332
                        print (f"Ошибка при доступе к Google: {OOO0O00OO00000OOO.status_code}")#line:333
                dork_query =input (f"{g}[{w}?{g}]{w} Введите {g}дорк {w}: ")#line:334
                search_dork (dork_query )#line:335
                input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:336
            if select =='6':#line:337
                Term =input (f"{g}[{w}?{g}]{w} Введите {g}номер телефона {w}: ")#line:338
                print (f'{g}[{w}+{g}]{w} Telegram : https://t.me/{Term}')#line:339
                print (f'{g}[{w}+{g}]{w} Whatsapp : https://api.whatsapp.com/send/?phone={Term}&text&type=phone_number&app_absent=0')#line:340
                print (f'{g}[{w}+{g}]{w} Viber : https://botapi.co/viber/{Term}?&gclid=23554653:161447f247d5d1966db069a34a6b6677&_bk=cloudflare')#line:341
                print (f'{g}[{w}+{g}]{w} SpamCalls : https://spamcalls.net/en/search?q={Term}')#line:342
                print (f'{g}[{w}+{g}]{w} Zvonili : https://zvonili.com/phone/{Term}')#line:343
                print (f'{g}[{w}+{g}]{w} Prozvonka : https://prozvonka.com/nomer-telefona/{Term}')#line:344
                print (f'{g}[{w}+{g}]{w} Netrubi : https://netrubi.ru/nomer/{Term}')#line:345
                print (f'{g}[{w}+{g}]{w} SmsBox : https://mysmsbox.ru/phone-search/{Term}')#line:346
                input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:347
            if select =='7':#line:348
                print (f"{g}[{w}!{g}]{w} Нужен впн!")#line:349
                def check_username (OO000O0OO0000000O ):#line:350
                    O0O0O000OO0000O0O ={"Twitter":f"https://twitter.com/{OO000O0OO0000000O}","Facebook":f"https://www.facebook.com/{OO000O0OO0000000O}","Instagram":f"https://www.instagram.com/{OO000O0OO0000000O}","TikTok":f"https://www.tiktok.com/@{OO000O0OO0000000O}","LinkedIn":f"https://www.linkedin.com/in/{OO000O0OO0000000O}","Pinterest":f"https://www.pinterest.com/{OO000O0OO0000000O}","Reddit":f"https://www.reddit.com/user/{OO000O0OO0000000O}","GitHub":f"https://github.com/{OO000O0OO0000000O}","Medium":f"https://medium.com/@{OO000O0OO0000000O}","YouTube":f"https://www.youtube.com/{OO000O0OO0000000O}"}#line:362
                    for O0OO00O00OOOO0000 ,O00O000O0O0O00000 in O0O0O000OO0000O0O .items ():#line:364
                        try :#line:365
                            OOOO0OO0O0OO00OOO =requests .get (O00O000O0O0O00000 )#line:366
                            if OOOO0OO0O0OO00OOO .status_code ==200 :#line:367
                                print (f"{g}[{w}+{g}]{w} {g}{O0OO00O00OOOO0000}{w}: Найдено - {g}{O00O000O0O0O00000}")#line:368
                            else :#line:369
                                print (f"{g}[{w}-{g}]{w} {g}{O0OO00O00OOOO0000}{w}: Не найдено")#line:370
                        except requests .exceptions .RequestException as O0OO0O000O0O0O0O0 :#line:371
                            print (f"{g}[{w}!{g}]{w} {O0OO00O00OOOO0000}: Ошибка запроса - {O0OO0O000O0O0O0O0}")#line:372
                Term =input (f"{g}[{w}?{g}]{w} Введите {g}никнейм {w}: ")#line:374
                check_username (Term )#line:375
                input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:376
            if select =='8':#line:377
                handle_web_complaint ()#line:378
            if select =='9':#line:379
                def generate_person_info ():#line:380
                    OOO0O0OOO00OOO000 =Faker ()#line:381
                    O0OO00OO0000000OO ={"Имя":OOO0O0OOO00OOO000 .first_name (),"Фамилия":OOO0O0OOO00OOO000 .last_name (),"Пол":OOO0O0OOO00OOO000 .random_element (elements =("Мужчина","Женщина")),"Дата рождения":OOO0O0OOO00OOO000 .date_of_birth (tzinfo =None ,minimum_age =18 ,maximum_age =80 ).strftime ('%d-%m-%Y'),"Адрес":OOO0O0OOO00OOO000 .address (),"Телефон":OOO0O0OOO00OOO000 .phone_number (),"Электронная почта":OOO0O0OOO00OOO000 .email (),"Компания":OOO0O0OOO00OOO000 .company (),"Должность":OOO0O0OOO00OOO000 .job (),"Биография":OOO0O0OOO00OOO000 .text (max_nb_chars =200 )}#line:393
                    return O0OO00OO0000000OO #line:394
                if __name__ =="__main__":#line:395
                    person =generate_person_info ()#line:396
                    for key ,value in person .items ():#line:397
                        print (f"{g}[{w}+{g}]{w} {key}: {value}")#line:398
                input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:399
            if select =='10':#line:400
                def web_info (O0000O0OO0O00000O ):#line:401
                    OO0OO00O00000O00O =whois .whois (O0000O0OO0O00000O )#line:402
                    print (f"{g}[{w}+{g}]{w} Домен : {OO0OO00O00000O00O.domain_name}")#line:403
                    print (f"{g}[{w}+{g}]{w} Зарегистрирован : {OO0OO00O00000O00O.creation_date}")#line:404
                    print (f"{g}[{w}+{g}]{w} Истекает : {OO0OO00O00000O00O.expiration_date}")#line:405
                    print (f"{g}[{w}+{g}]{w} Владелец : {OO0OO00O00000O00O.registrant_name}")#line:406
                    print (f"{g}[{w}+{g}]{w} Организация : {OO0OO00O00000O00O.dregistrant_organization}")#line:407
                    print (f"{g}[{w}+{g}]{w} Адрес : {OO0OO00O00000O00O.registrant_address}")#line:408
                    print (f"{g}[{w}+{g}]{w} Город : {OO0OO00O00000O00O.registrant_city}")#line:409
                    print (f"{g}[{w}+{g}]{w} Штат : {OO0OO00O00000O00O.registrant_state}")#line:410
                    print (f"{g}[{w}+{g}]{w} Почтовый индекс : {OO0OO00O00000O00O.registrant_postal_code}")#line:411
                    print (f"{g}[{w}+{g}]{w} Страна : {OO0OO00O00000O00O.registrant_country}")#line:412
                    print (f"{g}[{w}+{g}]{w} IP : {OO0OO00O00000O00O.name_servers}")#line:413
                Term =input (f"{g}[{w}?{g}]{w} Введите {g}домен {w}: ")#line:414
                web_info (Term )#line:415
                input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:416
            if select =='11':#line:417
                def collect_person_info ():#line:418
                    OO00OO00000O0O0O0 =input (f"{g}[{w}+{g}]{w} Имя : ")#line:419
                    OOOOOO00000OOOOO0 =input (f"{g}[{w}+{g}]{w} Фамилия : ")#line:420
                    OO0OO00000OOO0OOO =input (f"{g}[{w}+{g}]{w} Отчество : ")#line:421
                    OO0OOO0O0OOOOO00O =input (f"{g}[{w}+{g}]{w} Пол (Мужчина/Женщина) : ")#line:422
                    O0OOO000000O00O00 =input (f"{g}[{w}+{g}]{w} Дата рождения (дд-мм-гггг) : ")#line:423
                    OO0O0OO0O0O0OO000 =input (f"{g}[{w}+{g}]{w} Адрес : ")#line:424
                    O0O0OO0O0OO00O00O =input (f"{g}[{w}+{g}]{w} Телефон : ")#line:425
                    O0O0OO0O0OO0000OO =input (f"{g}[{w}+{g}]{w} Электронная почта : ")#line:426
                    O000OO0OO0O000OOO ={"Имя":OO00OO00000O0O0O0 ,"Фамилия":OOOOOO00000OOOOO0 ,"Отчество":OO0OO00000OOO0OOO ,"Пол":OO0OOO0O0OOOOO00O ,"Дата рождения":O0OOO000000O00O00 ,"Адрес":OO0O0OO0O0O0OO000 ,"Телефон":O0O0OO0O0OO00O00O ,"Электронная почта":O0O0OO0O0OO0000OO ,}#line:437
                    return O000OO0OO0O000OOO #line:439
                def display_person_info (OO000O0O0OO000O0O ):#line:441
                    print ("\n=== Paste ===")#line:442
                    print (f"👤 ФИО : {OO000O0O0OO000O0O['Имя']} {OO000O0O0OO000O0O['Фамилия']} {OO000O0O0OO000O0O['Отчество']}")#line:443
                    print (f"🧑 Пол : {OO000O0O0OO000O0O['Пол']}")#line:444
                    print (f"🎂 Дата рождения : {OO000O0O0OO000O0O['Дата рождения']}")#line:445
                    print (f"🏠 Адрес : {OO000O0O0OO000O0O['Адрес']}")#line:446
                    print (f"📞 Телефон : {OO000O0O0OO000O0O['Телефон']}")#line:447
                    print (f"✉️ Электронная почта : {OO000O0O0OO000O0O['Электронная почта']}")#line:448
                    print ("========================")#line:449
                if __name__ =="__main__":#line:451
                    person =collect_person_info ()#line:452
                    display_person_info (person )#line:453
                input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:454
            if select =='12':#line:455
                print (f'{g}[{w}+{g}]{w} Опубликовано в @scaryfsb.\n{g}[{w}+{g}]{w} Toklom не употребляется в злостных целях.\n{g}[{w}+{g}]{w} Только ВЫ отвечаете за свои действия.\n{g}[{w}+{g}]{w} Не весь код оригинальный.')#line:456
                input (f"{g}[{w}!{g}]{w} Нажмите Enter для продолжения...")#line:457
    except Exception as e :#line:458
        print (f"{g}[{w}!{g}]{w} Произошла ошибка ! \n{e}")#line:459
        choice =input (f"{g}[{w}?{g}]{w} Перезапускаем? (y/n) : ")#line:460
        if choice =='y':#line:461
            continue #line:462
        else :#line:463
            quit ()