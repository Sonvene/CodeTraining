import math

class FormaGeometrica:
    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.__lado = lado

    def calcular_area(self):
        return f'Área: {self.__lado * self.__lado}'

    def calcular_perimetro(self):
        return f'Perimetro: {4 * self.__lado}'

class Retangulo(FormaGeometrica):
    def __init__(self, comprimento, largura):
        self.__comprimento = comprimento
        self.__largura = largura

    def calcular_area(self):
        return f'Área: {self.__comprimento * self.__largura}'

    def calcular_perimetro(self):
        return f'Perimetro: {2 * (self.__comprimento + self.__largura)}'

class TrianguloEquilatero(FormaGeometrica):
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calcular_area(self):
        return f'Área: {(self.__base * self.__altura) / 2}'

    def calcular_perimetro(self):
        """como é um Triangulo Equilatero onde cada lado A, B e C são iguais, defini que
        - base - representasse os lados (A + B + C) respectivamente com intuito de calcular o perimetro"""
        return f'Perimetro: {self.__base + self.__base + self.__base}'

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.__raio = raio

    def calcular_area(self):
        return f'Área: {math.pi * self.__raio ** 2}'

    def calcular_perimetro(self):
        return f'Perimetro: {2 * math.pi * self.__raio}'

def validar(*valores):
    for valor in valores:
        if valor < 0:
            ValueError(f"O valor {valor} é negativo e não é possível calcular esta forma geométrica com um valor negativo!")

def tabela():
    print('Escolha uma forma geométrica.')
    print('1. Quadrado')
    print('2. Retangulo')
    print('3. Triangulo Equilatero')
    print('4. Circulo')
    print('5. Sair')

def main():
    while True:
        try:
            tabela()
            opc = int(input('Opção: '))

            if opc == 1:
                lado = int(input('informar o valor do lado: '))
                validar(lado)
                quadrado = Quadrado(lado=lado)
                print(quadrado.calcular_area())
                print(quadrado.calcular_perimetro())

            elif opc == 2:
                comprimento = int(input('informar o valor do comprimento: '))
                largura = int(input('informar o valor da largura: '))
                validar(comprimento, largura)
                retangulo = Retangulo(comprimento=comprimento, largura=largura)
                print(retangulo.calcular_area())
                print(retangulo.calcular_perimetro())

            elif opc == 3:
                base = int(input('informar o valor da base: '))
                altura = int(input('informar o valor da altura: '))
                validar(base, altura)
                triangulo = TrianguloEquilatero(base=base, altura=altura)
                print(triangulo.calcular_area())
                print(triangulo.calcular_perimetro())

            elif opc == 4:
                raio = int(input('informar o valor do raio: '))
                validar(raio)
                circulo = Circulo(raio=raio)
                print(circulo.calcular_area())
                print(circulo.calcular_perimetro())

            elif opc == 5:
                print('Fim do programa')
                break

        except Exception as e:
            print(f'Erro: {e}')

if __name__ == '__main__':
    main()
