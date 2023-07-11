import random
from datetime import datetime

arquivoDeContatos = 'Contatos.txt'

# iniciando o programa
def iniciando_programa():
    print('Atenção programa é um prototipo referente a gestão de contatos | v: 3.0')
    while True:
        iniciar = input('deseja iniciar o programa? [s] ou [n]: ').lower()
        if len(iniciar) > 1:
            print('somente 1 caracter para o funcionamento do programa!')
            continue
        elif iniciar not in ['s', 'n']:
            print('voce só pode escolher entre [s] ou [n] para o funcionar o programa!')
            continue
        elif iniciar == 's':
            print('iniciando o programa!')
            opicao_de_escolha()
            break
        elif iniciar == 'n':
            print('encerrando programa')
            break

# tabela de escolhas
def opicao_de_escolha():
    print(f'\n'
          f'----- Tabela de navegação do programa! -----\n'
          f'[1] - criar ou adicionar contatos.\n'
          f'[2] - pesquisar contatos\n'
          f'[3] - remover contatos\n'
          f'[4] - encerrar programa\n'
          f'----- ******************************** -----\n')
    while True:
        opc = int(input('informar a opção desejada: '))
        if len(str(opc)) > 1:
            print('somente 1 numero!')
            continue
        elif opc == 1:
            criando_contato()
            break
        elif opc == 2:
            pesquisando_contatos()
            break
        elif opc == 3:
            removendo_contatos()
            break
        elif opc == 4:
            print('fim do programa!')
            break
        else:
            print('somente entre 1 a 4!')
            continue

# criando ou adicionando contatos
def criando_contato():
    print('iniciando o programa de adicionamento e criação de contatos!\n')
    criandoContatos = False
    ano_atual = datetime.year
    while not criandoContatos:
        nome = input('informa o nome do contato: ')
        mes = random.randint(1, 12)
        ano = random.randint(1950, int(datetime.today().year))
        telefone = random.randint(10000000, 99999999)
        with open(arquivoDeContatos, 'a') as arq:
            arq.write(f'{nome}, {mes}, {ano}, {telefone}\n')
        while True:
            opc = input('deseja continuar? [s] ou [n]: ').lower()
            if len(opc) > 1:
                print('somente [s] ou [n]')
                continue
            elif opc not in ['s', 'n']:
                print('somente [s] ou [n]')
                continue
            elif opc == 's':
                criandoContatos = False
                print()
                break
            elif opc == 'n':
                criandoContatos = True
                print()
                opicao_de_escolha()
                break

# pesquisando contatos
def pesquisando_contatos():
    with open(arquivoDeContatos, 'r') as arq:
        linhas = arq.readlines()
        # criando um lista para armazenar os nomes.
        lista_de_contatos = [{"nome": linha.strip().split(',')[0].strip(),
                              "mes": linha.strip().split(',')[1].strip(),
                              "ano": linha.strip().split(',')[2].strip(),
                              "telefone": linha.strip().split()[3].strip()} for linha in linhas]

        # verificando se tem linhas armazenadas no arquivo
        if len(linhas) <= 0:
            print('não tem nada para ser lido')
            opicao_de_escolha()
        else:
            # imprimindo todos os contatos e falando quem faz aniversario
            mes = datetime.today().month
            aniversariantes_mes = False

            for indice in range(len(lista_de_contatos)):
                if lista_de_contatos[indice]["mes"] == str(mes):
                    print(f'Este mês é aniversario de : {lista_de_contatos[indice]["nome"]}')
                    aniversariantes_mes = True

            if not aniversariantes_mes:
                print('Ninguém vai fazer aniversário este mês\n')

            # buscar pelos nomes com 1 letra:
            encontrado = False
            while not encontrado:
                buscar_nome = input('Escolha o nome a ser pesquisado: ')
                buscar_nome = buscar_nome.lower()

                for contato in lista_de_contatos:
                    if contato["nome"].lower() == buscar_nome:  # Procurar por nome completo
                        print(f'O contato {contato["nome"]} existe!')
                        encontrado = True
                        opicao_de_escolha()
                        break

                    if contato["nome"].lower().startswith(buscar_nome):  # Procurar por início do nome
                        print(f'---> {contato["nome"]}')

                if not encontrado:
                    print("O nome não foi encontrado na lista.\n")
                    while True:
                        continuar = input('Deseja continuar? [s] ou [n]: ').lower()
                        if continuar == 's':
                            encontrado = False
                            break
                        elif continuar == 'n':
                            opicao_de_escolha()
                            encontrado = True
                            break
                        else:
                            print('Opção inválida! Digite apenas [s] ou [n].')

# removendo contatos
def removendo_contatos():
    removendo = True
    while removendo != False:
        opc = int(input('qual opção de remoção vai escolher?\n'
                    '[1] - remover individualmente.\n'
                    '[2] - limpar o arquivo de contatos.\n'
                    ': '))
        if opc not in [1, 2]:
            print('somente as opções mencionadas!')
            continue
        elif opc == 1:
            # abrindo arquivo para leitura
            with open(arquivoDeContatos, 'r') as arq:
                linhas = arq.readlines()
                # lista dos contatos
                lista_de_contatos = [{"nome": linha.strip().split(',')[0].strip(),
                                      "mes": linha.strip().split(',')[1].strip(),
                                      "ano": linha.strip().split(',')[2].strip(),
                                      "telefone": linha.strip().split()[3].strip()} for linha in linhas]

            # imprimindo a tabela
            for h in lista_de_contatos:
                print(h)
            print()

            # realizar a busca pelo nome
            while True:
                buscar_nome = input('Escolha o nome que deseja excluir da lista: ')
                encontrado = False
                for indice in range(len(lista_de_contatos) - 1, -1, -1):
                    if lista_de_contatos[indice]["nome"] == buscar_nome:
                        lista_de_contatos.pop(indice)
                        encontrado = True

                if not encontrado:
                    print("O nome não foi encontrado na lista.")
                    continue

                print()
                # imprimindo a tabela novamente
                for h in lista_de_contatos:
                    print(h)
                break

            # atualizando o arquivo
            with open(arquivoDeContatos, 'w') as arq:
                for contatos in lista_de_contatos:
                    arq.write(f'{contatos["nome"]}, '
                              f'{contatos["mes"]}, '
                              f'{contatos["ano"]}, '
                              f'{contatos["telefone"]}\n')
            print()
            opicao_de_escolha()

        elif opc == 2:
            with open(arquivoDeContatos, 'w') as arq:
                arq.write(f'')
            removendo = False
            opicao_de_escolha()
        break

iniciando_programa()