import flet as ft
from src.services.auth_service import AuthService
from src.database.db import get_db
from contextlib import contextmanager

class LoginScreen(ft.Container):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate

        # Controls
        self.email_field = ft.TextField(label="Email")
        self.password_field = ft.TextField(label="Password", password=True)
        self.error_text = ft.Text(color=ft.Colors.RED)

        # Content
        self.content = ft.Column([
            ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
            self.email_field,
            self.password_field,
            self.error_text,
            ft.ElevatedButton("Login", on_click=self.login_clicked),
            ft.TextButton("Don't have an account? Register",
                         on_click=lambda e: self.on_navigate("register"))
        ])

        #Style
        self.padding = 20
        self.expand = True

    def login_clicked(self, e):
        email = self.email_field.value
        password = self.password_field.value

        if not email or not password:
            self.error_text.value = "Email and password are required."
            e.page.update()
            return

        # Use context manager to handle database session
        with contextmanager(get_db)() as db:
            if AuthService.login_user(db, email, password):
                self.error_text.value = ""
                e.page.update()
                self.on_navigate("dashboard")
            else:
                self.error_text.value = "Invalid email or password"
                e.page.update()
