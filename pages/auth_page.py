import tkinter as tk
import sql
from pages.admin_page import AdminPage
from pages.user_page import UserPage

# страница авторизации
class AuthPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.rowconfigure([0, 2], minsize=125)
        self.rowconfigure(1, minsize=100)
        self.columnconfigure([0, 2], minsize=150)
        self.columnconfigure(1, minsize=300)


        auth_frm = tk.Frame(master=self)
        auth_frm.grid(row=1, column=1, sticky="nsew")

        auth_lbl = tk.Label(master=auth_frm, text="Авторизация")
        auth_lbl.pack()

        login_frm = tk.Frame(master=auth_frm)
        login_frm.rowconfigure(0, minsize=30)
        login_frm.columnconfigure(0, minsize=50)
        login_frm.columnconfigure(1)
        login_frm.columnconfigure(2, minsize=50)
        login_frm.pack()

        login_lbl = tk.Label(master=login_frm, text="Логин: ")
        login_lbl.grid(row=0, column=0, sticky="e")
        login_ent = tk.Entry(master=login_frm)
        login_ent.grid(row=0, column=1)


        password_frm = tk.Frame(master=auth_frm)
        password_frm.rowconfigure(0, minsize=30)
        password_frm.columnconfigure(0, minsize=50)
        password_frm.columnconfigure(1)
        password_frm.columnconfigure(2, minsize=50)
        password_frm.pack()

        password_lbl = tk.Label(master=password_frm, text="Пароль:")
        password_lbl.grid(row=0, column=0, sticky="e")
        password_ent = tk.Entry(master=password_frm)
        password_ent.grid(row=0, column=1)

        self.load_users()

        ok_btn = tk.Button(master=auth_frm, text="OK",
                           command=lambda: self.check_auth(controller, login_ent, password_ent, status_lbl))
        ok_btn.pack(pady=5)

        status_lbl = tk.Label(master=auth_frm, text="")
        status_lbl.pack()


    def check_auth(self, controller, login_ent, password_ent, status_lbl):
        login = login_ent.get()
        password = password_ent.get()

        if (login == 'admin') and (password == 'password'):
            controller.show_frame(AdminPage)
        elif (login in self.users) and (self.users[login] == password):
            controller.show_frame(UserPage)
            controller.frames[UserPage].update_user_name(login)
        else:
            print('Ошибка авторизации')
            status_lbl['text'] = 'Ошибка авторизации'


    def load_users(self):
        self.users = dict(sql.query_with_fetchall("SELECT логин, пароль FROM пользователь"))