import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro App Flet"
    page.add(
        ft.SafeArea(
            ft.Container(
                content=ft.Column([
                    ft.Text("Hallison!!\n❤️🎸🎸🎸"),
                    ft.Text("Rock🎸"),
                    
                ]),
                padding=20
            ),
            expand=True,
        ),
    )

ft.app(target=main)

