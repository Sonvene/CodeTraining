# Constantes e configurações
from random import randint as rd
ARQ_GERAL = "EX26_ARQ_GERAL.bin"
OPCAO_CRIAR_ARQUIVO = 1
OPCAO_PESQUISAR_ARQUIVO = 2
OPCAO_PESQUISAR_CLASSE_DE_ALUNOS = 3
OPCAO_ENCERRAR_PROGRAMA = 4

def exibir_menu():
    print("[1] - Criar arquivos de classes.")
    print("[2] - Pesquisar ou editar arquivos de classes.")
    print("[3] - Pesquisar classes de alunos.")
    print("[4] - Encerrar programa.")


def exibir_menu_2():
    print("[1] - Adicionar inscrições de alunos ao arquivo?.")
    print("[2] - Remover o arquivo?.")


def exibir_menu_3():
    print("[1] - Adicionar inscrições de alunos ao arquivo?.")
    print("[2] - Remover inscrições de alunos ao arquivo?.")


def exibir_sub_menu_pesquisa():
    print("[1] - Adicionar inscrições de alunos ao arquivo?.")
    print("[2] - Remover inscrições de alunos ao arquivo?.")


def iniciar_programa():
    while True:
        try:
            exibir_menu()
            opc = int(input("Opção: "))

            if opc == OPCAO_CRIAR_ARQUIVO:
                print("Iniciando programa [1]...\n")
                criando_arquivo_classe()

            elif opc == OPCAO_PESQUISAR_ARQUIVO:
                print("Iniciando programa [2]...")
                pesquisar_arquivo_classe()

            elif opc == OPCAO_PESQUISAR_CLASSE_DE_ALUNOS:
                print("Iniciando programa [3]...")
                pesquisar_classes()

            elif opc == OPCAO_ENCERRAR_PROGRAMA:
                print("Encerrando programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Opção inválida. Tente novamente.")


def nomeando_arquivo_classes(): # não faz parte de um todo, pois ele é chamado dentro de um função
    criando = True
    while criando:
        try:
            nome_arquivo_classe = input('Informe o nome do arquivo: ') + ".bin"
            return nome_arquivo_classe

        except ValueError:
            print("Opção inválida. Tente novamente.")
            return None


def criando_arquivo_classe(): # ele chama a função para nomear e depois armazena-o em uma lista
    print('iniciando o programa de criação e edição de arquivos de classes!')
    listaArquivosCriados = []

    while True:
        arquivo = nomeando_arquivo_classes()
        if arquivo:
            listaArquivosCriados.append(arquivo)

        while True:
            opc = input('Deseja continuar? [s] ou [n]: ').lower()
            if opc not in ['s', 'n']:
                print('Somente entre [s] ou [n]!')
            else:
                break

        if opc == 'n':
            break

    print('\n----- arquivos criados -----')
    for h in listaArquivosCriados:
        print(f'--> {h}')
    print()

    with open(ARQ_GERAL, 'a') as arquivo_geral:
        for h in listaArquivosCriados:
            arquivo_geral.write(f'{h}\n')


# realiza uma pesquisa para saber quais arquivos de classes possam ser usados.
def pesquisar_arquivo_classe():
    # crio outra função para ler o arquivo geral para depois imprimiar todas as opções criadas de arquivos bin.
    lista_de_arquivos = lendo_arquivo_geral()

    # verificando se existe um arquivo criado, caso contrario ele retorna a tabela de opções.
    if len(lista_de_arquivos) <= 0:
        print('\033[31m\nNão tem arquivo para ser pesquisado!\n\033[0m')
    else:
        while True:
            try:
                # imprimindo os arquivos criados, caso tenha.
                print('\n--------- Tabela dos Arquivos ---------')
                for i, arquivo in enumerate(lista_de_arquivos):
                    print(f'[{i}]. --> {arquivo}')

                sair = input('deseja alterar algum desses arquivos? [s] ou [n]: ').lower()
                if sair not in ['s', 'n']:
                    print('opção invalida, tente novamente!\n')
                    continue
                else:
                    if sair == 's':
                        while True:
                            try:
                                opc = int(input('Escolha um dos arquivos: '))
                                if opc not in range(len(lista_de_arquivos)):
                                    print('Este arquivo não está na tabela.')
                                    continue
                                else:
                                    print(f'\n -----> Arquivo escolhido {lista_de_arquivos[opc]} <-----')

                                    while True:
                                        opc1 = input('\nDeseja modifica-lo? [s] ou [n]: ').lower()
                                        if opc1 not in ['s', 'n']:
                                            print('Somente entre [s] ou [n]!')
                                        else:
                                            break

                                if opc1 == 's':  # quero modificar algo
                                    exibir_menu_2()
                                    opc2 = int(input('opção: '))

                                    if opc2 == 1:
                                        lista_de_dados_alunos = []
                                        while True:
                                            arquivo_dados_de_alunos = adicionar_inscricoes_alunos()
                                            if arquivo_dados_de_alunos:
                                                lista_de_dados_alunos.append(arquivo_dados_de_alunos)

                                            while True:
                                                opc_alunos = input('Deseja continuar? [s] ou [n]: ').lower()
                                                if opc_alunos not in ['s', 'n']:
                                                    print('Somente entre [s] ou [n]!')
                                                else:
                                                    break
                                            if opc_alunos == 'n':
                                                break

                                        with open(lista_de_arquivos[opc], 'a') as arquivo:
                                            """
                                            criei o arquivo que armazena os dados de cada aluno;
                                            matricula, nome, sobrenome, e data de nascimento.
                                            """
                                            for h in lista_de_dados_alunos:
                                                arquivo.write(f'{h["matricula"]},'
                                                              f'{h["aluno"]},'
                                                              f'{h["sobrenome"]},'
                                                              f'{h["nascimento"]}\n')
                                        break

                                    elif opc2 == 2:
                                        try:
                                            indice = lista_de_arquivos.index(lista_de_arquivos[opc])
                                            lista_de_arquivos.pop(indice)

                                        except ValueError:
                                            print("O nome não foi encontrado na lista.")
                                            continue

                                        print('\n---------- tabela atualizada ----------')
                                        for h in lista_de_arquivos:
                                            print(h)
                                        print()

                                        # atualizando o arquivo removido
                                        with open(ARQ_GERAL, 'w') as arquivo:
                                            for h in lista_de_arquivos:
                                                arquivo.write(f'{h}\n')
                                            break

                                if opc1 == 'n':  # sair dos loops pois, n quero fazer nada
                                    break

                            except IndexError:
                                print('valor não encontrado')

                    elif sair == 'n':
                        print('fim do programa!\n')
                        break

            except ValueError:
                print('valor incorreto')


