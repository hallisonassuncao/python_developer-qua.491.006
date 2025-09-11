import flet as ft

def main(page: ft.Page):
    # Propriedades da página
    page.title = "Eventos"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Variáveis
    texto = ft.TextField(label="Digite aqui o seu texto:")
    result = ft.Text()

    # Função de evento 
    def exibir_texto(e):
        result.value = f"Você digitou: {texto.value}"
        page.update()

    # Layout
    page.add(
        ft.SafeArea(
            ft.Container(
                content=ft.Text("App Evento", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        texto,
        ft.ElevatedButton("Enviar", on_click=exibir_texto),
        result
    )

ft.app(target=main)
