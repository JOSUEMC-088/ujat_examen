import flet as ft
import modelo as md
import main as ma

def main(page: ft.Page):

    def regresar(e: ft.ControlEvent):
        page.clean()
        ma.main(page)

    # Configurar página
    page.title = "Consultas"
    page.window.width = 800
    page.window.height = 600
    page.theme_mode = "light"
    page.scroll = True

    page.appbar = ft.AppBar(
        title=ft.Text("Listado de medicamentos UJAT"),
        leading=ft.Icon("receipt_long"),
        bgcolor="blue",
        center_title=True,
    )

    # Botón regresar
    btn_regresar = ft.ElevatedButton(text="Regresar", icon="arrow_back", on_click=regresar)

    # Encabezado de la tabla
    encabezado = [
        ft.DataColumn(ft.Text("Descripción", width=200)),
        ft.DataColumn(ft.Text("Presentación", width=200)),
        ft.DataColumn(ft.Text("Clasificación", width=200)),
        ft.DataColumn(ft.Text("Nivel de atencion", width=100)),
        ft.DataColumn(ft.Text("Sustancia activa", width=200))
    ]

    # Cuerpo de la tabla
    filas = []
    medicinas = md.Medicamento.select()
    for med in medicinas:
        celda1 = ft.DataCell(ft.Text(med.descripcion, weight="bold"))
        celda2 = ft.DataCell(ft.Text(med.presentacion))
        celda3 = ft.DataCell(ft.Text(med.clasificacion, italic=True))
        celda4 = ft.DataCell(ft.Text(med.nivel_atencion))
        celda5 = ft.DataCell(ft.Text(med.descripcion, color="pink"))  # Verifica si querías `med.sustancia_activa` aquí
        fila = ft.DataRow([celda1, celda2, celda3, celda4, celda5])
        filas.append(fila)

    tbl_medicamentos = ft.DataTable(
        columns=encabezado,
        rows=filas
    )

    # Agregar componentes a la página
    page.add(btn_regresar, tbl_medicamentos)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
