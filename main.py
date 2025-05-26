import flet as ft
from src.ui.layout import MainLayout
from src.database.db import init_db

def main(page: ft.Page):
    page.title = "Demo Desktop App"
    page.window_width = 800
    page.window_height = 600

    # Initialize database
    init_db()

    # Set up main layout
    layout = MainLayout(page)
    page.add(layout)

    page.update()

if __name__ == "__main__":
    ft.app(target=main)
