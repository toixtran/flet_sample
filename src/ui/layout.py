import flet as ft
from src.ui.components.navbar import Navbar
from src.ui.screens.login import LoginScreen
from src.ui.screens.register import RegisterScreen
from src.ui.screens.dashboard import DashboardScreen

class MainLayout(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.navbar = Navbar(self.on_navigate)
        self.content = ft.Container(content=LoginScreen(self.on_navigate))
    
    def on_navigate(self, route: str):
        if route == "login":
            self.content.content = LoginScreen(self.on_navigate)
        elif route == "register":
            self.content.content = RegisterScreen(self.on_navigate)
        elif route == "dashboard":
            self.content.content = DashboardScreen(self.on_navigate)
        self.update()
    
    def build(self):
        return ft.Column([
            self.navbar,
            ft.Container(
                content=self.content,
                expand=True,
                padding=20
            )
        ])