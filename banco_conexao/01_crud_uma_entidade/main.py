
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Importa a Base e a entidade do arquivo entidades.py
from entidades import Base, Pessoa

# --------- Utilidades ----------
def limpar_tela():
    """Limpa a tela do terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def criar_tab_pessoa(engine):
    """Cria a tabela 'Pessoa' no banco de dados."""
    try:
        Base.metadata.create_all(engine)
        print("Tabela criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar a tabela: {e}")

# --------- Operações CRUD ----------
def cadastrar_pessoa(session):
    """Cadastra uma nova pessoa no banco de dados."""
    try:
        nome = input("Digite o Nome do Usuário: ").strip().title()
        email = input("Digite Seu Email: ").strip().lower()
        data_nascimento = input("Data de Nascimento (dd/mm/aaaa): ").strip()

        # Valida data
        try:
            data_formatada = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        except ValueError:
            print("Data de nascimento inválida! Formato esperado: dd/mm/aaaa.")
            return

        # Verifica se o email já existe
        existe_email = session.query(Pessoa).filter(Pessoa.email == email).first()
        if existe_email:
            print("E-mail já cadastrado!")
            return

        nova_pessoa = Pessoa(nome=nome, email=email, data_nasc=data_formatada)
        session.add(nova_pessoa)
        session.commit()
        print(f"Pessoa '{nome}' cadastrada com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar: {e}")
        session.rollback()

def listar_pessoas(session):
    """Lista todas as pessoas cadastradas no banco de dados."""
    try:
        pessoas = session.query(Pessoa).all()
        if pessoas:
            print("\nLista de Pessoas:")
            for p in pessoas:
                nasc_str = p.data_nasc.strftime('%d/%m/%Y') if p.data_nasc else "-"
                print(f"ID: {p.id_pessoa} | Nome: {p.nome} | Email: {p.email} | Nasc: {nasc_str}")
        else:
            print("Nenhuma pessoa cadastrada.")
    except Exception as e:
        print(f"Erro ao listar: {e}")

def atualizar_pessoa(session):
    """Atualiza os dados de uma pessoa cadastrada."""
    try:
        id_alvo = input("Digite o ID da pessoa que deseja atualizar: ").strip()
        
        match id_alvo.isdigit():
            case True:
                id_alvo = int(id_alvo)
            case False:
                print("ID inválido.")
                return

        pessoa = session.get(Pessoa, id_alvo)
        match pessoa:
            case None:
                print("Pessoa não encontrada.")
                return
            case _:
                print("Deixe em branco para manter o valor atual.")
                novo_nome = input(f"Nome atual ({pessoa.nome}): ").strip()
                novo_email = input(f"Email atual ({pessoa.email}): ").strip().lower()
                atual_data = pessoa.data_nasc.strftime('%d/%m/%Y') if pessoa.data_nasc else "-"
                nova_data = input(f"Data Nascimento atual ({atual_data}): ").strip()

                # Verifica se novo_email já existe em outro registro
                if novo_email and novo_email != pessoa.email:
                    existe_email = session.query(Pessoa).filter(Pessoa.email == novo_email).first()
                    if existe_email:
                        print("E-mail já cadastrado para outra pessoa!")
                        return

                if novo_nome:
                    pessoa.nome = novo_nome.title()
                if novo_email:
                    pessoa.email = novo_email
                if nova_data:
                    try:
                        pessoa.data_nasc = datetime.strptime(nova_data, "%d/%m/%Y").date()
                    except ValueError:
                        print("Data de nascimento inválida! Formato esperado: dd/mm/aaaa.")
                        return

                session.commit()
                print("Pessoa atualizada com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar: {e}")
        session.rollback()

def deletar_pessoa(session):
    """Deleta uma pessoa do banco de dados."""
    try:
        id_alvo = input("Digite o ID da pessoa que deseja deletar: ").strip()
        match id_alvo.isdigit():
            case True:
                id_alvo = int(id_alvo)
            case False:
                print("ID inválido.")
                return

        pessoa = session.get(Pessoa, id_alvo)
        match pessoa:
            case None:
                print("Pessoa não encontrada.")
                return
            case _:
                confirmar = input(f"Tem certeza que deseja deletar '{pessoa.nome}'? (s/n): ").strip().lower()
                match confirmar:
                    case 's':
                        session.delete(pessoa)
                        session.commit()
                        print("Pessoa deletada com sucesso!")
                    case _:
                        print("Operação cancelada.")
    except Exception as e:
        print(f"Erro ao deletar: {e}")
        session.rollback()

# --------- App ---------
def main():
    """Função principal que executa o menu e as operações do CRUD."""
    # Garante diretório do banco (opcional)
    db_path = "01_crud_uma_entidade/database"
    os.makedirs(db_path, exist_ok=True)

    # Cria o banco de dados e a conexão com o SQLAlchemy
    engine = create_engine(f"sqlite:///{db_path}/db_crud.db", echo=False, future=True)
    criar_tab_pessoa(engine)

    # Cria a sessão para interagir com o banco
    Session = sessionmaker(bind=engine, future=True)
    session = Session()

    while True:
        limpar_tela()
        print("MENU".center(30, "-"))
        print("1 - Cadastrar Pessoa")
        print("2 - Listar Pessoas")
        print("3 - Atualizar Pessoa")
        print("4 - Deletar Pessoa")
        print("5 - Sair")
        print("-" * 30)

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                limpar_tela()
                cadastrar_pessoa(session)
            case "2":
                limpar_tela()
                listar_pessoas(session)
            case "3":
                limpar_tela()
                atualizar_pessoa(session)
            case "4":
                limpar_tela()
                deletar_pessoa(session)
            case "5":
                print(f'{"-"*30}\nFIM DO PROGRAMA\n{"-"*30}')
                break
            case _:
                print("Opção inválida!")

        input("\nPressione Enter para continuar...")

    session.close()

if __name__ == "__main__":
    main()
