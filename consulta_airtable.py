import flet as ft
import nube as nb


def main(page: ft.Page):
    # Abrir conexión a la base de datos
    nb.farmacia_ujat.connect()

    page.title = "Recetas"
    page.theme_mode = "light"
    page.scroll = True
    page.appbar = ft.AppBar(
        title=ft.Text("Listado de medicamentos UJAT"),
        leading=ft.Icon("LIST_ALT", color=ft.Colors.WHITE),
        bgcolor="blue",
        center_title=True,
    )
    encabezado = [
        ft.DataColumn(ft.Text("Medicamento")),
        ft.DataColumn(ft.Text("Interacciones"))
    ]
    filas = []

    datos = nb.Receta.select()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.medicamento))
        celda2 = ft.DataCell(ft.Text(d.interacciones))
        fila = ft.DataRow([celda1, celda2])
        filas.append(fila)

    tbl_medicamentos = ft.DataTable(
        columns=encabezado,
        rows=filas
    )
    page.add(tbl_medicamentos)
    page.update()

    nb.farmacia_ujat.close()


if __name__ == "__main__":
    ft.app(target=main,view=ft.AppView.WEB_BROWSER)
