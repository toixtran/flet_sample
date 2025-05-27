import flet as ft

class Navbar(ft.Container):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate

        # Style
        self.padding = 20

        self.content = ft.Column([
            ft.ElevatedButton(
                "Login",
                on_click=lambda e: self.on_navigate("login"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
                width=200
            ),
            ft.ElevatedButton(
                "Register",
                on_click=lambda e: self.on_navigate("register"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
                width=200
            ),
            ft.ElevatedButton(
                "Dashboard",
                on_click=lambda e: self.on_navigate("dashboard"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
                width=200
            ),
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
