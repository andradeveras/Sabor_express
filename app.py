import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Ella Pizzaria','categoria':'Italiana','ativo':True},
                {'nome':'Churrascaria','categoria':'Brasileira','ativo':False}
]

def exibir_nome_programa():
    print("Sabor Express\n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar status do restaurante")
    print("4. Sair\n")

def voltar_ao_menu_principal(): 
    input("\nDigite uma tecla para voltar ao menu")
    main()

def opcao_invalida():
    print("Opcao invalida\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("clear")
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """Essa função é restonsavel por cadastar um novo restaurante
    
    Inputs:
    - Nome do restaurante 
    - Categoria

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    
    """
    exibir_subtitulo("Cadastro de novos restaurantes") 
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo("Listando restaurantes")

    print(f"{"Nome do restaurante".ljust(21)} | {"Categoria".ljust(20)} | {"Status".ljust(20)}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante["ativo"] else 'Desativado'
        print(f".{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo.ljust(20)}" )
        
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo("Alterando estado do restautante...")
    nome_restaurante = input("Digite o nome do restaurante que deseja alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado') 

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
                alternar_estado_restaurante()
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