import flet as ft

class Navbar(ft.UserControl):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate
    
    def build(self):
        return ft.Container(
            content=ft.Row([
                ft.TextButton("Login", on_click=lambda e: self.on_navigate("login")),
                ft.TextButton("Register", on_click=lambda e: self.on_navigate("register")),
                ft.TextButton("Dashboard", on_click=lambda e: self.on_navigate("dashboard")),
            ], alignment=ft.MainAxisAlignment.CENTER),
            bgcolor=ft.colors.BLUE_900,
            padding=10
        )