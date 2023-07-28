'''ENCAPSULAMENTO'''

'''Atibutos Públicos

Public: Os membros de uma classe (atributos e métodos) são públicos por padrão em Python, 
o que significa que podem ser acessados de qualquer lugar:
'''

class Carro:
    def __init__(self, marca):
        self.marca = marca
        
    def iniciar_motor(self):
        print("Motor Iniciado")

# Criando um objeto da classe Carro
meu_carro = Carro("Tesla")
print(meu_carro.marca)  # Acesso público ao atributo 'marca'
meu_carro.iniciar_motor()  # Acesso público ao método 'iniciar_motor'


'''Atributos Privados

Private: Os membros de uma classe podem ser tornados privados prefixando-os com dois sublinhados __. 
Isso indica que eles devem ser acessados apenas de dentro da própria classe:
'''

class ContaBancaria:
    def __init__(self, numero_conta, balanco):
        self.__numero_conta = numero_conta
        self.__balance = balanco
        
    def __check_balanco(self):
        return self.__balance

# Criando um objeto da classe ContaBancaria
minha_conta = ContaBancaria("1234567890", 1000)
print(minha_conta.__numero_conta)  # Erro! Atributo privado
print(minha_conta.__check_balanco())  # Erro! Método privado


'''Atributos Protegidos

Protected: Embora Python não tenha um modificador de acesso explicitamente chamado "protected", 
pode-se usar um sublinhado _ no início de um nome de atributo ou método para indicar que eles são 
protegidos e devem ser acessados apenas por subclasses ou dentro do mesmo módulo:
'''

class Animal:
    def __init__(self, nome):
        self._nome = nome
        
    def _emitir_som(self):
        pass

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)
        
    def emitir_som(self):
        self._emitir_som()

# Criando um objeto da classe Gato
my_Gato = Gato("Whiskers")
print(my_Gato._nome)  # Acesso protegido ao atributo '_nome'
my_Gato.emitir_som()  # Acesso protegido ao método '_emitir_som'











class DadosIniciais:
    def __init__(self):
        self._nome = ''
        self._idade = 0
        self._cidade = ''

    def _coleta_nome(self):
        self._nome = input('Insira seu nome: ')
    
    def _coleta_idade(self):
        self._idade = int(input('Insira sua idade: '))

    def _coleta_cidade(self):
        self._cidade = input('Insira sua cidade: ')



class Menu(DadosIniciais):
    def __init__(self):
        super().__init__()

    def _mostrar_resultados(self):
        print(f'Seu nome: {self._nome}')
        print(f'Sua idade: {self._idade}')
        print(f'Sua cidade: {self._cidade}')

objeto = Menu()

objeto._coleta_nome()
objeto._coleta_cidade()
objeto._coleta_idade()

objeto._mostrar_resultados()