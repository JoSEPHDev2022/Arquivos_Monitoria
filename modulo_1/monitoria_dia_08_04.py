# COMENTÁRIOS! isso é um comentário

# Utilizamos comentários para descrever brevemente o que partes do nosso código faz

'''
Porém caso seja necessário uma documentação mais longa, podemos utilizar comentários
em várias linhas tipo esse aqui, basta abrir três aspas simples ou duplas e 
sair escrevendo!
'''
#=============================================================================================#
# EXEMPLO DE UTILIZAÇÃO DE COMENTÁRIO:

# Essa var guarda o dinheiro que o cliente gastou no dia:
din_gasto = 100

# Essa var guarda o relato do cliente após a entrega:
review_cliente = 'sou uma variável que contém texto!'

print('Minhas variáveis:')
print(din_gasto)
print(review_cliente)
#=============================================================================================#
# NOMEANDO VARIÁVEIS:

# Nomes curtos e descritivos, evitem isso:
x = 20
hsd = 'Bom'

# Prefiram algo assim:
gorjeta = 20
avaliacao_entrega = 'Bom'
#=============================================================================================#
# SAÍDA DE DADOS: MIL E UMA FORMAS DIFERENTES

numero_1 = 1
numero_2 = 2

soma = numero_1 + numero_2

# Jeito 1, com vírgulas:
print('Soma = ', soma)

# Jeito 2, utilizando as "f strings" com o cálculo dentro das chaves:
print(f'Soma = {numero_1 + numero_2}')

# Jeito 3, utilizando as "f strings" com a variável dentro:
print(f'Minha idade é: {soma}')

# Jeito 4, usando .format:
print('Soma = {}'.format(soma))

# MAIS EXEMPLOS:
salario_min = 1000
salario_ser = 2000

resultado = salario_ser / salario_min

# Mostrar o resultado utilizando .format() com mais de uma variável:
print('O resultado do cálculo é {} e o salario minimo é {}'.format(resultado, salario_min))

# Utilizando "f strings" com mais de uma variável:
print(f'O resultado do cálculo é {resultado} e o salario minimo é {salario_min}')
#=============================================================================================#
# ARREDONDAMENTO DE VALORES

# Jeito 1, usando f string e arrendondano:
print(f'O resultado do cálculo é {resultado:.2f}')
'''
sintaxe: {variavel:.num_casa_decimaisf}
Exemplo (arredondar uma variável para ela ter 3 casas decimais):
    {variavel:.3f}
'''
# Jeito 2, usando a função round() do python:
num = 3.5645734563456
num_arredondado= round(num, 2)

print(f'O resultado arredondado utilizando o primeiro jeito: {num:.2f}')
print(f'O resultado arredondado utilizando a função round: {num_arredondado}')

'''
sintaxe da função round(): round(numero, qtde_casas_decimais)
Exemplo (arredondar uma variável para ela ter 4 casas decimais):
    numero = 3.56785343
    numero_arredondado = round(numero, 4)
'''