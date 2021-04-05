import tkinter as tk
import sql
from tkinter import ttk

# основная страница администратора
class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.rowconfigure(0, minsize=100)
        self.rowconfigure(1, minsize=500)
        self.columnconfigure(0, minsize=200)
        self.columnconfigure(1, minsize=650)

        self.user_lbl = tk.Label(master=self, text="admin", bg="white", font=("Courier", 14))
        self.user_lbl.grid(row=0, column=0, sticky="w", padx=20)

        main_frm = tk.Frame(master=self)
        main_frm.grid(row=1, column=1, sticky="nsew")
        main_frm.grid_rowconfigure(0, weight=1)
        main_frm.grid_columnconfigure(0, weight=1)

        menu_frm = tk.Frame(master=self, bg="white")
        menu_frm.grid(row=1, column=0, sticky="nsew")

        add_film_btn = tk.Button(master=menu_frm, text="Добавить фильм",
                                 command=lambda: self.show_frame(AddFilm))
        add_film_btn.pack(fill=tk.X, padx=20, pady=10)

        add_person_btn = tk.Button(master=menu_frm, text="Добавить кинодеятеля",
                                   command=lambda: self.show_frame(AddPerson))
        add_person_btn.pack(fill=tk.X, padx=20, pady=10)

        add_credits_btn = tk.Button(master=menu_frm, text="Добавить титры",
                                    command=lambda: self.show_frame(AddCredits))
        add_credits_btn.pack(fill=tk.X, padx=20, pady=10)

        add_theater_btn = tk.Button(master=menu_frm, text="Добавить кинотеатр",
                                    command=lambda: self.show_frame(AddTheater))
        add_theater_btn.pack(fill=tk.X, padx=20, pady=10)

        add_room_btn = tk.Button(master=menu_frm, text="Добавить зал",
                                 command=lambda: self.show_frame(AddHall))
        add_room_btn.pack(fill=tk.X, padx=20, pady=10)

        add_session_btn = tk.Button(master=menu_frm, text="Добавить сеанс",
                                    command=lambda: self.show_frame(AddSession))
        add_session_btn.pack(fill=tk.X, padx=20, pady=10)

        self.frames = {}

        for F in (AddFilm, AddPerson, AddTheater, AddHall, AddSession, AddCredits):
            frame = F(main_frm, self)
            self.frames[F] = frame
            frame.grid(row=1, column=1, sticky="nsew")

        self.show_frame(AddFilm)

    def show_frame(self, cont):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[cont]
        frame.grid()

# подстраница, добавление фильма
class AddFilm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, minsize=150)
        self.columnconfigure(1, minsize=400)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure([0,1,2,3,4,5,6,7], minsize=30)
        self.rowconfigure(8, minsize=200)
        self.rowconfigure(9, minsize=60)

        title_lbl = tk.Label(self, text="Название: ")
        title_lbl.grid(row=0, column=0, sticky="e")
        title_ent = tk.Entry(self)
        title_ent.grid(row=0, column=1, sticky="we")

        directors = []

        director_lbl = tk.Label(self, text="Режиссер: ")
        director_lbl.grid(row=1, column=0, sticky="e")
        director_cb = ttk.Combobox(self, values=directors)
        director_cb.grid(row=1, column=1, sticky="we")

        with open('genres.txt', 'r', encoding='utf-8') as f:
            genres = f.read().splitlines()

        genre_lbl = tk.Label(self, text="Жанр: ")
        genre_lbl.grid(row=2, column=0, sticky="e")
        genre_cb = ttk.Combobox(self, values=genres)
        genre_cb.grid(row=2, column=1, sticky="we")

        year_lbl = tk.Label(self, text="Год выпуска: ")
        year_lbl.grid(row=3, column=0, sticky="e")
        year_ent = tk.Entry(self)
        year_ent.grid(row=3, column=1, sticky="we")

        with open('countries.txt', 'r', encoding='utf-8') as f:
            countries = f.read().splitlines()

        country_lbl = tk.Label(self, text="Страна производства: ")
        country_lbl.grid(row=4, column=0, sticky="e")
        country_cb = ttk.Combobox(self, values=countries)
        country_cb.grid(row=4, column=1, sticky="we")

        length_lbl = tk.Label(self, text="Хронометраж: ")
        length_lbl.grid(row=5, column=0, sticky="e")
        length_ent = tk.Entry(self)
        length_ent.grid(row=5, column=1, sticky="we")

        imax_lbl = tk.Label(self, text="IMAX: ")
        imax_lbl.grid(row=6, column=0, sticky="e")
        ImaxCheck = tk.IntVar()
        imax_cbtn = tk.Checkbutton(self, variable=ImaxCheck,
                                   onvalue=1, offvalue=0)
        imax_cbtn.grid(row=6, column=1, sticky="w")

        threed_lbl = tk.Label(self, text="3D: ")
        threed_lbl.grid(row=7, column=0, sticky="e")
        ThreeDCheck = tk.IntVar()
        threed_cbtn = tk.Checkbutton(self, variable=ThreeDCheck,
                                   onvalue=1, offvalue=0)
        threed_cbtn.grid(row=7, column=1, sticky="w")

        description_lbl = tk.Label(self, text="Описание: ")
        description_lbl.grid(row=8, column=0, sticky="e")
        description_txt = tk.Text(self, height=1, width=1)
        description_txt.grid(row=8, column=1, sticky="nsew")

        add_btn = tk.Button(self, text="Добавить")
        add_btn.grid(row=9, column=1, sticky="nw", pady=15)


