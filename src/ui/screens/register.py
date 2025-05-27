import flet as ft
from src.services.auth_service import AuthService
from src.database.db import get_db
from contextlib import contextmanager
import os

class RegisterScreen(ft.Container):
    def __init__(self, on_navigate):
        super().__init__(
            expand=True,
            padding=20,
        )
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.on_navigate = on_navigate
        self.build_ui()

    def build_left_column(self):
        img_path = os.path.join(self.base_dir, "assets/images/bgimg.png")
        return ft.Container(
            content=ft.Image(src=img_path, fit=ft.ImageFit.CONTAIN),
            expand=True,
            bgcolor=ft.Colors.BLUE_100,
            padding=10,
            border_radius=10,
        )

    def build_right_column(self):
        self.title = ft.Text("Register", size=30, weight=ft.FontWeight.BOLD)
        self.email_field = ft.TextField(label="Email", width=300)
        self.password_field = ft.TextField(label="Password", password=True, width=300)
        self.error_text = ft.Text(value="", color=ft.Colors.RED)

        self.register_button = ft.ElevatedButton("Register", on_click=self.register_clicked)
        self.login_button = ft.TextButton(
            "Already have an account? Login",
            on_click=lambda e: self.on_navigate("login")
        )

        return ft.Column(
            controls=[
                self.title,
                self.email_field,
                self.password_field,
                self.error_text,
                self.register_button,
                self.login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            width=350,
        )

    def build_ui(self):
        left_col = self.build_left_column()
        right_col = self.build_right_column()
        self.content = ft.Row(
            controls=[left_col, right_col],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=40,
            expand=True,
        )
        self.content = self.content

    def register_clicked(self, e):
        email = self.email_field.value.strip()
        password = self.password_field.value.strip()

        if not email or not password:
            self.error_text.value = "Please enter both email and password"
            self.update()
            return

        with contextmanager(get_db)() as db:
            try:
                user = AuthService.register_user(db, email, password)
                self.error_text.value = ""
                self.on_navigate("login")
            except Exception as err:
                self.error_text.value = str(err)
                self.update()
