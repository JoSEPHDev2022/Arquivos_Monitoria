# WHILE > Loop utilizado para realizarmos uma operação enquanto uma condição é real:
while True:
    print('Olá! Você esta dentro do loop')
    escolha = input('Você quer mostrar essa mensagem novamente? (S/N): ')

    if escolha != 'S':
        break

# FOR > Loop utilizado para iterar/percorrer itens de um "tamanho" definido:
# EXEMPLO:

# 1 - Pedir pro usuário um numero
# 2 - Printar cada numero de 0 ate o numero que o usuário pediu

numero_inicio = int(input('Qual o numero para iniciarmos a contagem: '))
numero_final = int(input('Qual o numero para finalizarmos a contagem: '))

for numero in range(numero_inicio, numero_final):
    print(numero)

# LEMBRANDO: PARÂMETROS DA FUNÇÃO RANGE()
# range(numero_inicio, numero_final, espaçamento)
# Range SÓ TRABALHA com números inteiros

# OPERADORES ARITMÉTICOS:

# == IGUALDADE/COMPARAÇÃO "se input == 2: print(input)"

# = ATRIBUIÇÃO "quero que a variavel x tenha o valor 2: x = 2"

# != DIFERENÇA "se input != 2: print(input)"

# EXEMPLO:
cor = 'verde'
if cor == 'verde':
    print(cor)

# / DIVISÃO com resultado completo (10 / 3 = 3.333333333)

# // DIVISÃO com resultado inteiro, apenas o número antes da virgula (10 / 3 = 3)

# % RESTO da divisão (10 % 3 = 1)

# SOMANDO FLOATS COM FUNÇÃO:
def somar_floats(num1, num2):
    return float(num1) + float(num2)

somar_floats(10.2, 89.2)