import tkinter as tk
import sql
from tkinter import ttk

# основная страница для пользователя
class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.rowconfigure(0, minsize=100)
        self.rowconfigure(1, minsize=500)
        self.columnconfigure(0, minsize=200)
        self.columnconfigure(1, minsize=650)

        self.user_lbl = tk.Label(master=self, text="", bg="white", font=("Courier", 14))
        self.user_lbl.grid(row=0, column=0, sticky="w", padx=20)

        main_frm = tk.Frame(master=self)
        main_frm.grid(row=1, column=1, sticky="nsew")
        main_frm.grid_rowconfigure(0, weight=1)
        main_frm.grid_columnconfigure(0, weight=1)

        menu_frm = tk.Frame(master=self, bg="white")
        menu_frm.grid(row=1, column=0, sticky="nsew")

        search_film_btn = tk.Button(menu_frm, text="Поиск фильма",
                                    command=lambda: self.show_frame(SearchFilm))
        search_film_btn.pack(fill=tk.X, padx=20, pady=10)

        rating_film_btn = tk.Button(menu_frm, text="Рейтинг фильмов")
        rating_film_btn.pack(fill=tk.X, padx=20, pady=10)

        persons_btn = tk.Button(menu_frm, text="Киноперсоны")
        persons_btn.pack(fill=tk.X, padx=20, pady=10)

        self.frames = {}

        for F in (SearchFilm, FilmInfo, BuyTicket):
            frame = F(main_frm, self)
            self.frames[F] = frame
            frame.grid(row=1, column=1, sticky="nsew")

        self.show_frame(SearchFilm)


    def show_frame(self, cont):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[cont]
        frame.grid()


    def update_user_name(self, user_name):
        self.user_lbl['text'] = user_name



# подстраница, поиск фильма
class SearchFilm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, minsize=150)
        self.columnconfigure(1, minsize=400)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure([0, 1, 2, 3, 4], minsize=30)
        self.rowconfigure(5, minsize=290)
        self.rowconfigure(6, minsize=60)

        title_lbl = tk.Label(self, text="Название: ")
        title_lbl.grid(row=0, column=0, sticky="e")
        title_ent = tk.Entry(self)
        title_ent.grid(row=0, column=1, sticky="we")

        with open('genres.txt', 'r', encoding='utf-8') as f:
            genres = f.read().splitlines()

        genre_lbl = tk.Label(self, text="Жанр: ")
        genre_lbl.grid(row=1, column=0, sticky="e")
        genre_cb = ttk.Combobox(self, values=genres)
        genre_cb.grid(row=1, column=1, sticky="we")

        year_lbl = tk.Label(self, text="Год выпуска: ")
        year_lbl.grid(row=2, column=0, sticky="e")
        year_ent = tk.Entry(self)
        year_ent.grid(row=2, column=1, sticky="we")

        with open('countries.txt', 'r', encoding='utf-8') as f:
            countries = f.read().splitlines()

        country_lbl = tk.Label(self, text="Страна производства: ")
        country_lbl.grid(row=3, column=0, sticky="e")
        country_cb = ttk.Combobox(self, values=countries)
        country_cb.grid(row=3, column=1, sticky="we")

        search_btn = tk.Button(self, text="Искать",
                               command=lambda: self.show_results(title_ent, genre_cb, year_ent, country_cb, controller))
        search_btn.grid(row=4, column=1, sticky="nw")

        self.goto_btn = tk.Button(self, text="Перейти")

        self.results_lb = tk.Listbox(self)


    def show_results(self, title_ent, genre_cb, year_ent, country_cb, controller):
        self.results_lb.delete(0, tk.END)

        title = title_ent.get()
        genre = genre_cb.get()
        year = year_ent.get()
        country = country_cb.get()

        query = "select название, дата_выпуска from фильм where "
        and_flag = False
        if title != "":
            query = query + "название = '" + title + "'"
            and_flag = True
        if genre != "":
            if and_flag:
                query += " and "
            query = query + "жанр = '" + genre + "'"
            and_flag = True
        if year != "":
            if and_flag:
                query += " and "
            query = query + "year(дата_выпуска) = '" + year + "'"
            and_flag = True
        if country != "":
            if and_flag:
                query += " and "
            query = query + "страна = '" + country + "'"
        query = query + ";"

        rows = sql.query_with_fetchall(query)
        for row in rows:
            self.results_lb.insert(tk.END, row)
        self.results_lb.grid(row=5, column=1, sticky="nswe")
        self.goto_btn.grid(row=6, column=1, sticky="nw", pady=10)
        self.goto_btn['command'] = lambda: self.goto_film(controller)


    def goto_film(self, controller):
        title = self.results_lb.get(tk.ANCHOR)[0]
        query = "select * from фильм inner join режисер_фильма on фильм.название=режисер_фильма.название_фильма where название = '" + title + "';"

        row = sql.query_with_fetchall(query)[0]
        date = row[1]
        country = row[2]
        length = row[3]
        genre = row[4]
        director_id = row[9]

        director_in_film = sql.query_with_fetchall("select kinodeyatel_id from режисер_фильма where kinodeyatel_id = " + str(director_id) + ";")
        director = sql.query_with_fetchall("select ФИО from кинодиетели where kinodeyatel_id = " + str(director_in_film[0][0]) + ";")[0][0]
        #print(director_name)
        controller.frames[FilmInfo].update_info(title, genre, date, length, country, director)
        controller.show_frame(FilmInfo)