# подстраница, добавление кинодеятеля
class AddPerson(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, minsize=150)
        self.columnconfigure(1, minsize=400)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure([0,1,2], minsize=30)
        self.rowconfigure(3, minsize=410)

        name_lbl = tk.Label(self, text="Имя: ")
        name_lbl.grid(row=0, column=0, sticky="e")
        name_ent = tk.Entry(self)
        name_ent.grid(row=0, column=1, sticky="we")

        with open('countries.txt', 'r', encoding='utf-8') as f:
            countries = f.read().splitlines()

        country_lbl = tk.Label(self, text="Страна: ")
        country_lbl.grid(row=1, column=0, sticky="e")
        country_cb = ttk.Combobox(self, values=countries)
        country_cb.grid(row=1, column=1, sticky="we")

        birthday_lbl = tk.Label(self, text="Дата рождения: ")
        birthday_lbl.grid(row=2, column=0, sticky="e")
        birthday_ent = tk.Entry(self)
        birthday_ent.insert(tk.END, 'ДД.ММ.ГГГГ')
        birthday_ent.grid(row=2, column=1, sticky="we")

        add_btn = tk.Button(self, text="Добавить")
        add_btn.grid(row=3, column=1, sticky="nw", pady=15)



# подстраница, добавление титров
class AddCredits(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, minsize=150)
        self.columnconfigure(1, minsize=400)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure([0,1,2,3], minsize=30)
        self.rowconfigure(4, minsize=210)

        films = sql.query_with_fetchall("select * from фильм;")
        for i in range(len(films)):
            films[i] = films[i][0]

        film_lbl = tk.Label(self, text="Фильм: ")
        film_lbl.grid(row=0, column=0, sticky="e")
        film_cb = ttk.Combobox(self, values=films)
        film_cb.grid(row=0, column=1, sticky="we")

        persons = sql.query_with_fetchall("select * from кинодиетели;")

        person_lbl = tk.Label(self, text="Человек: ")
        person_lbl.grid(row=1, column=0, sticky="e")
        person_lb = tk.Listbox(self, height=10)
        person_lb.grid(row=1, column=1, sticky="we")
        for row in persons:
            person_lb.insert(tk.END, row)

        credits_lbl = tk.Label(self, text="Деятельность: ")
        credits_lbl.grid(row=2, column=0, sticky="e")
        credits_ent = tk.Entry(self)
        credits_ent.grid(row=2, column=1, sticky="we")

        info_lbl = tk.Label(self, text="Доп. информация: ")
        info_lbl.grid(row=3, column=0, sticky="e")
        info_ent = tk.Entry(self)
        info_ent.grid(row=3, column=1, sticky="we")

        add_btn = tk.Button(self, text="Добавить",
                            command=lambda: self.add_credits(film_cb, person_lb, credits_ent))
        add_btn.grid(row=4, column=1, sticky="nw", pady=15)


    def add_credits(self, film_cb, person_lb, credits_ent):
        film = film_cb.get()
        person = person_lb.get(tk.ANCHOR)
        credits = credits_ent.get()

        id = person[0]
        query = "insert into кинодиетели_в_фильме(название_фильма, kinodeyatel_id, функция_в_фильме) values ('" + film + "' ,"
        query = query + str(id) + ", '" + credits + "');"
        credits_id = sql.insert(query)



