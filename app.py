'''Importação para poder limpar a tela'''
import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italizano', 'ativo': False}]

def exibir_nome_do_programa():
    '''
    Apresenta o nome estilizado do programa na tela inicial
    '''
    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''') # Fsymbols.com


def exibir_opcoes():
    '''
    Mostrar todas as opções que poderá ser selecionado no menu inicial
    '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Estado do Restaurante')
    print('4. Sair')


def finalizar_app():
    '''
    Mostra a mensagem de finalização do programa
    '''
    exibir_subtitulo('Finalizando o app')


def voltar_ao_menu_principal():
    '''
    Solicita uma tecla para retornar ao menu inicial e redireciona para o mesmo

    Output:
        Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def opcao_invalida(mensagem):
    '''
    Mostra na tela uma mensagem de erro de acordo com a chamada dessa função

    Output:
        Retorna ao menu principal
    '''
    print(mensagem)
    voltar_ao_menu_principal()


def exibir_subtitulo(subtitulo):
    '''Essa Função tem a resposabilidade de mostrar os subtítulos do programa.

    Params: 
        subtitulo (str): texto que deverá ser mostrado na tela
    '''
    os.system('cls') # No Windows
    linha = '*' * (len(subtitulo) + 4)
    print(f'\033[1;034m{linha}\033[0;037m')
    print(f'  \033[1;032m{subtitulo}\033[0;037m  ')
    print(f'\033[1;034m{linha}\033[0;037m')
    print()


def cadastrar_novo_resteurante():
    '''
    Cadastra um novo restaurante na lista de restaurantes.
    
    Inputs:
        nome_do_restaurante (str): O nome do restaurantte que será adicionado.
        categoria (str): A categoria do restaurante que será adicionado.
    
    Output:
        Adiciona o novo restaurante na lista de restaurantes.
    '''
    try:
        exibir_subtitulo('Cadastro de novos resteurantes')
        nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ') # Alt-z para visualizar tudo
        if not nome_do_restaurante:
            raise ValueError('Nome do restaurante não foi inserido')

        categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
        if not categoria:
            raise ValueError('Categoria não foi inserida')

        dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

        restaurantes.append(dados_do_restaurante)
        print(f'O restaurante {nome_do_restaurante} foi adicionado com sucesso!')
        voltar_ao_menu_principal()

    except Exception as ve:
        opcao_invalida(ve)


def listar_restaurantes():
    '''
    Mosta na tela todos os restaurantes cadastrados.

    Output:
        Exibe a lista de restaurantes na tela
    '''
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status ')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''
    Altera o estado de um restaurante cadastrado.
    
    Inputs:
        nome_retaurante (str): nome do restaurante que terá seu estado alterado
        
    Output:
        Alteração do estado do restaurante selecionado'''

    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''
    Requere que uma opção seja escolhida entre as opções da tela.
    
    Inputs:
        opcao_escolhida (int): Opção que será selecionada.
        
    Output:
        Executa a operação escolhida.
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1: cadastrar_novo_resteurante()
            case 2: listar_restaurantes()
            case 3: alternar_estado_restaurante()
            case 4: finalizar_app()
            case _:opcao_invalida("Opcao inválida!\n")

    except Exception:
        opcao_invalida("Opcao inválida! \n")


def main():
    '''
    Inicia o fluxo do programa principal
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
