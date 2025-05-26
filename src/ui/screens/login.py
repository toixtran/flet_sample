import flet as ft
from src.services.auth_service import AuthService
from src.database.db import get_db
from contextlib import contextmanager

class LoginScreen(ft.UserControl):
    def __init__(self, on_navigate):
        super().__init__()
        self.on_navigate = on_navigate
        self.email_field = ft.TextField(label="Email")
        self.password_field = ft.TextField(label="Password", password=True)
        self.error_text = ft.Text(color=ft.colors.RED)
    
    def login_clicked(self, e):
        email = self.email_field.value
        password = self.password_field.value
        
        # Use context manager to handle database session
        with contextmanager(get_db)() as db:
            if AuthService.login_user(db, email, password):
                self.error_text.value = ""
                self.on_navigate("dashboard")
            else:
                self.error_text.value = "Invalid email or password"
            self.update()
    
    def build(self):
        return ft.Column([
            ft.Text("Login", size=30, weight=ft.FontWeight.BOLD),
            self.email_field,
            self.password_field,
            self.error_text,
            ft.ElevatedButton("Login", on_click=self.login_clicked),
            ft.TextButton("Don't have an account? Register", 
                         on_click=lambda e: self.on_navigate("register"))
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)