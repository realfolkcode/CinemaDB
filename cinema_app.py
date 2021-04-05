import tkinter as tk
from pages.auth_page import AuthPage
from pages.admin_page import AdminPage
from pages.user_page import UserPage

# основной класс GUI

class CinemaApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(False, False)
        self.title("Сеть кинотеатров")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (AuthPage, UserPage, AdminPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AuthPage)

    def show_frame(self, cont):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[cont]
        frame.grid()