# подстраница, информация о фильме
class FilmInfo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(0, minsize=150)
        self.columnconfigure(1, minsize=400)
        self.columnconfigure(2, minsize=100)
        self.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], minsize=30)
        self.rowconfigure(8, minsize=200)
        self.rowconfigure(9, minsize=60)

        title_lbl = tk.Label(self, text="Название: ")
        title_lbl.grid(row=0, column=0, sticky="e")
        self.title_inf = tk.Label(self, text="")
        self.title_inf.grid(row=0, column=1, sticky="w")

        director_lbl = tk.Label(self, text="Режиссер: ")
        director_lbl.grid(row=1, column=0, sticky="e")
        self.director_inf = tk.Label(self, text="")
        self.director_inf.grid(row=1, column=1, sticky="w")

        genre_lbl = tk.Label(self, text="Жанр: ")
        genre_lbl.grid(row=2, column=0, sticky="e")
        self.genre_inf = tk.Label(self, text="")
        self.genre_inf.grid(row=2, column=1, sticky="w")

        date_lbl = tk.Label(self, text="Дата выпуска: ")
        date_lbl.grid(row=3, column=0, sticky="e")
        self.date_inf = tk.Label(self, text="")
        self.date_inf.grid(row=3, column=1, sticky="w")

        country_lbl = tk.Label(self, text="Страна производства: ")
        country_lbl.grid(row=4, column=0, sticky="e")
        self.country_inf = tk.Label(self, text="")
        self.country_inf.grid(row=4, column=1, sticky="w")

        length_lbl = tk.Label(self, text="Хронометраж")
        length_lbl.grid(row=5, column=0, sticky="e")
        self.length_inf = tk.Label(self, text="")
        self.length_inf.grid(row=5, column=1, sticky="w")

        score_lbl = tk.Label(self, text="Оценка: ")
        score_lbl.grid(row=6, column=0, sticky="e")
        self.score_inf = tk.Label(self, text="")
        self.score_inf.grid(row=6, column=1, sticky="e")

        choose_session_btn = tk.Button(self, text="Выбрать сеанс",
                                       command=lambda: self.show_sessions())
        choose_session_btn.grid(row=7, column=1, sticky="w")

        self.session_lb = tk.Listbox(self)

        self.buy_btn = tk.Button(self, text="Купить билет",
                                 command=lambda: self.buy_ticket(controller, self.session_lb))


    def update_info(self, title, genre, date, length, country, director):
        self.title_inf['text'] = title
        self.genre_inf['text'] = genre
        self.date_inf['text'] = date
        self.country_inf['text'] = country
        self.length_inf['text'] = length
        self.director_inf['text'] = director


    def show_sessions(self):
        self.session_lb.delete(0, tk.END)

        query = "select * from сеанс where название_фильма='" + self.title_inf['text'] + "';"
        sessions = sql.query_with_fetchall(query)
        for row in sessions:
            self.session_lb.insert(tk.END, row)

        self.session_lb.grid(row=8, column=1, sticky="nsew")
        self.buy_btn.grid(row=9, column=1, sticky="nw")


    def buy_ticket(self, controller, session_lb):
        session_id = session_lb.get(tk.ANCHOR)[0]
        controller.show_frame(BuyTicket)
        controller.frames[BuyTicket].show(session_id, controller)



# подстраница, покупка билета
class BuyTicket(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], minsize=25)
        self.rowconfigure([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19], minsize=25)


    def clear(self):
        for slave in self.grid_slaves():
            slave.destroy()


    def show(self, session_id, controller):
        self.clear()
        self.user = controller.user_lbl["text"]
        hall = sql.query_with_fetchall("select zal_id from сеанс where seans_id=" + str(session_id) + ";")[0][0]
        self.num_rows, self.num_places = sql.query_with_fetchall("select колличество_рядов, колличество_мест_в_ряде from зал where zal_id=" + str(hall) + ";")[0]

        query = "select ряд, место, num from билет where seans_id=" + str(session_id) + ";"
        self.ticket_id = dict((sublist[0:2], sublist[2]) for sublist in sql.query_with_fetchall(query))

        self.btns = {}
        for i in range(self.num_rows):
            for j in range(self.num_places):
                self.btns[(i+1, j+1)] = tk.Button(self, text=str(j + 1),
                                             command=lambda row=i+1, place=j+1: self.buy(row, place, session_id, self.user))
                self.btns[(i+1, j+1)].grid(row=i, column=j)

        self.update_btns(session_id)


    def update_btns(self, session_id):
        query = "select ряд, место, логин_пользователя from билет where seans_id=" + str(session_id) + ";"
        self.btns_flg = dict((sublist[0:2], sublist[2]) for sublist in sql.query_with_fetchall(query))
        for i in range(self.num_rows):
            for j in range(self.num_places):
                bg = "green"
                if self.btns_flg[(i+1, j+1)] != None:
                    bg = "red"
                self.btns[(i+1, j+1)]["bg"] = bg


    def buy(self, row, place, session_id, user):
        print(user)
        self.update_btns(session_id)
        if self.btns_flg[(row, place)] == None:
            sql.insert("update билет set логин_пользователя='" + user + "' where num=" + str(self.ticket_id[(row, place)]) + ";")
        self.update_btns(session_id)