# realiza uma pesquisa dos nomes dos arquivos de classes, vendo quais sao operantes e quais não são.
def pesquisar_classes():
    lista_de_arquivos = lendo_arquivo_geral()

    if len(lista_de_arquivos) <= 0:
        print('\033[31m\nNão tem arquivo para ser pesquisado!\n\033[0m')
        print('\033[31mLogo não tem dados de alunos!\n\033[0m')
    else:
        pesquisando = True
        while pesquisando:
            try:
                # imprimindo os arquivos criados, caso tenha.
                print('\n--------- Tabela dos Arquivos existentes ---------')
                for i, arquivo in enumerate(lista_de_arquivos):
                    print(f'[{i}]. --> {arquivo}')
                print()

                opc = int(input('Escolha um dos arquivos para acessar: '))

                if opc not in range(len(lista_de_arquivos)):
                    print('\033[31m\nO valor digitado não corresponde a quantidade fornecida pelo sistema!\033[0m')
                    continue

                arquivo_novo = lista_de_arquivos[opc] # dado do nome do arquivo
                arquivo_lido = acessando_arquivo_lido(arquivo_novo) # dado bruto retirado pelo nome

                if arquivo_lido is None: # verifica se ele existe ou não.
                    print('\033[31m\nO arquivo não existe!\033[0m')
                    while True:
                        sair = input('\nDeseja continuar com a pesquisa? [s] ou [n]: ').lower()

                        if sair == 's':
                            pesquisando = True
                            break

                        elif sair == 'n':
                            print('Fim do programa de pesquisa!\n')
                            pesquisando = False
                            break

                elif len(arquivo_lido) <= 0: # verifica se etem dados ou não.
                    print('\033[31m\nO arquivo existe, mas não possui dados nele!\033[0m')
                    while True:
                        sair = input('\nDeseja continuar com a pesquisa? [s] ou [n]: ').lower()

                        if sair == 's':
                            pesquisando = True
                            break

                        elif sair == 'n':
                            print('Fim do programa de pesquisa!\n')
                            pesquisando = False
                            break

                else:
                    print(f'\n--------- Tabela dos alunos da classe ({arquivo_novo}) ---------')
                    for h in arquivo_lido: # imprime a tabela com os dados dos alunos dentro da classe.
                        print(f'Matricula: {h.split(",")[0]}, '
                              f'Nome: {h.split(",")[1]}, '
                              f'Sobrenome: {h.split(",")[2]}, '
                              f'Data de Nascimento: {h.split(",")[3]}')

                    # perguntando se quer alterar ou adicionar ao arquivo atual:
                    while True:
                        try:
                            opc = input('\nDeseja alterar ou adicionar esse arquivo? [s] ou [n]: ').lower()

                            if opc == 's':
                                criando_contatos_pelo_arquivo_acessado(arquivo_novo)
                                break

                            elif opc == 'n':
                                pesquisando = False
                                break

                        except ValueError:
                            print('valor incorreto')

                    # pedindo para sair ou continar com a pesquisa e alteração: se sair acaba o programa de pesquisa.
                    while True:
                        try:
                            sair = input('\nDeseja continuar com a pesquisa? [s] ou [n]: ').lower()

                            if sair == 's':
                                pesquisar_classes()
                                break
                            elif sair == 'n':
                                print('Fim do programa de pesquisa!\n')
                                pesquisando = False
                                break

                        except ValueError:
                            print('valor incorreto')

                    break # só para garantir que não repeta o processo da pergunta de acesso.

            except FileNotFoundError:
                print('arquivo não encontrado')


