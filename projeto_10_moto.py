import random

class Moto:

    marchas = ['Neutro', 'Primeira', 'Segunda', 'Terceira', 'Quarta', 'Quinta', 'Sexta', 'Sétima', 'Oitava', 'Nona',
               'Décima']

    def __init__(self, marca, modelo, cor, ligada=False, marcha_atual=0, max_marchas=10):
        self.__marca = marca
        self.__modelo = modelo
        self.__cor = cor
        self.__ligada = ligada
        self.__marcha_atual = marcha_atual
        self.__max_marchas = max_marchas

    @property
    def ligada(self):
        return self.__ligada

    @property
    def marcha_atual(self):
        return self.__marcha_atual

    @property
    def max_marchas(self):
        return self.__max_marchas

    def __str__(self):
        return (f'marca: {self.__marca} | '
                f'modelo: {self.__modelo} | '
                f'cor: {self.__cor} | '
                f'marcha: {self.marchas[self.__marcha_atual]} | '
                f'status: {"ligada" if self.__ligada else "desligada"}')

    @ligada.setter
    def ligada(self, valor):
        if valor in (True, False):
            self.__ligada = valor
        else:
            raise ValueError("O valor deve ser True ou False.")

    @marcha_atual.setter
    def marcha_atual(self, nova_marcha):
        if 0 <= nova_marcha <= self.__max_marchas:
            self.__marcha_atual = nova_marcha
        else:
            raise ValueError("A marcha atual deve estar entre 0 e o máximo de marchas.")

def dados_iniciais():
    cores = [
        "Vermelho", "Verde", "Azul", "Amarelo", "Laranja", "Roxo", "Rosa", "Preto", "Branco", "Cinza",
        "Marrom", "Bege", "Prata", "Ouro", "Turquesa", "Violeta", "Magenta", "Ciano", "Lilás", "Marron"]

    motos = [
        ("Honda", "CBR1000RR Fireblade", random.choice(cores)),
        ("Yamaha", "YZF-R6", random.choice(cores)),
        ("Suzuki", "GSX-R1000", random.choice(cores)),
        ("Kawasaki", "Ninja ZX-10R", random.choice(cores)),
        ("Ducati", "Monster 821", random.choice(cores)),
        ("Harley-Davidson", "Iron 883", random.choice(cores)),
        ("KTM", "1290 Super Duke R", random.choice(cores)),
        ("Triumph", "Bonneville T120", random.choice(cores)),
        ("BMW", "S 1000 RR", random.choice(cores)),
        ("Aprilia", "Tuono V4 1100 Factory", random.choice(cores))]

    marca, modelo, cor = random.choice(motos)
    return marca, modelo, cor

def trata_erros(funcao):
    def func(*args, **kwargs):
        try:
            funcao(*args, **kwargs)
        except ValueError as e:
            print(f"Erro: Valor inválido - {str(e)}")
        except IndexError as e:
            print(f"Erro: Índice inválido - {str(e)}")
        except Exception as e:
            print(f"Erro desconhecido: {str(e)}")
    return func

@trata_erros
def main():
    while True:
        moto = Moto(*dados_iniciais())
        ligar = input('[L] - Ligar moto | [Q] sair: ').upper()

        if ligar == 'L':
            moto.ligada = True

            while True:
                try:
                    print(moto)
                    acao = input('[A] aumentar a marcha | [D] diminuir a marcha | [Q] desligar: ').upper()

                    if acao == 'A':
                        moto.marcha_atual += 1
                    elif acao == 'D':
                        moto.marcha_atual -= 1
                    elif acao == 'Q':
                        break
                except Exception as e:
                    print(f"Erro: {e}")

        elif ligar == 'Q':
            moto.ligada = False
            print('Programa encerrado')
            break

if __name__ == '__main__':
    main()
