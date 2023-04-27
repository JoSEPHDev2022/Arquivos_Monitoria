# CONSTANTES: IMUTÁVEIS!.... só que não
'''
Constantes em Python são definidas por letras maiúsculas (EXEMPLO, MINHA_CONSTANTE, ISSO_É_UMA_CONSTANTE).
Elas indicam ao leitor do código que o valor atribuído a elas NÃO DEVE ser alterado, uma convenção apenas, pois
podemos de fato alterar seu valor.
'''
MINHA_CONSTANTE = 20
print(MINHA_CONSTANTE) # mostra 20

# Se eu tentar alterar seu valor, ele será alterado, pois declarar uma constante apenas INDICA ao leitor
# que esse valor não deve ser alterado, porém sim, ele pode ser manipulado:
MINHA_CONSTANTE = 40 # alterando valor
print(MINHA_CONSTANTE) # mostra 40

# Usamos elas quando sabemos que um valor é imutável e queremos mostrar aos usuários e leitores que esse valor
# não deve ser alterado.
VELOCIDADE_DA_LUZ = 299792458

tempo = int(input('')) # tempo é uma VARIAVEL, que muda de acordo com o que o usuário pede
distancia = int(input('')) # distancia também é uma VARIAVEL, que muda de acordo

calculo = (tempo * distancia) / VELOCIDADE_DA_LUZ

# Nesse exemplo, utilizamos variáveis (letras minusculas) para definir o valor do tempo e distancia,
# porem no calculo utilizamos uma constante (DEFINIDA EM LETRAS MAIUSCULAS) para definir a velocidade
# imutável da luz.

#===========================================================================================================#
# FUNÇÕES: Podem RETORNAR algo ou nos MOSTRAR algo

# Função que MOSTRA um resultado final porém que não nos permite a manipulação 
# futura desse resultado:
def soma_print(num_1, num_2):
    return print(f'O resultado de {num_1} + {num_2} é {num_1 + num_2}')

# Função que RETORNA um resultado final, permitindo manipulação posterior:
def soma_return(num_1, num_2):
    return num_1 + num_2

# Se eu quiser chamar a função, basta utilizar seu nome e passar os argumentos:
soma_print(10, 10)      # Resultado mostrado no terminal, porém impossível de ser manipulado

soma_return(10, 10)     # Resultado não aparece no terminal, porém possível de ser manipulado

# Exemplo de manipulação:
resultado = soma_return(20,20)

if resultado >= 100:
    print('Maior que cem')
else:
    print('Menor que cem')

# Essa manipulação só é possivel com a função que utiliza o RETURN, pois a função realiza os cálculos
# e nos RETORNA o resultado, permitindo manipulação.

# Essa mesma manipulação não é possivel com a função que apenas MOSTRA o resultado na tela, a função
# que utiliza o print

# Exemplo de manipulação que NÃO funciona:
resultado = soma_print(20,20)

if resultado >= 100:
    print('Maior que cem')
else:
    print('Menor que cem')

# Para mostrar o resultado de uma função qure RETORNA o resultado, podemos englobar a chamada da função em um print:
print(soma_return(10, 10))
#===========================================================================================================#
# APRIMORANDO FUNÇÕES:

# Uma função pode ser simples:
def calculo_frete(endereço, preco_compra, cpf):
    VARIACAO = 15
    calculo = preco_compra * VARIACAO
    return print(f'Seu endereço é {endereço} seu cpf é {cpf} seu valor total é {calculo}')

# Passe o mouse em cima do nome da função abaixo, as informações que temos são:

# (function) def calculo_frete(
#     endereço: Any,
#     preco_compra: Any,
#     cpf: Any
# ) -> None

calculo_frete('Rua dos bobos', 1000, '44444444444')

# Podemos especificar ao usuário o que EXATAMENTE essa função faz, que tipos de dados aceita e
# o que retorna utilizando documentação e tipos de dados:

#                   explicitando os tipos de dados dos parâmetros -> o tipo de dado retornado pela função
def calculo_frete(endereço: str, preco_compra: float, cpf: str) -> str:
    # abaixo, documentação da função (o texto que aparece ao passar o mouse pelo nome da função)
    '''
    Essa função pega o endereço, o preço da compra e o cpf do usuário
    e retorna uma string formatada com as informações.

    Parametros
    ----------
    endereço = Só aceito <str> Logradouro da pessoa

    preco_compra = Só aceito <float> Valor final da compra da pessoa

    cpf = Só aceito <str> CPF da pessoa

    Exemplo
    --------
    >>> calculo_frete('XXXXX', 1000.55, '11111111')
    >>> f'Seu endereço é {endereço} seu cpf é {cpf} seu valor total é {calculo}'
    '''
    VARIACAO = 15
    calculo = preco_compra * VARIACAO
    return print(f'Seu endereço é {endereço} seu cpf é {cpf} seu valor total é {calculo}')

# Agora, ao passar o mouse no nome da função, vemos o seguinte:

# (function) def calculo_frete(
#     endereço: str,
#     preco_compra: float,
#     cpf: str
# ) -> str
# Essa função pega o endereço, o preço da compra e o cpf do usuário e retorna uma string formatada com as informações.

# Parametros
# endereço = Só aceito <str> Logradouro da pessoa

# preco_compra = Só aceito <float> Valor final da compra da pessoa

# cpf = Só aceito <str> CPF da pessoa

# Exemplo
# >>> calculo_frete('XXXXX', 1000.55, '11111111')
# >>> f'Seu endereço é {endereço} seu cpf é {cpf} seu valor total é {calculo}'

# Uma informação completa do que faz a função
calculo_frete('Rua dos bobos', 1000, '44444444444')
#===========================================================================================================#
# ARGUMENTOS, TENHO QUE SEMPRE PASSAR DOIS NUMEROS PRA SOMA?

# Ao criarmos a seguinte função:
def soma(num_1, num_2):
    return num_1 + num_2

soma(10, 10) # retorna corretamente 20
soma(10, 10, 10) # retorna um erro, pois passamos mais de 2 numeros para a função
soma(10) # retorna um erro, pois passamos menos de 2 numeros para a função

# Estamos FORÇANDO a função a trabalhar não com 1, não com 3, mas com 2 números apenas.
# Porém, e se o usuário quiser somar uma gama de números? como fazemos para nossa função
# funcionar com quantos números forem que o usuário passe? Com asterisco!

# Função que soma uma quantidade qualquer de numeros:
def soma_tudo(*numeros):
    return sum(numeros)

soma_tudo(10,10,10,10) # retorna 40
soma_tudo(10,10) # retorna 20
soma_tudo(20,11,22,33,4,3,2,1) # retorna 96