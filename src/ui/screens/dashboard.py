import flet as ft

class DashboardScreen(ft.Container):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate

        # Content
        self.content = ft.Column([
            ft.Text("Welcome to Dashboard", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("This is your personal dashboard"),
            ft.ElevatedButton("Back to Login",
                            on_click=lambda e: self.on_navigate("login"))
        ],)

        #Style
        self.padding = 20
        self.expand = True
