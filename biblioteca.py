class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'O {self.nome} foi comer...')
class Cachorro(Animal):
    def latir(self):
        print(f'O {self.nome} está latindo Au au!')
class Coelho(Animal):
    def pular(self):
        print(f'O {self.nome} está pulando muito deve ser por isso q o peludo está latindo!')
class Vaca(Animal):
    def mugir(self):
            print(f'A {self.nome} está atolada na lama e mugindo muito, enfim, nelore sendo nelore!')
    def comer(self):
        print(f'a {self.nome} foi comer capim por isso que ela atolou')

class Ingresso:
      def __init__(self, valor):
                self.valor = valor

      def imprimeValor(self):
        print(f'O valor do ingresso é R$ {self.valor:.2f}')
class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor * 1.50)

    def imprimeValor(self):
        print(f'O valor do ingresso é R$ {self.valor:.2f}')
