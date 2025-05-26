import flet as ft

class DashboardScreen(ft.Column):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate

        self.controls = [
            ft.Text("Welcome to Dashboard", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("This is your personal dashboard"),
            ft.ElevatedButton("Back to Login",
                            on_click=lambda e: self.on_navigate("login"))
        ]
