import random


class EletroDomestico:
    def __init__(self, nome, marca, estado, ligado=False):
        self._nome = nome
        self._marca = marca
        self._ligado = ligado
        self._estado = estado

    def checar_eletrodomestico(self):
        # probabilidades que ocorra um defeito para cada estado
        probabilidades_de_defeito = {
            'novo': 0.1,  # 10% de chance de defeito
            'usado': 0.3,  # 30% de chance de defeito
            'velho': 0.6  # 60% de chance de defeito
        }
        # Gere um número aleatório entre 0 e 1
        numero_aleatorio = random.random()
        if numero_aleatorio < probabilidades_de_defeito[self._estado]:
            return 'quebrou'
        else:
            return 'não quebrou'

    def liga_desliga(self):
        if self.checar_eletrodomestico() == 'quebrou':
            return 'quebrou'
        else:
            self._ligado = not self._ligado
            return 'ligado' if self._ligado else 'desligado'

    def __str__(self):
        return f'nome do eletrodomesticos: {self._nome}, marca: {self._marca}, estado: {self._estado}'


def eletro_domesticos():
    status = ['novo', 'usado', 'velho']
    probabilidade = [0.33, 0.33, 0.33]
    eletrodomesticos = [
        ('Geladeira', 'Brastemp', random.choices(status, probabilidade)[0]),
        ('Máquina de Lavar Roupa', 'Electrolux', random.choices(status, probabilidade)[0]),
        ('Fogão', 'Consul', random.choices(status, probabilidade)[0]),
        ('Micro-ondas', 'Panasonic', random.choices(status, probabilidade)[0]),
        ('Máquina de Lavar Louça', 'Bosch', random.choices(status, probabilidade)[0]),
        ('Forno Elétrico', 'Tramontina', random.choices(status, probabilidade)[0]),
        ('Aspirador de Pó', 'Dyson', random.choices(status, probabilidade)[0]),
        ('Liquidificador', 'Oster', random.choices(status, probabilidade)[0]),
        ('Cafeteira', 'Nespresso', random.choices(status, probabilidade)[0]),
        ('Forno de Micro-ondas', 'Samsung', random.choices(status, probabilidade)[0])
    ]
    return random.choice(eletrodomesticos)


def main():
    eletro = EletroDomestico(*eletro_domesticos())
    print('foi escolhido um eletrodomesticos randomicamente em um armazem.')
    print(f'seu aparelho é um: {eletro}')

    while True:
        try:
            ligar = input('Aperte [Q] para sair ou [L] para ligar ou desligar: ').lower()
            if ligar == 'l':
                resultado = eletro.liga_desliga()
                print(resultado)
                if resultado == 'quebrou':
                    print('Parece que o aparelho quebrou, infelizmente não será possível continuar ligando e desligando.')
                    break

            elif ligar == 'q':
                print('fim do programa')
                break
            else:
                print('o programa lê apenas L ou Q')

        except Exception as e:
            print(str(f'Erro: {e}'))


if __name__ == "__main__":
    main()
