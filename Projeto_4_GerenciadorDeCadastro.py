import random
import os

arquivo_geral = 'arquivo_guia.txt'

# setor de exibição
def exibir_menu():
    print('Selecione a opção desejada:')
    print('1 - Criar arquivo de dados')
    print('2 - Adicionar registro ao arquivo')
    print('3 - Remover um registro do arquivo')
    print('4 - Alterar o valor de venda de um registro')
    print('5 - Mostrar os registros de um arquivo')
    print('6 - Sair')
def exibir_menu_remover():
    print('1 - Remover completamente um arquivo.')
    print('2 - Remover todos os dados do arquivo.')
    print('3 - Remover manualmente um vendedor de um arquivo.')

# setor de classes
class Registro:
    def __init__(self, codigo, nome, venda, mes):
        self.codigo = codigo
        self.nome = nome
        self.venda = venda
        self.mes = mes
    def __str__(self):
        return f'codigo, {self.codigo}, vendedor, {self.nome}, valor_venda, {self.venda}, mes, {self.mes}'
class ArquivoDados:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    # Criando o arquivo nomeado
    def criar(self):
        try:
            with open(self.nome_arquivo, 'w', encoding='utf-8'):
                pass
        except FileNotFoundError:
            print('Arquivo não encontrado')

    # Adicionando dados ao arquivo escolhido.
    def fuc_2_adicionar_registro(self, registro):
        try:
            with open(self.nome_arquivo, 'a', encoding='utf-8') as arquivo:
                arquivo.write(str(registro) + '\n')
        except FileNotFoundError:
            print('arquivo nao encontrado')

# função da opção (2°)
def fuc_2_obter_dados():
    lista_de_dados = []
    while True:
        codigo = random.randint(10000, 99999)
        nome = input('Digite o nome do vendedor: ')
        venda = random.randint(0, 99999)
        mes = random.randint(1, 12)
        lista_de_dados.append({"codigo": codigo, "nome": nome, "venda": venda, "mes": mes})

        opc = input('Deseja continuar [s] ou [n]: ').lower()
        while opc not in ['s', 'n']:
            print('Somente [s] ou [n]')
            opc = input('Deseja continuar [s] ou [n]: ').lower()
        if opc == 'n':
            break
    return lista_de_dados

# função da opção (3°)
def fuc_3_tabela(arquivo):
    exibir_menu_remover()
    opc = input()
    if opc == '1':
        fuc_3_remover_arquivo(arquivo)
    elif opc == '2':
        arquivo_lido = ler_arquivo_escolhido(arquivo)
        if not arquivo_lido:
            print("Não há dados para serem lidos.")
        else:
            fuc_3_remover_dados_arquivo(arquivo)
    elif opc == '3':
        arquivo_lido = ler_arquivo_escolhido(arquivo)
        if not arquivo_lido:
            print("Não há dados para serem lidos.")
        else:
            fuc_3_remover_vendedor(arquivo_lido, arquivo)
    else:
        print('Opção inválida. Tente novamente.')
def fuc_3_remover_arquivo(nome_arquivo):
    try:
        # Remover o nome do arquivo da lista (se existir)
        lista_de_nomes = [dado for dado in ler_arquivo_guia() if dado != nome_arquivo]
        with open(arquivo_geral, 'w', encoding='utf-8') as arquivo:
            for h in lista_de_nomes:
                arquivo.writelines(h + "\n")

        # Remover o arquivo que foi criado
        os.remove(nome_arquivo)
        print(f"O arquivo '{nome_arquivo}' foi removido com sucesso.")
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except PermissionError:
        print(f"Não foi possível remover o arquivo '{nome_arquivo}'. Verifique as permissões.")
def fuc_3_remover_dados_arquivo(arquivo):
    try:
        with open(arquivo_geral, 'w'):
            pass
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    print('Todos os dados do arquivo foram apagados!')
def fuc_3_remover_vendedor(arquivo_lido, arquivo):
    linhas_manter = []

    nomes = [linha.strip().split(',')[3] for linha in ler_arquivo_escolhido(arquivo)]
    [print(f'----> [ {nome} ]') for nome in nomes]

    nome_exclusao = input("Digite o nome do vendedor que deseja excluir: ")
    for linha in arquivo_lido:
        if nome_exclusao not in linha:
            linhas_manter.append(linha)

    with open(arquivo, 'w') as arq:
        for linha in linhas_manter:
            arq.write(linha)
    print("Linha com o nome 'caio' foi excluída do arquivo.")

