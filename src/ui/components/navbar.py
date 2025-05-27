import flet as ft

class Navbar(ft.Container):
    def __init__(self, on_navigate):
        self.on_navigate = on_navigate

        self.drawer = ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(icon=ft.Icons.DASHBOARD, label="Dashboard"),
            ],
            on_change=self.drawer_navigate
        )

        super().__init__(
            content=ft.Row(
                [
                    ft.IconButton(icon=ft.Icons.MENU, on_click=self.open_drawer, icon_color=ft.Colors.WHITE),
                    ft.Text("My App", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=ft.Colors.BLUE_900,
            padding=10,
        )

    def attach_page(self, page: ft.Page):
        self.page = page
        self.page.drawer = self.drawer

    def open_drawer(self, e):
        if hasattr(self, "page") and self.page.drawer == self.drawer:
            self.page.drawer.open = True
            self.page.drawer.update()

    def drawer_navigate(self, e):
        index = e.control.selected_index
        route = ["dashboard"][index]
        self.on_navigate(route)
        self.page.drawer.open = False
        self.page.drawer.update()
