from config import app_name, bg_color, logo_color_yellow

import flet as ft

def main(page: ft.Page):
    page.title = app_name
    page.theme_mode = ft.ThemeMode.LIGHT

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    destinations = [
        ft.NavigationDestination(icon=ft.icons.TRAVEL_EXPLORE_ROUNDED, label="Plan it"),
        ft.NavigationDestination(icon=ft.icons.ROCKET_LAUNCH_SHARP, label="Surprise me"),
        ft.NavigationDestination(icon=ft.icons.INFO_OUTLINE, label="About us"),
    ]

    def format_number(number):
        return "{:,}".format(number).replace(",", ".")

    def change_tab(e):

        print("Selected tab:", e.control.selected_index)
        page.clean()

        cg = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="cheap", label="Cheap"),
        ft.Radio(value="mid", label="Mid"),
        ft.Radio(value="Fancy", label="Fancy")], alignment=ft.MainAxisAlignment.CENTER), on_change=lambda e: print(e.control.value))

        if e.control.selected_index == 0:
            page.add(
                ft.Text("Ingrese su destino aqui:"),
                ft.TextField(
                    on_change=lambda e: print(e.control.value)
                ),
                cg,
                ft.TextButton("Next")
            )
        elif e.control.selected_index == 1:
            page.add(ft.Text("Contenido para Sorprendeme"))
        elif e.control.selected_index == 2:
            page.add(ft.Text("Contenido para Sobre nosotros"))

    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=bg_color,
        inactive_color=ft.colors.WHITE,
        active_color=logo_color_yellow,
        on_change=change_tab,
        destinations=destinations
    )

    page.add(ft.Text("Hello world"))

ft.app(target=main)