import flet as ft

class DashboardScreen(ft.Container):
    def __init__(self, on_navigate):
        super().__init__(
            padding=20,
            expand=True,
        )
        self.on_navigate = on_navigate

        column = ft.Column(
            controls=[
                ft.Text("Welcome to Dashboard", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("This is your personal dashboard"),
                ft.ElevatedButton("Back to Login", on_click=lambda e: self.on_navigate("login")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

        self.content = column