# подстраница, добавление кинотеатра
class AddTheater(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, minsize=150)
        self.columnconfigure(1, minsize=400)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure([0,1,2], minsize=30)
        self.rowconfigure(3, minsize=410)

        title_lbl = tk.Label(self, text="Название: ")
        title_lbl.grid(row=0, column=0, sticky="e")
        title_ent = tk.Entry(self)
        title_ent.grid(row=0, column=1, sticky="we")

        with open('cities.txt', 'r', encoding='utf-8') as f:
            cities = f.read().splitlines()

        city_lbl = tk.Label(self, text="Город: ")
        city_lbl.grid(row=1, column=0, sticky="e")
        city_cb = ttk.Combobox(self, values=cities)

        city_cb.grid(row=1, column=1, sticky="we")

        address_lbl = tk.Label(self, text="Адрес: ")
        address_lbl.grid(row=2, column=0, sticky="e")
        address_ent = tk.Entry(self)
        address_ent.grid(row=2, column=1, sticky="we")

        add_btn = tk.Button(self, text="Добавить")
        add_btn.grid(row=3, column=1, sticky="nw", pady=15)


# подстраница, добавление зала
class AddHall(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, minsize=150)
        self.columnconfigure(1, minsize=400)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure([0,1,2,3,4,5], minsize=30)
        self.rowconfigure(6, minsize=320)

        theaters = []

        theater_lbl = tk.Label(self, text="Кинотеатр: ")
        theater_lbl.grid(row=0, column=0, sticky="e")
        theater_cb = ttk.Combobox(self, values=theaters)
        theater_cb.grid(row=0, column=1, sticky="we")


        title_lbl = tk.Label(self, text="Название: ")
        title_lbl.grid(row=1, column=0, sticky="e")
        title_ent = tk.Entry(self)
        title_ent.grid(row=1, column=1, sticky="we")

        rows_lbl = tk.Label(self, text="Кол-во рядов: ")
        rows_lbl.grid(row=2, column=0, sticky="e")
        rows_ent = tk.Entry(self)
        rows_ent.grid(row=2, column=1, sticky="we")

        places_lbl = tk.Label(self, text="Кол-во мест в ряде: ")
        places_lbl.grid(row=3, column=0, sticky="e")
        places_ent = tk.Entry(self)
        places_ent.grid(row=3, column=1, sticky="we")

        imax_lbl = tk.Label(self, text="IMAX: ")
        imax_lbl.grid(row=4, column=0, sticky="e")
        ImaxCheck = tk.IntVar()
        imax_cbtn = tk.Checkbutton(self, variable=ImaxCheck,
                                   onvalue=1, offvalue=0)
        imax_cbtn.grid(row=4, column=1, sticky="w")

        threed_lbl = tk.Label(self, text="3D: ")
        threed_lbl.grid(row=5, column=0, sticky="e")
        ThreeDCheck = tk.IntVar()
        threed_cbtn = tk.Checkbutton(self, variable=ThreeDCheck,
                                   onvalue=1, offvalue=0)
        threed_cbtn.grid(row=5, column=1, sticky="w")

        add_btn = tk.Button(self, text="Добавить")
        add_btn.grid(row=6, column=1, sticky="nw", pady=15)


