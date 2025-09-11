import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, expand=1, on_click=None):
        super().__init__(text=text, expand=expand, on_click=on_click)
        self.text = text
        self.expand = expand

class DigitButton(CalcButton):
    def __init__(self, text, expand=1, on_click=None):
        super().__init__(text, expand, on_click)
        self.bgcolor = ft.Colors.WHITE24
        self.color = ft.Colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text, on_click=None):
        super().__init__(text, on_click=on_click)
        self.bgcolor = ft.Colors.ORANGE
        self.color = ft.Colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text, on_click=None):
        super().__init__(text, on_click=on_click)
        self.bgcolor = ft.Colors.BLUE_GREY_100
        self.color = ft.Colors.BLACK

def main(page: ft.Page):
    page.title = "Calc App"
    page.bgcolor = ft.Colors.BLACK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    result = ft.Text(value="0", size=40, color=ft.Colors.WHITE)

    # Variável para guardar a expressão atual
    expression = ""

    def button_click(e):
        nonlocal expression
        btn = e.control
        text = btn.text

        if text == "AC":
            expression = ""
            result.value = "0"
        elif text == "+/-":
            # Tenta inverter o sinal do número atual
            try:
                if expression:
                    # Converte para float e multiplica por -1
                    num = float(expression)
                    num = -num
                    expression = str(num)
                    # Remove .0 se for inteiro
                    if num.is_integer():
                        expression = str(int(num))
                    result.value = expression
            except:
                pass
        elif text == "%":
            try:
                if expression:
                    num = float(expression)
                    num = num / 100
                    expression = str(num)
                    if num.is_integer():
                        expression = str(int(num))
                    result.value = expression
            except:
                pass
        elif text == "=":
            try:
                # Avalia a expressão matemática
                # Atenção: eval pode ser perigoso em apps reais
                result.value = str(eval(expression))
                expression = result.value
            except:
                result.value = "Erro"
                expression = ""
        else:
            # Para evitar começar com vários zeros
            if expression == "0" and text not in [".", "+", "-", "*", "/"]:
                expression = ""

            expression += text
            result.value = expression

        result.update()

    container = ft.Container(
        width=350,
        bgcolor=ft.Colors.BLACK,
        border_radius=ft.border_radius.all(20),
        padding=20,
        content=ft.Column(
            controls=[
                ft.Row(controls=[result], alignment=ft.MainAxisAlignment.END),
                ft.Row(
                    controls=[
                        ExtraActionButton(text="AC", on_click=button_click),
                        ExtraActionButton(text="+/-", on_click=button_click),
                        ExtraActionButton(text="%", on_click=button_click),
                        ActionButton(text="/", on_click=button_click),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="7", on_click=button_click),
                        DigitButton(text="8", on_click=button_click),
                        DigitButton(text="9", on_click=button_click),
                        ActionButton(text="*", on_click=button_click),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="4", on_click=button_click),
                        DigitButton(text="5", on_click=button_click),
                        DigitButton(text="6", on_click=button_click),
                        ActionButton(text="-", on_click=button_click),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="1", on_click=button_click),
                        DigitButton(text="2", on_click=button_click),
                        DigitButton(text="3", on_click=button_click),
                        ActionButton(text="+", on_click=button_click),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="0", expand=2, on_click=button_click),
                        DigitButton(text=".", on_click=button_click),
                        ActionButton(text="=", on_click=button_click),
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            spacing=15,
        )
    )

    page.add(container)


ft.app(main)
