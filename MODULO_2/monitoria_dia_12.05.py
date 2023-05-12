# Listas, como percorremos?

# Listas com 4 valores, começando do ínice 0 e indo até o 3
nome = ['José', 'Lucas', 'Luciana', 'Matheus']   
idade = [13, 25, 65, 55]                                

# Printando nomes e idades usando ZIP:

# Função ZIP: UNIFICA duas listas pelos seus índices, zero com zero, um com um, etc.
# Percorremos CADA nome e CADA idade ao mesmo tempo com a função zip:
for nomes, idades in zip(nome, idade):
    if idades > 18:
        print(f'MAIOR DE IDADE: {nomes} tem {idades} anos de idade')
    else:
        print(f'MENOR DE IDADE: {nomes} tem {idades} anos de idade')
#==============================================================================#
# MOSTRAR DICIONÁRIOS DENTRO DE LISTAS

# Primeiro, o que são dicionários? Pares de CHAVE e VALOR, exemplo:
# LISTAS = ['valor_1', 'valor_2', 'valor_3']
# DICIONÁRIOS = {'chave_1': 'valor_1', 'chave_2': 'valor_2'}

# Podemos juntar as duas estruturas, 4 dicionários dentro de uma LISTA:
pessoas = [{'Nome': 'José', 'Idade': 13}, # registro 1
           {'Nome': 'Lucas', 'Idade': 25}, # registro 2
           {'Nome': 'Luciana', 'Idade': 65}, # registro 3
           {'Nome': 'Matheus', 'Idade': 55}] # registro 4

# Temos duas estruturas, dicionários dentro de listas, para acessar cada "nível" dessas estruturas,
# precisamos de um loop. 

# Para printarmos na tela cada registro (cada dicionário), utilizamos um loop:
for registros in pessoas:
    print(registros)
# Entramos no PRIMEIRO nível, estamos dentro das listas vendo os dicionários.
# Para entrarmos no SEGUNDO nível, para entrarmos dentro dos valores dentro dos dicionários, criamos outro loop:


for registros in pessoas: # Entra na lista
    for valores in registros: # Entra nos dicionários DENTRO da lista
        print(valores)
#==============================================================================#
# Prints detalhados com um contador simples:
pessoas = [{'Nome': 'José', 'Idade': 13}, 
           {'Nome': 'Lucas', 'Idade': 25}, 
           {'Nome': 'Luciana', 'Idade': 65} ,
           {'Nome': 'Matheus', 'Idade': 55}]

cont = 0
for registros in pessoas:
    cont += 1
    nome = registros['Nome']
    idade = registros['Idade']
    print(f'Registro {cont}: {nome}, de {idade} anos de idade')
#==============================================================================#
# Função para filtrar pessoas:
def filtrar_por_idade(pessoas, idade_minina):
    pessoas_filtradas = []

    for pessoa in pessoas:
        idade = pessoa['Idade']

        if idade > idade_minina:
            pessoas_filtradas.append(pessoa)

    return pessoas_filtradas


# Lista com participantes e idades
pessoas = [{'Nome': 'José', 'Idade': 14}, 
            {'Nome': 'Lucas', 'Idade': 25}, 
            {'Nome': 'Luciana', 'Idade': 65},
            {'Nome': 'Matheus', 'Idade': 55}]

# Pedir a nota de corte (nesse caso a idade) para o usuário
idade_minina = int(input('Informe a idade mínima desejada: '))

# Chama a função, passando a lista com dicionários (pessoas) e a nota de corte (idade_minima):
pessoas_filtradas = filtrar_por_idade(pessoas, idade_minina)

# Imprimir os resultados utilizando a função enumerate:
for index, pessoa in enumerate(pessoas_filtradas, start=1):
    nome = pessoa['Nome']
    idade = pessoa['Idade']
    print(f'Registro de número {index}: {nome} de idade {idade} anos de idade')