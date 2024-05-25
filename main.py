from config import app_name, bg_color, logo_color_yellow
from data import *

import flet as ft

def main(page: ft.Page):
    page.title = app_name
    page.theme_mode = ft.ThemeMode.LIGHT

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def page_show_best_options(destino, presupuesto):
        print(presupuesto, type(presupuesto))
        # TODO: Muestre las mejores opciones para el destino ingresado en una ft.Card, que muestre 3 opciones de hoteles y restaurantes
        options = search_best_hotel_and_restaurant(destino, budget=presupuesto)
        
        page.views.clear()
        page.views.append(
            ft.View(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text("Mejores opciones para ti:"),
                            ft.Text(f"Hotel: {options[0]}"),
                            ft.Text(f"Restaurante: {options[1]}"),
                        ]
                    )
                ]
            )
        )
        page.update()

    def page_ask_destination(e):
        page.views.clear()
        page.views.append(
            ft.View(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text("Ingrese su destino aqui:"),
                            ft.TextField(
                                label="Destino",
                                on_change=lambda e: setattr(page, "destino", e.control.value),
                            ),
                            
                            ft.Text("Ingrese su presupuesto"),
                            ft.Dropdown(
                                options=[
                                    ft.dropdown.Option("$"),
                                    ft.dropdown.Option("$$"),
                                    ft.dropdown.Option("$$$")
                                ],
                                on_change=lambda e: setattr(page, "presupuesto", e.control.value)
                            ),
                            ft.ElevatedButton("Next", on_click=lambda e: page_show_best_options(getattr(page, "destino", ""), getattr(page, "presupuesto", "$$$"))),
                        ]
                    )
                ]
            )
        )
        page.update()

    page_ask_destination(None)

ft.app(target=main)
