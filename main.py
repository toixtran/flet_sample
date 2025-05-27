import flet as ft
from src.ui.layout import MainLayout

def main(page: ft.Page):
    page.title = "Demo Desktop App"
    page.window_width = 800
    page.window_height = 800
    page.theme_mode = ft.ThemeMode.LIGHT

    layout = MainLayout(page)
    page.add(layout)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
