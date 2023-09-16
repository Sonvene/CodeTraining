class Televisao:
    def __init__(self, maximo=10):
        self.som_tv = 1
        self.maximo = maximo

    def alterar_som(self, acao):
        if acao == 'aumentar' and self.som_tv < self.maximo:
            self.som_tv += 1
        elif acao == 'diminuir' and self.som_tv > 0:
            self.som_tv -= 1
class ControleRemoto:
    def __init__(self, canal=0, canais=10):
        self.__canal = canal
        self.__canais = canais

    def subir(self, tv):
        self.__canal = (self.__canal + 1) % self.__canais

    def descer(self, tv):
        self.__canal = (self.__canal - 1) % self.__canais

    def mostrar_canal(self, tv):
        return f'\nCanal: {self.__canal + 1}\nSom: {"*" * tv.som_tv}'

def main():
    num_canais = 10
    nomes_canais_tv = [f"Canal {i + 1}" for i in range(num_canais)]

    tv = Televisao()
    con = ControleRemoto(canais=num_canais)

    while True:
        try:
            opcao = input('\nControle: [s] para subir [d] para descer [q] para desligar TV: '
                          '\n          [a] para aumentar som   [g] para diminuir som'
                          '\n          Opção: ')

            if opcao.lower() == 's':
                con.subir(tv)
            elif opcao.lower() == 'd':
                con.descer(tv)
            elif opcao.lower() == 'a':
                tv.alterar_som('aumentar')
            elif opcao.lower() == 'g':
                tv.alterar_som('diminuir')
            elif opcao.lower() == 'q':
                print('\nDesligando...')
                break

            print(con.mostrar_canal(tv))

        except (ValueError, TypeError):
            print('Valor inválido.')

if __name__ == "__main__":
    main()