import flet as ft

def main(page: ft.Page):
    page.title = "Índice de Massa Corporal"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # campos de entrada
    peso = ft.TextField(label="Peso", suffix_text="kg")
    altura = ft.TextField(label="Altura", suffix_text="metros")

    # conteúdo dinâmico da caixa de diálogo
    conteudo_dialogo = ft.Text(value="", size=20, weight="bold")

    # caixa de diálogo
    dig_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Resultado"),
        content=conteudo_dialogo,
        actions=[ft.TextButton("OK", on_click=lambda e: page.dialog.close())],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # função de cálculo
    def calcular_imc(e):
        peso.error_text = ""
        altura.error_text = ""

        if not peso.value:
            peso.error_text = "Peso não pode ficar vazio!"
        if not altura.value:
            altura.error_text = "Altura não pode ficar vazia!"

        if peso.error_text or altura.error_text:
            page.update()
            return

        try:
            peso_float = float(peso.value.replace(",", "."))
            altura_float = float(altura.value.replace(",", "."))
            imc = peso_float / (altura_float ** 2)

            if imc < 18.5:
                classificacao = "Abaixo do peso"
            elif imc < 25:
                classificacao = "Peso normal"
            elif imc < 30:
                classificacao = "Sobrepeso"
            elif imc < 35:
                classificacao = "Obesidade grau I"
            elif imc < 40:
                classificacao = "Obesidade grau II"
            else:
                classificacao = "Obesidade grau III"

            conteudo_dialogo.value = f"Seu IMC é {imc:.2f}\nClassificação: {classificacao}"
            page.dialog = dig_modal
            dig_modal.open = True
            page.update()

        except ValueError:
            peso.error_text = "Valor inválido!"
            altura.error_text = "Valor inválido!"
            page.update()

    # função para limpar os campos
    def limpar_campos(e):
        peso.value = ""
        altura.value = ""
        peso.error_text = ""
        altura.error_text = ""
        conteudo_dialogo.value = ""
        dig_modal.open = False
        page.update()

    # barra superior
    page.appbar = ft.AppBar(title=ft.Text("IMC", size=16))

    # layout
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Índice de Massa Corporal", size=40, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        ft.ResponsiveRow([
            ft.Container(peso, col={"sm": 4, "md": 4, "xl": 2}),
            ft.Container(altura, col={"sm": 4, "md": 4, "xl": 2}),
        ],
        alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([
            ft.ElevatedButton("Calcular IMC", on_click=calcular_imc),
            ft.ElevatedButton("Executar", on_click=calcular_imc),
            ft.ElevatedButton("Limpar", on_click=limpar_campos),
        ],
        alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
