import flet as ft

def main(page: ft.Page):
    page.title = "Calc App"
    expression = ""
    result = ft.Text(value="0", size=40)

    # Função de clique dos botões
    def button_click(e):
        nonlocal expression
        text = e.control.text

        if text == "AC":
            expression = ""
        elif text == "=":
            try:
                expression = str(eval(expression))
            except:
                expression = "Erro"
        elif text == "+/-":
            if expression.startswith("-"):
                expression = expression[1:]
            else:
                expression = "-" + expression
        elif text == "%":
            try:
                expression = str(float(expression) / 100)
            except:
                expression = "Erro"
        else:
            expression += text

        result.value = expression if expression else "0"
        result.update()

    # Interface organizada em linhas
    page.add(
        ft.Row(controls=[result], alignment="end"),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="AC", on_click=button_click),
                ft.ElevatedButton(text="+/-", on_click=button_click),
                ft.ElevatedButton(text="%", on_click=button_click),
                ft.ElevatedButton(text="/", on_click=button_click),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7", on_click=button_click),
                ft.ElevatedButton(text="8", on_click=button_click),
                ft.ElevatedButton(text="9", on_click=button_click),
                ft.ElevatedButton(text="*", on_click=button_click),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4", on_click=button_click),
                ft.ElevatedButton(text="5", on_click=button_click),
                ft.ElevatedButton(text="6", on_click=button_click),
                ft.ElevatedButton(text="-", on_click=button_click),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1", on_click=button_click),
                ft.ElevatedButton(text="2", on_click=button_click),
                ft.ElevatedButton(text="3", on_click=button_click),
                ft.ElevatedButton(text="+", on_click=button_click),
            ]
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="0", on_click=button_click),
                ft.ElevatedButton(text=".", on_click=button_click),
                ft.ElevatedButton(text="=", on_click=button_click),
            ]
        ),
    )

ft.app(main)

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text

        
