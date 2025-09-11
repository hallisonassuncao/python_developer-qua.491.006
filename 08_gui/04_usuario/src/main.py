import flet as ft
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: ft.TextField
    idade: ft.TextField
    peso: ft.TextField
    salario: ft.TextField
    email: ft.TextField

def main(page: ft.Page):
    # propriedades da pagina
    page.title = "Dados do Usuario"
    page.theme_mode = ft.ThemeMode.LIGHT      

    # variaveis de saida
    Saida_titulo = ft.Text(weight="bold")
    nome = ft.Text()
    idade = ft.Text()
    peso = ft.Text()
    salario = ft.Text()
    email = ft.Text()

    # função de evento
    def mostrar_dados(e):
        Saida_titulo.value = "Dados do Usuario\n"
        nome.value = f"Nome: {campo_nome.value}"
        idade.value = f"Idade: {campo_idade.value} anos"
        peso.value = f"Peso: {campo_peso.value} kg"
        salario.value = f"Salario: R$ {float(campo_salario.value):.2f}" if campo_salario.value else "Salario: R$ 0.00"
        email.value = f"Email: {campo_email.value}"
        page.update()

    # campos visuais
    campo_nome = ft.TextField(label="Nome")
    campo_idade = ft.TextField(label="Idade", suffix="anos")
    campo_peso = ft.TextField(label="Peso", suffix="kg")
    campo_salario = ft.TextField(label="Salario", prefix="R$")
    campo_email = ft.TextField(label="Email", on_submit=mostrar_dados)

    # instancia da classe 
    usuario = Pessoa(
        nome=campo_nome,
        idade=campo_idade,
        peso=campo_peso,
        salario=campo_salario,
        email=campo_email
    )

    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Dados do Usuario", size=30, weight="bold"),
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        usuario.nome,
        usuario.idade,
        usuario.peso,
        usuario.salario,
        usuario.email,
        ft.ElevatedButton("Enviar", on_click=mostrar_dados),  
        Saida_titulo, 
        nome,
        idade,
        peso,
        salario,
        email
    )

ft.app(main)
