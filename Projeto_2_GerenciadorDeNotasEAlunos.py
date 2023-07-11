import random
class GerenciadorDeNotasEAlunos:
    ARQUIVO_GERAL = "ARQ_GERAL_EX27.bin"
    def ler_arquivo_geral(self):
        try:
            with open(self.ARQUIVO_GERAL, 'r', encoding='utf-8') as arquivo:
                return arquivo.read().splitlines()
        except FileNotFoundError:
            print("Arquivo não encontrado!")
            return []
    def analise(self):
        if not self.ler_arquivo_geral():
            print('\033[31mO arquivo principal não contém nomes de arquivos (classes) para serem utilizados.\033[0m')
            print('\033[31mPor favor, crie nomes de arquivos que serão usados posteriormente.\033[0m')
            return None
        else:
            return True
    def armazenar_nomes_arquivos(self, arquivos):
        with open(self.ARQUIVO_GERAL, 'w') as arquivo:
            for nomes in arquivos:
                arquivo.write(f'{nomes}\n')
    def __init__(self):
        self.gabarito = [random.choice(['a', 'b', 'c', 'd', 'e']) for _ in range(10)]

    # - SETOR DE EXIBIÇÃO -
    @staticmethod
    def exibir_menu_principal():
        print("[1] - Opção: Criar Arquivos de Classes.")
        print("[2] - Opção: Criar Cadastros de Alunos.")
        print("[3] - Opção: Pesquisar.")
        print("[4] - Opção: Encerrar programa.")
    def exibir_opcoes_cadastro(self):
        print("[1] - Opção: Criar Cadastro manualmente.")
        print("[2] - Opção: Criar Cadastro randomicamente.")
    def exibir_menu_pesquisando(self):
        print("[1] - Opção: Pesquisar Classes de alunos.")
        print("[2] - Opção: Pesquisar Alunos em Classes.")
        print("[3] - Opção: Pesquisar Alunos Aprovados.")
        print("[4] - Opção: Pesquisar Alunos Reprovados.")
        print("[5] - Opção: Sair do programa de pesquisa.")
    def exibir_alunos_aprovados(self, alunos_aprovados, classe):
        if len(alunos_aprovados) > 0:
            print(f'----- Tabela dos aprovados {classe} -----')
            for h in alunos_aprovados:
                print(f'{h["nome"]}: {h["status"]}')
            print()
        else:
            print("\033[31m Nenhum aluno foi aprovado.\n \033[0m")
    def exibir_alunos_reprovados(self, alunos_reprovados, classe):
        if len(alunos_reprovados) > 0:
            print(f'----- Tabela dos aprovados {classe} -----')
            for h in alunos_reprovados:
                print(f'{h["nome"]}: {h["status"]}')
            print()
        else:
            print("\033[31m Nenhum aluno foi aprovado.\n \033[0m")
    @staticmethod
    def exibir_dados_alunos(alunos):
        qtd_aprovados = 0
        print('-' * 50 + ' Tabela dos alunos ' + '-' * 50)
        for aluno in alunos:
            status = "\033[32mAPROVADO\033[0m" if aluno['nota'] >= 5 else "\033[31mREPROVADO!\033[0m"
            print(f"Matrícula: {aluno['matricula']}, "
                  f"Nome: {aluno['nome']}, "
                  f"Prova: {aluno['prova']}, "
                  f"Nota: {aluno['nota']}/{len(aluno['prova'])}, "
                  f"Status: {status}")
            if aluno['nota'] >= 5:
                qtd_aprovados += 1
        print(f"A quantidade de aprovados é de: ---> {qtd_aprovados} <---\n")

    # SETOR 1° - criador de nomes de arquivos (classes de alunos)
    def Opcao_1_criando_nomes_de_arquivos(self):
        nomes_arquivos = []
        while True:
            nome_arquivo = input('Informe o nome do arquivo a ser criado (sem extensão): ')
            nomes_arquivos.append(f"{nome_arquivo}.bin")
            opcao = input('Deseja continuar? [s] ou [n]: ').lower()
            while opcao not in ['s', 'n']:
                print('Opção inválida. Digite "s" para continuar ou "n" para sair.')
                opcao = input('Deseja continuar? [s] ou [n]: ').lower()
            if opcao == 'n':
                break
        return nomes_arquivos

    # SETOR 2° - criando cadastro de alunos com os nomes criados pelo SETOR 1°
    def Opcao_2_criando_cadastros_de_alunos(self):
        while True:
            try:
                self.exibir_opcoes_cadastro()
                opcao = int(input(f'Opção: '))
                if opcao not in [1, 2]:
                    print(
                        '\033[31mSomente entre "1" para Cad.manualmente ou "2" para Cad.randomicamente.\033[0m')
                    continue
                if opcao == 1:
                    alunos = self.Opcao_2_criando_cadastros_manualmente()
                    return alunos
                elif opcao == 2:
                    alunos = self.Opcao_2_criando_cadastros_randomicamente()
                    return alunos
            except ValueError:
                print('\033[31m Opção inválida. Digite um número válido.\033[0m')
    def Opcao_2_criando_cadastros_manualmente(self):
        opc_mult_Escolha = ['a', 'b', 'c', 'd', 'e']
        alunos = []
        i = 0
        while True:
            matricula = random.randint(10000, 99999)
            nome = input(f'Informe o nome do ({i+1}°) Aluno: ')
            prova = [random.choice(opc_mult_Escolha) for _ in range(10)]
            nota = sum([1 for i in range(len(self.gabarito)) if prova[i].lower() == self.gabarito[i].lower()])
            alunos.append({"matricula": matricula, "nome": nome, "prova": prova, "nota": nota})
            i += 1
            opcao = input('Deseja continuar? [s] ou [n]: ').lower()
            while opcao not in ['s', 'n']:
                print('Opção inválida. Digite "s" para continuar ou "n" para sair.')
                opcao = input('Deseja continuar? [s] ou [n]: ').lower()
            if opcao == 'n':
                break
        return alunos
    def Opcao_2_criando_cadastros_randomicamente(self):
        alunos = []
        opc_mult_Escolha = ('a', 'b', 'c', 'd', 'e')
        nomes = ["Alice", "Bob", "Carol", "David", "Eva", "Frank", "Grace", "Henry", "Ivy", "Jack",
            "Kelly", "Liam", "Mia", "Nathan", "Olivia", "Peter", "Quinn", "Rachel", "Samuel", "Tara",
            "Adam", "Beth", "Chloe", "Daniel", "Emily", "Fiona", "George", "Hannah", "Isaac", "Jessica",
            "Kevin", "Laura", "Michael", "Nora", "Oscar", "Penelope", "Quentin", "Rebecca", "Simon", "Tiffany",
            "Victor", "Wendy", "Xavier", "Yvonne", "Zane", "Amy", "Benjamin", "Catherine", "Dylan", "Elizabeth",
            "Frederick", "Gina", "Harry", "Iris", "Jason", "Katherine", "Landon", "Megan", "Noah", "Olivia",
            "Patrick", "Rachel", "Sebastian", "Stephanie", "Tristan", "Victoria", "Wyatt", "Zoe", "Andrew", "Brianna",
            "Christopher", "Danielle", "Elijah", "Faith", "Gabriel", "Hailey", "Isaiah", "Jasmine", "Jacob", "Kennedy",
            "Liam", "Lily", "Matthew", "Madison", "Nathan", "Natalie", "Oliver", "Sophia", "Ryan", "Samantha",
            'João', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Mariana', 'Carlos', 'Julia', 'Rafael', 'Fernanda']
        while True:
            num_alunos = int(input('Quantos alunos deseja ter na turma (entre 0 e 100)?: '))
            if num_alunos < 0 or num_alunos > 100:
                print('A capacidade máxima é de 100 alunos. Por favor, informe um valor entre 0 e 100.')
                continue
            else:
                for i in range(num_alunos):
                    matricula = random.randint(10000, 99999)
                    nome = nomes[i]
                    prova = [random.choice(opc_mult_Escolha) for _ in range(10)]
                    nota = sum([1 for i in range(len(self.gabarito)) if prova[i].lower() == self.gabarito[i].lower()])
                    alunos.append({"matricula": matricula, "nome": nome, "prova": prova, "nota": nota})
                break
        return alunos
    def Opcao_2_adicionando_dados_arquivo(self, alunos):
        arquivo_lido = self.ler_arquivo_geral()
        [print(f'[{i}°] ---> {arquivo}') for i, arquivo in enumerate(arquivo_lido)]
        while True:
            opcao = int(input('Escolha um dos arquivos: '))
            if opcao in range(len(arquivo_lido)):
                print(f'\nO arquivo escolhido foi: --> {arquivo_lido[opcao]} <--\n')
                # criando arquivo de acordo com o nome fornecido pelo usuario.
                with open(arquivo_lido[opcao], 'wb') as arquivo:
                    for aluno in alunos:
                        status = "APROVADO" if aluno['nota'] >= 5 else "REPROVADO"
                        linha = f"Matrícula: {aluno['matricula']}, " \
                                f"Nome: {aluno['nome']}, " \
                                f"Prova: {aluno['prova']}, " \
                                f"Nota: {aluno['nota']}/{len(aluno['prova'])}, " \
                                f"Status: {status}\n"
                        arquivo.write(linha.encode('utf-8'))
                break
            else:
                print(f'Opção inválida. somente entre [{1}] ao [{len(arquivo_lido)}] dos arquivos.')
                continue

    # SETOR 3° - pesquisando cadastros e arquivos.
    def Opcao_3_pesquisando(self):
        while True:
            self.exibir_menu_pesquisando()
            try:
                opcao = int(input('Opção: '))
                if opcao == 1:
                    self.Opcao_3_Mostrando_classes()
                elif opcao == 2:
                    self.Opcao_3_Mostrando_alunos_de_cada_classe()
                elif opcao == 3:
                    alunos_aprovados, classe = self.Opcao_3_Mostrando_alunos_aprovados()
                    self.exibir_alunos_aprovados(alunos_aprovados, classe)
                elif opcao == 4:
                    alunos_reprovados, classe = self.Opcao_4_Mostrando_alunos_reprovados()
                    self.exibir_alunos_reprovados(alunos_reprovados, classe)
                elif opcao == 5:
                    break
            except ValueError:
                print('Opção inválida. Digite um número de opção válido.')
                continue

    def Opcao_3_Mostrando_classes(self):
        print('--------- Lista de arquivos (classes) ---------')
        [print(f'[{i}°] ---> {arquivo}') for i, arquivo in enumerate(self.ler_arquivo_geral())]
        print()
    def Opcao_3_Mostrando_alunos_de_cada_classe(self):
        classes = self.ler_arquivo_geral()
        [print(f'[{i}°] ---> {arquivo}') for i, arquivo in enumerate(classes)]
        while True:
            opcao = int(input('Escolha um dos arquivos: '))
            if opcao in range(len(classes)):
                print(f'\nA classe escolhida foi: --> {classes[opcao]} <--\n')
                self.analisando_arquivos_classes(classes[opcao])
                break
            else:
                print('arquivo nao encontrado')
    def Opcao_3_Mostrando_alunos_aprovados(self):
        classes = self.ler_arquivo_geral()
        while True:
            try:
                [print(f'[{i}°] ---> {arquivo}') for i, arquivo in enumerate(classes)]
                opcao = int(input('Escolha um dos arquivos: '))
                if opcao in range(len(classes)):
                    print(f'\nA classe escolhida foi: --> {classes[opcao]} <--\n')
                    arquivo_cop = classes[opcao]
                    with open(arquivo_cop, 'r', encoding='utf-8') as arquivo:
                        linhas = arquivo.readlines()
                        lista_de_aprovados = []
                        for linha in linhas:
                            nomes = linha.strip().split(',')[1]
                            aprovados = linha.strip().split(': ')[5]
                            if aprovados == 'APROVADO':
                                lista_de_aprovados.append({'nome': nomes, 'status': aprovados})
                        if len(lista_de_aprovados) > 0:
                            return lista_de_aprovados, arquivo_cop
                        else:
                            return [], arquivo_cop
                else:
                    print('por favor escolher somente entre as opções provindas da tabela!')
            except FileNotFoundError:
                print('\033[31m O nome da classe existe, mas o arquivo não foi criado! \n\033[0m')
    def Opcao_4_Mostrando_alunos_reprovados(self):
        classes = self.ler_arquivo_geral()
        while True:
            try:
                [print(f'[{i}°] ---> {arquivo}') for i, arquivo in enumerate(classes)]
                opcao = int(input('Escolha um dos arquivos: '))
                if opcao in range(len(classes)):
                    print(f'\nA classe escolhida foi: --> {classes[opcao]} <--\n')
                    arquivo_cop = classes[opcao]
                    with open(arquivo_cop, 'r', encoding='utf-8') as arquivo:
                        linhas = arquivo.readlines()
                        lista_de_reprovados = []
                        for linha in linhas:
                            nomes = linha.strip().split(',')[1]
                            aprovados = linha.strip().split(': ')[5]
                            if aprovados == 'REPROVADO':
                                lista_de_reprovados.append({'nome': nomes, 'status': aprovados})
                        if len(lista_de_reprovados) > 0:
                            return lista_de_reprovados, arquivo_cop
                        else:
                            return [], arquivo_cop
                else:
                    print('por favor escolher somente entre as opções provindas da tabela!')
            except FileNotFoundError:
                print('\033[31m O nome da classe existe, mas o arquivo não foi criado! \n\033[0m')

    def analisando_arquivos_classes(self, arquivo):
        try:
            if not arquivo:
                print('\033[31m Essa classe não contem nenhum aluno! \033[0m')
            else:
                with open(arquivo, 'r', encoding='utf-8') as arquivo:
                    linhas = arquivo.readlines()
                    print(f'---------- Nomes dos alunos da classe ----------')
                    [print(l.strip().split(',')[1]) for l in linhas]
                    print()
        except FileNotFoundError:
            print('\033[31m Seu nome existe, mas o arquivo não foi criado!\n \033[0m')

    def main(self):
        while True:
            self.exibir_menu_principal()
            try:
                opcao = int(input('Opção: '))
                if opcao == 1:
                    print('\n\033[32mIniciando programa de criação de arquivos (classes)\033[0m\n')
                    nomes = self.Opcao_1_criando_nomes_de_arquivos() # <- esta retornando uma lista contida com os nomes.
                    self.armazenar_nomes_arquivos(nomes)
                elif opcao == 2:
                    if self.analise() is True:
                        alunos = self.Opcao_2_criando_cadastros_de_alunos() # <- retorna uma lista contendo os alunos
                        self.exibir_dados_alunos(alunos)
                        self.Opcao_2_adicionando_dados_arquivo(alunos)
                    else:
                        continue
                elif opcao == 3:
                    if self.analise() is True:
                        pesquisando = self.Opcao_3_pesquisando()
                    else:
                        continue
                elif opcao == 4:
                    print('Encerrando programa.')
                    break
                else:
                    print('Opção inválida. Digite um número de opção válido.')
            except ValueError:
                print('Opção inválida. Digite um número de opção válido.')

if __name__ == '__main__':
    gerenciador = GerenciadorDeNotasEAlunos()
    gerenciador.main()
