# Palavras Reservadas
# Input = ENTRADA de dados
nome = input('Olá! Qual seu nome? ')
# # Print = SAÍDA de dados
print(nome)

# Checando TIPO do dado com a função type()
numero_1 = float(input('Digite um numero: '))
numero_2 = float(input('Digite outro numero: '))

soma = numero_1 + numero_2

print(soma)
print(type(soma))

print(type('uahuahuhad'))
print(type(10))
print(type(True))

idade = 'Minha idade é 21 anos'
print(type(idade))

# FUNÇÕES:
def nome_da_funcao(parametros):
    soma = numero_1 + numero_2
    return soma

# IDENTAÇÃO PESQUISEM!!

def soma_numeros(numero_1, numero_2):
    soma = numero_1 + numero_2
    return soma

print(soma_numeros(30, 90))

def nome_da_pessoa(nome):
    return nome

print(nome_da_pessoa('Luiz'))

# OPERADORES DE COMAPRAÇÃO
# 100 > 20      # Verdadeiro  (100 maior que 20)
# 100 < 20      # Falso       (100 menor que 20)
# 100 >= 20     # Verdadeiro  (100 é maior OU igual a 20)
# 100 <= 20     # Falso       (100 é menor OU igual a 20)
# 100 != 20     # Verdadeiro  (100 é diferente de 20)
# 100 == 20     # Falso       (100 NÃO É igual a 20)

numero_1 = float(input('Digite um numero: '))

if numero_1 > 10: # SE for positivo, entre no bloco do if e execute
    print('Número inserido é maior que 10')
elif numero_1 < 10:
    print('Número inserido é menor que 10')
elif numero_1 == 1:
    print('Sim, é igual a 1')
else:
    print('Numéro inserido é 10')


