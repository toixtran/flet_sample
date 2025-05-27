import flet as ft
from src.ui.components.navbar import Navbar
from src.ui.screens.login import LoginScreen
from src.ui.screens.register import RegisterScreen
from src.ui.screens.dashboard import DashboardScreen

class MainLayout(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.navbar = Navbar(self.on_navigate)
        self.height = 800
        self.navbar.width = 250

        self.content_container = ft.Container(
            content=LoginScreen(self.on_navigate),
            expand=True,
            padding=20,
        )

        self.content = ft.Row([
            self.navbar,
            ft.VerticalDivider(width=1),
            self.content_container
        ],
        expand=True,
        )


    def on_navigate(self, route: str):
        if route == "login":
            self.content_container.content = LoginScreen(self.on_navigate)
        elif route == "register":
            self.content_container.content = RegisterScreen(self.on_navigate)
        elif route == "dashboard":
            self.content_container.content = DashboardScreen(self.on_navigate)
        self.update()
