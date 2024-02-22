import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True}, 
                {'nome': 'Cantina', 'categoria': 'Italizano', 'ativo': False}]

def exibir_nome_do_programa():
    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''') # Fsymbols.com


def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterar Estado do Restaurante')
    print('4. Sair')


def finalizar_app():
    exibir_subtitulo('Finalizando o app')


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def opcao_invalida(mensagem):
    print(mensagem)
    voltar_ao_menu_principal()


def exibir_subtitulo(subtitulo):
    os.system('cls') # No Windows
    linha = '*' * (len(subtitulo) + 4)
    print(f'\033[1;034m{linha}\033[0;037m')
    print(f'  \033[1;032m{subtitulo}\033[0;037m  ')
    print(f'\033[1;034m{linha}\033[0;037m')
    print()


def cadastrar_novo_resteurante():
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
    exibir_subtitulo('Listando restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status ')
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f'- {nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()


def alternar_estado_restaurante():
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
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
