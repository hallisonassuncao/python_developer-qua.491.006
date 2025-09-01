from datetime import datetime
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Digite o nome da Pessoa: ").strip().title()
        email = input("Digite o Email: ").strip().lower()

        pessoas = session.query(Pessoa).filter(Pessoa.email == email).all()

        if email in [pessoa.email for pessoa in pessoas]:
            print("E-mail já cadastrado !")
        else:
            data_nasc = input("Digite a Data de Nascimento (dd/mm/aaaa): ").strip()

            data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y").date()
            nova_pessoa = Pessoa(nome=nome, email=email, data_nasc=data_nasc)

            session.add(nova_pessoa)
            session.commit()

            print(f"\nA Pessoa: {nome}, foi cadastrada com Sucesso!")
    except Exception as e:
        print(f"Não foi possível cadastrar! Erro: {e}")

def listar_pessoas(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        print("\nPESSOAS CADASTRADAS:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"Email: {pessoa.email}")
            print(f"Data_Nasc: {pessoa.data_nasc.strftime('%d/%m/%Y')}")
            print(f"{'-'*40}\n")
    except Exception as e:
        print(f"Não foi possível listar! Erro: {e}")

def pesquisar_pessoas(session, Pessoa):
    print(f"{'-'*20}  Filtrar pessoas por campo  {'-'*20}")
    print("1 - ID")
    print("2 - Nome")
    print("3 - E-mail")
    print("4 - Data de Nasc.")
    print("5 - Retornar")

    campo = input("Informe o Campo a pesquisar: ").strip()

    limpar()

    pessoas = []
    match campo:
        case "1":
            valor = input("Digite o ID: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.id_pessoa.like(f"{valor}")).all()
        case "2":
            valor = input("Digite o Nome: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.nome.like(f"%{valor}%")).all()
        case "3":
            valor = input("Digite o E-mail: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"%{valor}%")).all()
        case "4":
            valor = input("Digite a Data de Nasc. (dd/mm/aaaa): ").strip()
            try:
                data_nasc = datetime.strptime(valor, "%d/%m/%Y").date()
                pessoas = session.query(Pessoa).filter(Pessoa.data_nasc == data_nasc).all()
            except ValueError:
                print("Data inválida!")
                return
        case "5":
            return
        case _:
            print("Campo inexistente!")
            return

    limpar()

    print("\nRESULTADO DA PESQUISA:\n")
    if pessoas:
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Data de Nasc.: {pessoa.data_nasc.strftime('%d/%m/%Y')}\n")
            print(f"{'-'*40}\n")
    else:
        print("Nenhum registro encontrado!")

def alterar_dados(session, Pessoa):
    try:
        print("1 - Buscar por ID")
        print("2 - Buscar por Email")
        opcao = input("Escolha o campo para localizar a pessoa: ").strip()

        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe Email: ").strip()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case _:
                print("Opção inválida!")
                return

        if pessoa:
            novo_nome = None
            novo_email = None
            nova_data_nasc = None

            while True:
                print("\nQual campo deseja alterar:\n")
                print(f"ID: {pessoa.id_pessoa}")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de Nasc.: {pessoa.data_nasc.strftime('%d/%m/%Y')}")
                print("4 - Sair")
                campo = input("Informe o Campo: ").strip()

                limpar()

                match campo:
                    case "1":
                        novo_nome = input("Informe o novo Nome: ").strip().title()
                        print(f"Nome a ser cadastrado: {novo_nome}.")
                    case "2":
                        novo_email = input("Informe o novo E-mail: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if novo_email in [p.email for p in pessoas if p.id_pessoa != pessoa.id_pessoa]:
                            print("E-mail já cadastrado!")
                            novo_email = None
                        else:
                            print(f"E-mail a ser cadastrado: {novo_email}.")
                    case "3":
                        nova_data_nasc = input("Informe a nova Data de Nasc. (dd/mm/aaaa): ").strip()
                        print(f"Data de nascimento a ser cadastrada: {nova_data_nasc}.")
                    case "4":
                        break
                    case _:
                        print("Campo inexistente!")
                        continue

            if novo_nome:
                pessoa.nome = novo_nome
            if novo_email:
                pessoa.email = novo_email
            if nova_data_nasc:
                try:
                    pessoa.data_nasc = datetime.strptime(nova_data_nasc, "%d/%m/%Y").date()
                except ValueError:
                    print("Data inválida, não alterada.")

            session.commit()
            print("Dados alterados com sucesso!")
        else:
            print("Pessoa não encontrada!")
    except Exception as e:
        print(f"Não foi possível alterar! Erro: {e}")
        session.rollback()