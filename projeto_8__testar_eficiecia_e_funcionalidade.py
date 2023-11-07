from random import randint as rd

class Pessoa:

    arquivo_txt = 'dados.txt'

    def __init__(self, nome, endereco, telefone):
        self.__dados = self.gerar_dados(nome, endereco, telefone)

    def gerar_dados(self, nomes, enderecos, telefones):
        for nome, endereco, telefone in zip(nomes, enderecos, telefones):
            yield f'{nome}, {endereco}, {telefone}'

    def salvar_no_arquivo(self):
        with open(self.arquivo_txt, 'w+', encoding='UTF-8') as arq:
            for dado in self.__dados:
                arq.write(dado+'\n')

    @classmethod
    def lendo_arquivo(cls):
        with open(cls.arquivo_txt, 'r', encoding='UTF-8') as arq:
            for linha in arq:
                yield linha.strip()

def tabela_principal():
    print('1. Criar cadastros aleatórios')
    print('2. Pesquisar')
    print('3. Encerrar')

def tabela_de_pesquisa(lista_de_dados):
    [print(i) for i in lista_de_dados]
    print('1. Escolher alguém')
    print('2. Sair')
    opc = int(input('Opção: '))

    if opc == 1:
        escolha = int(input('Escolha uma pessoa pelo número: '))
        if 1 <= escolha <= len(lista_de_dados):
            print(f'Você escolheu: {lista_de_dados[escolha - 1]}')
        else:
            print('Numero invalido')
    elif opc == 2:
        pass
    else:
        print("Opção de pesquisa inválida.")

def tratar_erros(funcao):
    def func(*args, **kwargs):
        try:
            funcao(*args, **kwargs)
        except Exception as e:
            print(f'Erro: {e}')
    return func

@tratar_erros
def main():
    while True:
        try:
            tabela_principal()
            opc = int(input('Opção: '))

            if opc == 1:
                qtd = int(input('quantos dados quer criar randomicamente?: '))
                nomes = [f'Pessoa {i}°' for i in range(1, qtd+1)]
                enderecos = [f'Endereco {i}°' for i in range(1, qtd+1)]
                telefones = [f'Telefone {rd(1000, 9999)}-{rd(1000, 9999)}' for i in range(1, qtd+1)]
                pessoa = Pessoa(nomes, enderecos, telefones)
                pessoa.salvar_no_arquivo()
                print('Cadastros aleatórios criados.')

            elif opc == 2:
                print('Pesquisando pessoas:')
                lista_de_pessoas = Pessoa.lendo_arquivo()
                if lista_de_pessoas:
                    lista_de_dados = [pessoa for pessoa in lista_de_pessoas]
                    tabela_de_pesquisa(lista_de_dados)
                else:
                    print("Nenhum cadastro disponível.")

            elif opc == 3:
                print('encerrando programa')
                break

        except (ValueError, TypeError) as e:
            print(f'Erro: {e}')

if __name__ == '__main__':
    main()