def criando_contatos_pelo_arquivo_acessado(arquivo_novo):
    while True:
        try:
            exibir_menu_3()
            opc = int(input('opção: '))

            if opc == 1:
                adicionar_arquivo_classe(arquivo_novo)
                break

            elif opc == 2:
                remover_Arquivo_classe(arquivo_novo)
                break

        except IndexError:
            print('valor incorreto!')


def adicionar_arquivo_classe(arquivo_novo): # acessa o arquivo escolhido pela pesquisa
    # criando novas inscrições
    lista_de_novos_dados = []
    while True:
        arquivo_dados_de_alunos = adicionar_inscricoes_alunos()
        if arquivo_dados_de_alunos:
            lista_de_novos_dados.append(arquivo_dados_de_alunos)

        while True:
            opc_alunos = input('Deseja continuar? [s] ou [n]: ').lower()
            if opc_alunos not in ['s', 'n']:
                print('Somente entre [s] ou [n]!')
            else:
                break
        if opc_alunos == 'n':
            break

    # abrindo o arquivo escolhido
    with open(arquivo_novo, 'a') as arquivo:
        for h in lista_de_novos_dados:
            arquivo.write(f'{h["matricula"]},'
                          f'{h["aluno"]},'
                          f'{h["sobrenome"]},'
                          f'{h["nascimento"]}\n')


def remover_Arquivo_classe(arquivo_novo):
    print('[1] - remover individualmente.')
    print('[2] - remover por completo.')
    while True:
        try:
            opc = int(input('Opção: '))

            if opc == 1:
                # acessando arquivo
                with open(arquivo_novo, 'r') as arquivo:
                    linhas = arquivo.readlines()

                    removendo = True
                    while removendo:
                        # Imprimir as linhas numeradas para referência
                        for i, linha in enumerate(linhas):
                            print(f"[{i + 1}]: {linha.strip()}")

                        # Solicitar ao usuário o número da linha a ser removida
                        linha_remover = int(input("Digite o número da linha que deseja remover: "))

                        # Verificar se o número da linha é válido
                        if linha_remover < 1 or linha_remover > len(linhas):
                            print("Número de linha inválido.\n")
                            continue
                        else:
                            # Remover a linha da lista
                            linha_remover -= 1  # Ajustar o número da linha para o índice da lista
                            linhas.pop(linha_remover)

                            print("Linha removida com sucesso.")

                        while True:
                            sair = input('Deseja continuar removendo linhas? [s] ou [n]: ').lower()

                            if sair not in ['s', 'n']:
                                print('Digite somente [s] ou [n]!')
                                continue

                            if sair == 's':
                                removendo = True
                                break

                            elif sair == 'n':
                                removendo = False
                                break

                    # Atualizar o arquivo com as linhas restantes
                    with open(arquivo_novo, 'w') as arquivo:
                        arquivo.writelines(linhas)

            elif opc == 2:
                print('remoção total completa')
                with open(arquivo_novo, 'w') as arquivo:
                    arquivo.write('')

            break
        except ValueError:
            print('Digite somente um número inteiro para a opção.')
            continue
        except IndexError:
            print('Digite somente [1] para a opção de remover linhas.')
            continue

# o mais importante
def lendo_arquivo_geral(): # acessando o arquivo geral, aqual guarda nomes de arquivos de classes
    try:
        with open(ARQ_GERAL, 'rb') as arquivo:
            linhas_byte = (arquivo.readlines())
            linhas = [linha.decode('utf-8', errors='ignore').strip() for linha in linhas_byte]
        return linhas

    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return None


def adicionar_inscricoes_alunos():
    dados_alunos = None
    while True:
        try:
            matricula = rd(10000, 99999)
            aluno = input('Informe o nome do aluno: ')
            sobrenome = input(f'informar o sobrenome do(a) {aluno}: ')
            nascimento = rd(2000, 2023)
            dados_alunos = dict({"matricula":matricula,
                                 "aluno":aluno,
                                 "sobrenome": sobrenome,
                                 "nascimento": nascimento})
            break
        except ValueError:
            print("Opção inválida. Tente novamente.")
    return dados_alunos


def acessando_arquivo_lido(arquivo_novo):
    # acessando o arquivo escolhido
    try:
        with open(arquivo_novo, 'rb') as arquivo_lido:
            linhas_byte = arquivo_lido.readlines()
            linhas = [linha.decode('utf-8', errors='ignore').strip() for linha in linhas_byte]

    except FileNotFoundError:
        return None
    return linhas

# Execução principal
if __name__ == "__main__":
    iniciar_programa()
