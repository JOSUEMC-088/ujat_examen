import flet as ft
import modelo as md

def main(page: ft.Page):
    # Función para guardar el medicamento
    def guardar_medicamento(e: ft.ControlEvent):
        clave = txt_clave.value.strip()
        nombre = txt_descripcion.value.strip()
        presentacion = txt_presentacion.value.strip()
        clasificacion = drp_clasificacion.value
        nivel = drp_nivel.value
        farmaco = drp_farmaco.value

        # Validación de campos
        if clave == "":
            page.open(ft.SnackBar(ft.Text("Introduce la clave")))
            return
        if nombre == "":
            page.open(ft.SnackBar(ft.Text("Introduce el nombre")))
            return
        if presentacion == "":
            page.open(ft.SnackBar(ft.Text("Introduce la presentación")))
            return
        if clasificacion is None:
            page.open(ft.SnackBar(ft.Text("Introduce la clasificación")))
            return
        if nivel is None:
            page.open(ft.SnackBar(ft.Text("Introduce el nivel de atención")))
            return
        if farmaco is None:
            page.open(ft.SnackBar(ft.Text("Selecciona un fármaco")))
            return

        # Obtener objeto Farmaco
        farmaco_obj = md.Farmaco.get_or_none(md.Farmaco.nombre == farmaco)
        if not farmaco_obj:
            page.open(ft.SnackBar(ft.Text("Fármaco no encontrado")))
            return

        # Guardar en la base de datos
        md.Medicamento.create(
            clave=clave,
            descripcion=nombre,
            presentacion=presentacion,
            clasificacion=clasificacion,
            nivel_atencion=nivel,
            nombre_farmaco=farmaco_obj
        )

        # Mostrar mensaje y limpiar campos
        page.open(ft.SnackBar(ft.Text("Guardado exitosamente"), bgcolor="blue", show_close_icon=True))
        txt_clave.value = "S/C"
        txt_descripcion.value = ""
        txt_presentacion.value = ""
        drp_clasificacion.value = None
        drp_nivel.value = None
        drp_farmaco.value = None
        page.update()

    # Configuración de la página
    page.title = "Alta de medicamentos"
    page.theme_mode = "light"
    page.window.width = 450
    page.window.height = 500
    page.window_resizable = False
    page.appbar = ft.AppBar(
        leading=ft.Icon("medical_services"),
        title=ft.Text("Nuevo medicamento"),
        center_title=True,
        bgcolor="green",
        color="white"
    )

    # Componentes de la interfaz
    txt_clave = ft.TextField(label="Clave", width=200, border="underline", filled=True, value="S/C")
    txt_descripcion = ft.TextField(label="Nombre y Descripción del medicamento", multiline=True, min_lines=1, max_lines=3, width=400)
    txt_presentacion = ft.TextField(label="Presentación", multiline=True, min_lines=1, max_lines=3, width=400)

    # Dropdown de clasificación
    lista_clasificacion = []
    medicinas = md.Medicamento.select(md.Medicamento.clasificacion).distinct()
    for med in medicinas:
        lista_clasificacion.append(ft.dropdown.Option(med.clasificacion))
    drp_clasificacion = ft.Dropdown(options=lista_clasificacion, width=400, label="Clasificación")

    # Dropdown de nivel de atención
    lista_nivel = [
        ft.dropdown.Option("Nivel 1"),
        ft.dropdown.Option("Nivel 2"),
        ft.dropdown.Option("Nivel 3"),
        ft.dropdown.Option("Nivel 1 y 2"),
        ft.dropdown.Option("Nivel 1 y 3"),
        ft.dropdown.Option("Nivel 2 y 3"),
        ft.dropdown.Option("Nivel 1, 2 y 3")
    ]
    drp_nivel = ft.Dropdown(options=lista_nivel, width=400, label="Nivel de atención")

    # Dropdown de fármacos
    lista_farmacos = []
    farmacos = md.Farmaco.select(md.Farmaco.nombre).distinct()
    for far in farmacos:
        lista_farmacos.append(ft.dropdown.Option(far.nombre))
    drp_farmaco = ft.Dropdown(options=lista_farmacos, width=400, label="Fármaco o sustancia activa")

    # Botones
    btn_guardar = ft.ElevatedButton(
        text="Guardar",
        icon="save",
        icon_color="white",
        bgcolor="blue",
        color="white",
        width=150,
        on_click=guardar_medicamento
    )

    btn_cancelar = ft.ElevatedButton(
        text="Cancelar",
        icon='close',
        icon_color="white",
        bgcolor='red',
        color='white',
        width=150,
        # Puedes agregar on_click para cerrar o limpiar
    )

    fila_boton = ft.Row([btn_guardar, btn_cancelar], alignment="Center")

    # Agregar todos los componentes a la página
    page.add(
        txt_clave,
        txt_descripcion,
        txt_presentacion,
        drp_clasificacion,
        drp_nivel,
        drp_farmaco,
        fila_boton
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
