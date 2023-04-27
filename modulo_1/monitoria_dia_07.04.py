# COMENTÁRIOS! Isso é um comentário e ele é usado para podermos descrever nosso código,
# suas funcionalidades e o motivo de termos tomados nossas escolhas.
#===============================================================================================#
# Jeitos diferentes de print:
numero_1 = 10
numero_2 = 20

soma = numero_1 + numero_2

# Jeito do Denyson:
print('Soma', numero_1 + numero_2)

# Jeito 2, utilizando as "f strings" com o cálculo dentro das chaves:
print(f'Soma é igual a {numero_1 + numero_2}')

# Jeito 3, utilizando as "f strings" com a variável dentro:
print(f'Minha idade é: {soma}')

#===============================================================================================#
# Jeitos diferentes de pedir inputs de usuários:

# Explicitamente falando para o python que o que queremos é um número inteiro (modo recomendado):
numero_1 = int(input('Qual o primeiro numero: '))
numero_2 = int(input('Qual o segundo numero: '))

soma = numero_1 + numero_2
print(f'Soma é igual a {soma}')

# Realizando a transformação de texto para número depois de coletar a informação:
numero_1 = input('Qual o primeiro número da nossa soma: ')
numero_2 = input('Qual o segundo número da nossa soma: ')

numero_final_1 = int(numero_1)
numero_final_2 = int(numero_2)

soma = numero_final_1 + numero_final_2

print(soma)

# Jeitos diferentes de executar a mesma tarefa!

# TEMAS

# Basta clicarem na rodinha de configuração localizada no canto inferior esquerdo e clicar em "Temas > Temas de Cores",
# A partir dai é escolher qual melhor tema para vocês.