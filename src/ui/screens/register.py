import flet as ft
from src.services.auth_service import AuthService
from src.database.db import get_db
from contextlib import contextmanager

class RegisterScreen(ft.Column):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate
        self.email_field = ft.TextField(label="Email")
        self.password_field = ft.TextField(label="Password", password=True)
        self.error_text = ft.Text(color=ft.Colors.RED)

    def register_clicked(self, e):
        email = self.email_field.value
        password = self.password_field.value

        # Use context manager to handle database session
        with contextmanager(get_db)() as db:
            if AuthService.register_user(db, email, password):
                self.error_text.value = ""
                self.on_navigate("login")
            else:
                self.error_text.value = "Registration failed. Email might be taken."
            self.update()

    def build(self):
        return ft.Column([
            ft.Text("Register", size=30, weight=ft.FontWeight.BOLD),
            self.email_field,
            self.password_field,
            self.error_text,
            ft.ElevatedButton("Register", on_click=self.register_clicked),
            ft.TextButton("Already have an account? Login",
                         on_click=lambda e: self.on_navigate("login"))
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
