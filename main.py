import flet as ft
import consulta_airtable as cat
import consultas as consul
import altas_medicamentos as altas_m

def main(page: ft.Page):

    def mostrar_interacciones(e: ft.ControlEvent):
        page.clean()
        cat.main(page)

    def mostras_medicamentos(e: ft.ControlEvent):
        page.clean()
        consul.main(page)
    
    def altas_medicameto(e: ft.ControlEvent):
        page.clean()
        altas_m.main(page)

    page.title = "FARMI-UJAT"
    page.bgcolor = "#F6F7FB"
    page.appbar = ft.AppBar(
        title=ft.Text("FARMI-UJAT", size=30, weight="bold"),
        center_title=True,
        bgcolor="white",
    )

    btn_interacciones = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(name="medication", size=40, color="green"),
                    ft.Text("Interacciones\nMedicamentosas", text_align=ft.TextAlign.CENTER, weight="bold", color="black")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            height=130,
            width=200,
            bgcolor="#FFE0B2",
            border_radius=10,
            padding=0,
        ),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=mostrar_interacciones
    )

    btn_medicamento = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(name="add_box", size=40, color="purple"),
                    ft.Text("Alta Medicamento", text_align=ft.TextAlign.CENTER, weight="bold", color="black")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            height=130,
            width=200,
            bgcolor="#C8E6C9",
            border_radius=10,
            padding=10
        ),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=altas_medicameto
    )

    btn_lista = ft.ElevatedButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(name="featured_play_list", size=40, color="brown"),
                    ft.Text("Lista Medicamento", text_align=ft.TextAlign.CENTER, weight="bold", color="black")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            height=130,
            width=200,
            bgcolor="#BBDEFB",
            border_radius=10,
            padding=0
        ),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
        on_click=mostras_medicamentos
    )

    page.add(
        ft.Divider(color="black"),
        ft.Container(
            content=ft.Row(
                controls=[btn_interacciones, btn_medicamento, btn_lista],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=30
            ),
            alignment=ft.alignment.center,
            padding=20
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
