'''
Em Python, as classes são estruturas que permitem definir tipos de objetos. Uma classe é uma espécie de "modelo" ou "planta" 
que descreve as propriedades (atributos) e comportamentos (métodos) que os objetos desse tipo podem ter.

Em termos mais simples, uma classe é como um "molde" que define como um objeto deve ser criado. Ela encapsula dados (atributos)
 e funcionalidades (métodos) relacionadas em um único objeto.

As classes permitem criar objetos específicos a partir desse molde, conhecidos como instâncias da classe. Cada instância possui 
seus próprios valores de atributos, mas compartilha os mesmos métodos definidos na classe.

As classes são fundamentais para a programação orientada a objetos (POO), uma abordagem que organiza o código em torno de objetos 
e suas interações. Elas proporcionam uma maneira de modelar e estruturar a lógica de um programa de forma mais modular, reutilizável 
e compreensível.
'''

# EXEMPLO 1: Criando Cachorros:

class Cachorro:
    # Definindo a classe Cachorro

    def __init__(self, nome, idade):
        # Método especial para inicializar um objeto da classe
        # Recebe o nome e a idade do cachorro e os atribui como atributos do objeto
        self.nome = nome
        self.idade = idade
    
    def latir(self):
        # Método que faz o cachorro latir
        # Imprime uma mensagem indicando o nome do cachorro que está latindo
        return print(f"{self.nome} está latindo!")
    
    def definir_idade(self, nova_idade):
        # Método que permite alterar a idade do cachorro
        # Recebe uma nova idade como parâmetro e atualiza o atributo idade do objeto
        self.idade = nova_idade
    
    def obter_idade(self):
        # Método que retorna a idade do cachorro
        # Imprime a idade atual do cachorro
        return print(f'Idade: {self.idade} anos')
    
# Criando um objeto da classe Cachorro com nome 'Fido' e idade 3
meu_cachorro = Cachorro('Fido', 3)

# Imprimindo o nome e a idade do cachorro
print(meu_cachorro.nome)
print(meu_cachorro.idade)

# Fazendo o cachorro latir
meu_cachorro.latir()

# Obtendo a idade do cachorro
meu_cachorro.obter_idade()

# Alterando a idade do cachorro para 4
meu_cachorro.definir_idade(4)

# Obtendo a nova idade do cachorro
meu_cachorro.obter_idade()

'''
O QUE É ESSA CLASSE E COMO FUNCIONA? EM DETALHES:

O código acima é um exemplo de uma classe chamada "Cachorro". Uma classe é uma estrutura que define um tipo de objeto,
especificando seus atributos (propriedades) e métodos (ações que o objeto pode realizar). A classe é como uma "planta",
uma "ideia" das características que aquele objeto representa, classes são abstrações de estruturas.

Nesse código, a classe "Cachorro" possui os seguintes atributos:

- "nome": que representa o nome do cachorro.
- "idade": que representa a idade do cachorro.

Além dos atributos, a classe também possui os seguintes métodos:

- "init": é um método especial usado para inicializar um objeto da classe. Ele recebe o nome e a idade do cachorro 
como parâmetros e os atribui aos atributos correspondentes.

- "latir": é um método que imprime uma mensagem indicando que o cachorro está latindo. Ele usa o atributo "nome" 
para exibir o nome do cachorro.

- "definir_idade": é um método que permite alterar a idade do cachorro. Ele recebe uma nova idade como parâmetro e 
atualiza o atributo "idade" do objeto, da instância específica da classe Cachorro, nesse caso, atualiza a idade
do Fido.

- "obter_idade": é um método que retorna a idade do cachorro. Ele imprime a idade atual do cachorro.

No restante do código, é criado um objeto da classe "Cachorro" com o nome "Fido" e a idade 3. Em seguida, são realizadas 
algumas operações com esse objeto:

- O nome e a idade do cachorro são impressos.
- O cachorro é "comandado" para latir (chamamos o método latir()), exibindo a mensagem correspondente.
- A idade do cachorro é obtida e impressa.
- A idade do cachorro é alterada para 4.
- A nova idade do cachorro é obtida e impressa.

Basicamente, esse código representa uma estrutura básica para criar e interagir com objetos do tipo "Cachorro". Ele encapsula as 
informações e comportamentos relacionados a cachorros em uma classe, permitindo a reutilização do código e a manipulação de 
diferentes instâncias (objetos) de cachorros de forma independente.
'''
#======================================================================================================================================#
# EXEMPLO 2: Bot de informações? De novo?