# função da opção (4°)
def fuc_4_alterar(arquivo):
    arquivo_lido = ler_arquivo_escolhido(arquivo)
    linhas_manter = []

    nomes = [linha.strip().split(',')[3] for linha in ler_arquivo_escolhido(arquivo)]
    [print(f'----> [ {nome} ]') for nome in nomes]

    nome = input('qual vendedor deseja alterar o valor de sua venda: ')
    for linha in arquivo_lido:
        codigo = linha.strip().split()[1]
        vendedor = linha.strip().split()[3]
        valor_venda = linha.strip().split()[5]
        mes = linha.strip().split()[7]

        if nome in linha:
            novo_valor = int(input('informa novo valor da venda: '))
            linhas_manter.append({"codigo": codigo, "vendedor": vendedor, "valor_venda": novo_valor, "mes": mes})
        else:
            linhas_manter.append({"codigo": codigo, "vendedor": vendedor, "valor_venda": valor_venda, "mes": mes})

    with open(arquivo, 'w') as arq:
        for h in linhas_manter:
            arq.write(f'codigo, {h["codigo"]}, '
                      f'vendedor, {h["vendedor"]}, '
                      f'valor_venda, {h["valor_venda"]}, '
                      f'mes, {h["mes"]}\n')

# função da opção (5°)
def fuc_5_imprimir_registro(arquivo):
    try:
        if not ler_arquivo_escolhido(arquivo):
            print('O arquivo não contém dados nele!')
        else:
            linha = ler_arquivo_escolhido(arquivo)
            print(f'----- tabela de registro do arquivo: {arquivo} -----')
            [print(f'{arquivo.strip()}') for arquivo in linha]
    except FileNotFoundError:
        print('Arquivo não encontrado')

# setor de tratamento essenciais.
def ler_arquivo_escolhido(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as arq:
            linha = arq.readlines()
            return linha
    except FileNotFoundError:
        return []
def escrever_arquivo_guia(nome_arquivo):
    with open(arquivo_geral, 'a', encoding='utf-8') as arquivo:
        arquivo.write(nome_arquivo + "\n")
def ler_arquivo_guia():
    try:
        with open(arquivo_geral, 'r', encoding='utf-8') as arquivo:
            return [linha.strip() for linha in arquivo.readlines()]
    except FileNotFoundError:
        return []

def main():
    while True:
        exibir_menu()
        opc = input('Opção: ')

        if opc == '1':
            nome_arquivo = input('Informe o nome do arquivo a ser criado: ')
            escrever_arquivo_guia(nome_arquivo)
            Arquivo_Dados = ArquivoDados(nome_arquivo)
            Arquivo_Dados.criar()

        elif opc == '2':
            if not ler_arquivo_guia():
                print('Não tem nomes de arquivos para serem adicionados, crie um por favor!')
            else:
                print('---------- arquivos disponiveis ----------')
                [print(f'{i} ----> {arquivo}') for i, arquivo in enumerate(ler_arquivo_guia())]
                arquivo = input('Digite o nome do arquivo: ')
                if arquivo in ler_arquivo_guia():
                    print('Arquivo encontrado')
                    lista_de_dados = fuc_2_obter_dados()
                    for dados in lista_de_dados:
                        registro = Registro(dados["codigo"], dados["nome"], dados["venda"], dados["mes"])
                        arquivo_dados = ArquivoDados(arquivo)
                        arquivo_dados.fuc_2_adicionar_registro(registro)
                else:
                    print('Arquivo não encontrado no guia de pesquisa')

        elif opc == '3':
            if not ler_arquivo_guia():  # isso se nao tiver nada
                print('Não tem nomes de arquivos para serem adicionados, crie um por favor!')
            else:
                print('---------- arquivos disponiveis ----------')
                [print(f'{i} ----> {arquivo}') for i, arquivo in enumerate(ler_arquivo_guia())]
                arquivo = input('Digite o nome do arquivo: ')
                if arquivo not in ler_arquivo_guia(): # isso se nao tiver nada
                    print('Nome não encontrado no arquivo geral. Impossível de excluir algum registro.')
                else:
                    fuc_3_tabela(arquivo)

        elif opc == '4':
            if not ler_arquivo_guia():  # isso se nao tiver nada
                print('não tem arquivos a serem alterados!')
            else:
                print('---------- arquivos disponiveis ----------')
                [print(f'{i} ----> {arquivo}') for i, arquivo in enumerate(ler_arquivo_guia())]
                arquivo = input('Digite o nome do arquivo: ')
                if arquivo not in ler_arquivo_guia():
                    print('esse nome não esta armazenado no arquivo geral, portanto não tem como altera-lo!')
                else:
                    fuc_4_alterar(arquivo)

        elif opc == '5':
            if not ler_arquivo_guia():  # isso se nao tiver nada
                print('não tem arquivos a serem alterados!')
            else:
                [print(f'{i} ----> {arquivo}') for i, arquivo in enumerate(ler_arquivo_guia())]
                arquivo = input('nome do arquivo: ')
                if arquivo not in ler_arquivo_guia(): # isso se nao tiver nada
                    print('Nome não encontrado no arquivo geral. Impossível imprimir o registro.')
                else:
                    fuc_5_imprimir_registro(arquivo)

        elif opc == '6':
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()
