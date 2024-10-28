import os

restaurantes = ["restaurente 1", "restau2", "restauranete3", "restaurante 4",]

def exibir_nome_programa():
    print("Sabor Express\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def voltar_ao_menu_principal(): 
    input("\nDigite uma tecla para voltar ao menu")
    main()

def opcao_invalida():
    print("Opcao invalida\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("clear")
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastro de novos restaurantes") 
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurantes.append(nome_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes..")
    for restaurante in restaurantes:
        print(f".{restaurante}")
        
    voltar_ao_menu_principal()

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
    exibir_subtitulo("Finalizando o app")

def main():
    os.system("clear")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()    

if __name__ == "__main__":
    main()