# подстраница, добавление сеанса
class AddSession(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, minsize=150)
        self.columnconfigure(1, minsize=400)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure([0,1,2,3,4,5,6,7], minsize=30)
        self.rowconfigure(8, minsize=170)

        films = sql.query_with_fetchall("select название from фильм")

        film_lbl = tk.Label(self, text="Фильм: ")
        film_lbl.grid(row=0, column=0, sticky="e")
        film_cb = ttk.Combobox(self, values=films)
        film_cb.grid(row=0, column=1, sticky="we")

        theaters = sql.query_with_fetchall("select * from кинотеатр")

        theater_lbl = tk.Label(self, text="Кинотеатр: ")
        theater_lbl.grid(row=1, column=0, sticky="e")
        self.theater_lb = tk.Listbox(self, height=5)
        for row in theaters:
            self.theater_lb.insert(tk.END, row)
        self.theater_lb.grid(row=1, column=1, sticky="we")
        self.theater_lb.bind("<<ListboxSelect>>", self.select_theater)

        hall_lbl = tk.Label(self, text="Зал: ")
        hall_lbl.grid(row=2, column=0, sticky="e")
        self.hall_lb = tk.Listbox(self, height=5)
        self.hall_lb.grid(row=2, column=1, sticky="we")

        date_lbl = tk.Label(self, text="Дата: ")
        date_lbl.grid(row=3, column=0, sticky="e")
        date_ent = tk.Entry(self)
        date_ent.grid(row=3, column=1, sticky="we")

        price_lbl = tk.Label(self, text="Цена: ")
        price_lbl.grid(row=4, column=0, sticky="e")
        price_ent = tk.Entry(self)
        price_ent.grid(row=4, column=1, sticky="we")

        imax_lbl = tk.Label(self, text="IMAX: ")
        imax_lbl.grid(row=5, column=0, sticky="e")
        ImaxCheck = tk.IntVar()
        imax_cbtn = tk.Checkbutton(self, variable=ImaxCheck,
                                   onvalue=1, offvalue=0)
        imax_cbtn.grid(row=5, column=1, sticky="w")

        threed_lbl = tk.Label(self, text="3D: ")
        threed_lbl.grid(row=6, column=0, sticky="e")
        ThreeDCheck = tk.IntVar()
        threed_cbtn = tk.Checkbutton(self, variable=ThreeDCheck,
                                   onvalue=1, offvalue=0)
        threed_cbtn.grid(row=6, column=1, sticky="w")

        add_btn = tk.Button(self, text="Добавить",
                            command=lambda: self.add_session(film_cb, date_ent, price_ent, ImaxCheck, ThreeDCheck))
        add_btn.grid(row=7, column=1, sticky="w")

        self.success_lbl = tk.Label(self, text="")
        self.success_lbl.grid(row=8, column=1, sticky="nw", pady=15)


    def select_theater(self, evt):
        self.hall_lb.delete(0, tk.END)

        theater = self.theater_lb.get(tk.ANCHOR)[0]
        query = "select * from зал where название_кинотеатра = '" + theater + "';"
        halls = sql.query_with_fetchall(query)
        for row in halls:
            self.hall_lb.insert(tk.END, row[0])


    def add_session(self, film_cb, date_ent, price_ent, ImaxCheck, ThreeDCheck):
        film = film_cb.get()
        if film[0] == '{':
            film = film[1:]
        if film[-1] == '}':
            film = film[:-1]
        hall = self.hall_lb.get(tk.ANCHOR)
        date = date_ent.get()
        imax = ImaxCheck.get()
        threed = ThreeDCheck.get()
        price = price_ent.get()

        film_imax, film_threed = sql.query_with_fetchall("select imax_flg, 3d_flg from фильм where название='" + film + "';")[0]
        hall_imax, hall_threed = sql.query_with_fetchall("select imax_flg, 3d_flg from зал where zal_id=" + str(hall) + ";")[0]

        success = True
        if imax==1 and film_imax==0:
            success = False
        if threed==1 and film_threed==0:
            success = False
        if imax==1 and hall_imax==0:
            success = False
        if threed==1 and hall_threed==0:
            success = False

        if success==False:
            self.success_lbl["text"] = "Ошибка"
            return

        query = "insert into сеанс(название_фильма, zal_id, дата_сеанса, imax_flg, 3d_flg, цена) values ('"\
                + film + "', " + str(hall) + ", '" + date + "', " + str(imax) + ", " + str(threed) \
                + ", " + str(price) + ");"

        print(query)
        session_id = sql.insert(query)

        query = "select колличество_рядов, колличество_мест_в_ряде from зал where zal_id=" + str(hall) + ";"
        print(query)
        num_rows, num_places = sql.query_with_fetchall(query)[0]
        for row in range(1, num_rows+1):
            for place in range(1, num_places+1):
                ticket_id = sql.insert("insert into билет(seans_id, ряд, место, цена) values ("
                                       + str(session_id) + ", " + str(row) + ", " + str(place) + ", " + str(price) + ");")

        if success==True:
            self.success_lbl["text"] = "Успех!"