class Bot:
    # Definindo a classe Bot

    def __init__(self, nome, localizacao, area_atuacao):
        # Método especial para inicializar um objeto da classe
        # Recebe o nome, localização e área de atuação da empresa e os atribui como atributos do objeto
        self.nome = nome
        self.localizacao = localizacao
        self.area_atuacao = area_atuacao

    def apresentar_empresa(self):
        # Método que apresenta a empresa
        # Imprime uma mensagem de boas-vindas com o nome da empresa, localização e área de atuação
        print(f"Bem-vindo! Somos a empresa {self.nome}.")
        print(f"Estamos localizados em {self.localizacao} e atuamos na área de {self.area_atuacao}.")
    
    def obter_nome(self):
        # Método que retorna o nome da empresa
        return self.nome
    
    def obter_localizacao(self):
        # Método que retorna a localização da empresa
        return self.localizacao
    
    def obter_area_atuacao(self):
        # Método que retorna a área de atuação da empresa
        return self.area_atuacao
    
    def verificar_dados(self):
        # Método que verifica se todos os dados necessários estão preenchidos
        if self.nome and self.localizacao and self.area_atuacao:
            print("Os dados estão preenchidos.")
        else:
            print("Faltam dados para preencher.")
    
# Criando um objeto da classe Bot com nome 'Nubank', localização 'São Paulo' e área de atuação 'Finanças'
empresa = Bot('Nubank', 'São Paulo', 'Finanças')

# Chamando o método apresentar_empresa para exibir informações sobre a empresa
empresa.apresentar_empresa()

# Obtendo o nome da empresa
nome_empresa = empresa.obter_nome()
print(f'Nome da empresa: {nome_empresa}')

# Verificando se os dados estão preenchidos
empresa.verificar_dados()

'''
O QUE É ESSA CLASSE E COMO FUNCIONA? EM DETALHES:

O código acima é um exemplo de uma classe chamada "Bot". Essa classe representa uma empresa ou organização e possui 
os seguintes atributos:

- "nome": que representa o nome da empresa.
- "localizacao": que representa a localização da empresa.
- "area_atuacao": que representa a área de atuação da empresa.

Além dos atributos, a classe também possui os seguintes métodos:

- "init": é um método especial usado para inicializar um objeto da classe. Ele recebe o nome, localização e área de 
atuação da empresa como parâmetros e os atribui aos atributos correspondentes.

- "apresentar_empresa": é um método que imprime uma mensagem de boas-vindas com o nome da empresa, localização e 
área de atuação.

- "obter_nome", "obter_localizacao" e "obter_area_atuacao" são métodos que retornam o nome, a localização e a área 
de atuação da empresa, respectivamente.

- "verificar_dados" é um método que verifica se todos os dados necessários (nome, localização e área de atuação) estão 
preenchidos. Ele imprime uma mensagem indicando se os dados estão preenchidos ou se faltam dados para preencher.

No restante do código, é criado um objeto da classe "Bot" com o nome "Nubank", a localização "São Paulo" e a área de atuação 
"Finanças". Em seguida, são realizadas as seguintes operações:

- O método "apresentar_empresa" é chamado para exibir informações sobre a empresa.
- O método "obter_nome" é chamado para obter o nome da empresa e o resultado é armazenado na variável "nome_empresa".
- O nome da empresa é impresso.
- O método "verificar_dados" é chamado para verificar se todos os dados necessários estão preenchidos, e uma mensagem é exibida indicando se os dados estão preenchidos ou se faltam dados.
'''
