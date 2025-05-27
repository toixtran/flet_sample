import flet as ft
from src.ui.components.navbar import Navbar
from src.ui.screens.login import LoginScreen
from src.ui.screens.register import RegisterScreen
from src.ui.screens.dashboard import DashboardScreen

class MainLayout(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.navbar = Navbar(self.on_navigate)
        self.navbar.attach_page(page)
        self.content_container = ft.Container(expand=True)
        self.controls.append(self.content_container)
        self.content_container.content = LoginScreen(self.on_navigate)

    def on_navigate(self, route: str):
        if route == "login":
            self.content_container.content = LoginScreen(self.on_navigate)
            self.remove_navbar()
        elif route == "register":
            self.content_container.content = RegisterScreen(self.on_navigate)
            self.remove_navbar()
        elif route == "dashboard":
            self.content_container.content = DashboardScreen(self.on_navigate)
            self.add_navbar()
        else:
            self.content_container.content = ft.Text(f"404 - Page '{route}' not found")
            self.remove_navbar()
        self.update()

    def add_navbar(self):
        if self.navbar not in self.controls:
            self.controls.insert(0, self.navbar)
            self.page.drawer = self.navbar.drawer

    def remove_navbar(self):
        if self.navbar in self.controls:
            self.controls.remove(self.navbar)
            self.page.drawer = None
