import os

restaurantes = []

def exibir_nome_programa():
    print("Sabor Express\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def opcao_invalida():
    print("Opcao invalida\n")
    input("Digite uma tecla para voltar ao menu principal")
    main()

def cadastrar_novo_restaurante():
    os.system("clear")
    print("Cadastro de novos restaurantes\n")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!")
    input("Digite uma tecla para voltar ao menu principal...")
    main()

def listar_restaurantes():
    print(restaurantes)

def escolher_opcao():
    #Por padrao o input espera uma string, por isso é nessesario colocar como int explicitamente... 
    
    # if opcao_escolhida == 1:
    #     print("Cadastrar restaurante")
    # elif opcao_escolhida == 2:
    #     print("Listar restaurante")
    # elif opcao_escolhida == 3:
    #     print("Ativar restaurante")
    # else:
    #     finalizar_app()    
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2: 
                listar_restaurantes()
            case 3:
                print("Ativar restaurante")
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


def finalizar_app():
    os.system("clear")
    print("Finalizando o app\n")

def main():
    os.system("clear")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()    

if __name__ == "__main__":
    main()