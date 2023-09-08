import random
from time import sleep

class Elevador:
    def __init__(self, capacidade, andar, andares):
        self.__capacidade = capacidade
        self.__andar = andar
        self.__andares = andares

    lista_de_passageiros = []

    def subindo(self, novo_andar):
        try:
            if novo_andar == self.__andar:
                print('Você já está no andar atual')
                return
            if novo_andar < 0:
                print('Somente valores positivos são permitidos')
                return
            if novo_andar < self.__andar:
                print('Você escolheu subir, mas o elevador só pode descer')
                return
            if novo_andar > self.__andares:
                print(f'O andar máximo é o {self.__andares}, não é possível subir mais')
                return

            print(f'O elevador está subindo para o {novo_andar}º andar.')
            for i in range(self.__andar, novo_andar + 1):
                sleep(0.2)
                print(f'-> {i}')
                sleep(0.2)
                self.__andar = novo_andar

            print(f'O elevador parou no {novo_andar}º andar')
            self.verifica_andar(self.__andar)
        except (ValueError, TypeError):
            print('Valor incorreto!')

    def descendo(self, novo_andar):
        try:
            if novo_andar == self.__andar:
                print('voce ja esta no andar atual')
                return
            if novo_andar < 0:
                print('0º Andar e o ultimo, não e possivel descer alem disso')
                return
            if novo_andar > self.__andar:
                print('voce escolheu descer e nao subir')
                return
            if novo_andar < 0:
                print('\nO 0º Andar e o ultimo, não e possivel descer alem disso')
                return

            for i in range(self.__andar, novo_andar - 1, -1):
                sleep(0.2)
                print(f'-> {i}')
                sleep(0.2)
                self.__andar = novo_andar

            print(f'\nO Elevadou parou no {novo_andar}º andar')
            Elevador.verifica_andar(self.__andar)

            if self.__andar == 0:
                Pessoa.selecao()
        except (ValueError, TypeError):
            print('Valor incorreto!')

    @classmethod
    def verifica_andar(cls, andar):
        try:
            pessoas = cls.lista_de_passageiros
            pessoas_no_andar = []

            for pessoa in pessoas:
                if pessoa[1] == andar:
                    print(f'--> {pessoa[0]} saiu do elevador.')
                    pessoas_no_andar.append(pessoa)

            for pessoa in pessoas_no_andar:
                cls.lista_de_passageiros.remove(pessoa)
        except (ValueError, TypeError):
            print('Valor incorreto')

class Pessoa:

    contador = 0
    fila_de_espera = [] # Tenho 10 pessoas esperando
    lista_de_quem_ja_foi = []

    def __init__(self, pessoa, destino):
        self.id = Pessoa.contador + 1
        self.__pessoa = pessoa
        self.__destino = destino
        Pessoa.contador = self.id
        Pessoa.fila_de_espera.append((pessoa, destino))

    @classmethod
    def selecao(cls):
        try:
            if len(Pessoa.fila_de_espera) >= 0:
                for pessoa in list(Pessoa.fila_de_espera):
                    if pessoa not in Pessoa.lista_de_quem_ja_foi:
                        if len(Elevador.lista_de_passageiros) < 4:
                            print(f'[{pessoa[0]}] - Entrou no elevador')
                            Elevador.lista_de_passageiros.append(pessoa)
                            Pessoa.fila_de_espera.remove(pessoa)  # Remove a pessoa da fila após seleção
            else:
                print('Não tem mais ninguem esperando!')
        except (ValueError, TypeError):
            print('Valor incorreto')

def tabela_informativa():
    print(f'\nDescrição para operador de elevador: (nome/destino).')
    print(f'Tabela de passageiros:')
    [print(f'--> Nome: {nome} / Andar: {andar}') for nome, andar in Elevador.lista_de_passageiros]
    print()

def main():
    while True:
        try:
            tabela_informativa()
            opc = input('Opção: [ S ] pra subir, [ D ] para descer: ')

            if opc.lower() == 's':
                andar = int(input('informa um andar: '))
                elevator.subindo(andar)

            elif opc.lower() == 'd':
                andar = int(input('informa um andar: '))
                elevator.descendo(andar)

            if not Elevador.lista_de_passageiros and not Pessoa.fila_de_espera:
                print('Todos os passageiros foram entregues ao seu destino. Bom trabalho')
                break

        except (ValueError, TypeError):
            print('valor incorreto')


if __name__ == "__main__":
    elevator = Elevador(capacidade=4, andar=0, andares=10)
    for i in range(10):
        nomes = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
        andar_destino = random.randint(1, 10)
        Pessoa(nomes[i], andar_destino)
    Pessoa.selecao()
    main()