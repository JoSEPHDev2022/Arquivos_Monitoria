# MÉTODO SPLIT()

'''
O método .split() é uma função embutida do Python que permite dividir uma string em várias 
partes com base em um separador especificado. Essa função retorna uma lista contendo 
as substrings resultantes da divisão
'''

# SINTAXE:  string.split(separador, maxsplit)

'''
Parâmetros:

- separador (opcional): É uma string que determina onde a divisão será feita. Se omitido, o 
                        separador padrão é um espaço em branco. O separador pode ser qualquer 
                        sequência de caracteres.

- maxsplit (opcional): É o número máximo de divisões que podem ser feitas. Se omitido, 
                     todas as ocorrências do separador serão consideradas.
'''

# EXEMPLO 1:
frase = "Olá, como vai você?"
palavras = frase.split()  # Dividindo por espaços em branco

print(palavras) # Saída: ['Olá,', 'como', 'vai', 'você?']

'''
Nesse exemplo, a string "Olá, como vai você?" é dividida em uma lista de palavras usando o espaço em branco 
como separador. A saída mostra a lista de palavras resultante.
'''

# EXEMPLO 2:
data = "2023-05-18"
dia, mes, ano = data.split("-")

print("Dia:", dia) # Dia: 2023
print("Mês:", mes) # Mês: 05
print("Ano:", ano) # Ano: 18


'''
Nesse exemplo, uma string contendo uma data no formato "AAAA-MM-DD" é dividida usando o caractere de hífen 
"-" como separador. O método .split() retorna uma lista com as partes divididas, e cada parte é atribuída 
a uma variável diferente. A saída mostra o dia, mês e ano separados.
'''

# EXEMPLO 3:
frase = "Maçã,Laranja,Banana,Morango"
frutas = frase.split(",")

print(frutas) # Saída: ['Maçã', 'Laranja', 'Banana', 'Morango']

'''
Nesse exemplo, uma string contendo várias frutas separadas por vírgulas é dividida usando a vírgula como separador. 
A função .split() retorna uma lista de frutas.

Esses são apenas alguns exemplos básicos de aplicação do método .split() do Python. É importante notar que a função 
retorna uma lista, o que permite acessar as partes individuais da string dividida. Essa função é muito útil para 
processar dados de texto e realizar operações em partes específicas de uma string.
'''
#===================================================================================================================================#
# MÉTODO .JOIN()

'''
O método .join() é uma função embutida do Python que permite concatenar elementos de uma lista ou iterável em uma única 
string. Essa função é chamada em um separador específico e retorna a string resultante da concatenação dos elementos. 
'''

# SINTAXE:  separador.join(iterável)

'''
Parâmetros:

- separador: É uma string que será usada como separador entre os elementos concatenados. A string vazia '' pode 
             ser usada como separador se nenhuma separação for desejada.

- iterável: É uma sequência de elementos que serão concatenados. Pode ser uma lista, uma tupla, um conjunto ou qualquer 
            outro iterável.
'''

# EXEMPLO 1:
palavras = ['Olá,', 'como', 'vai', 'você?']
frase = ' '.join(palavras)  # Concatenando com espaço em branco

print(frase) # Saída: Olá, como vai você?

'''
Nesse exemplo, uma lista de palavras é concatenada em uma única string usando um espaço em branco como separador. 
O método .join() retorna a string resultante.
'''

# EXEMPLO 2:
numeros = ['1', '2', '3', '4', '5']
lista_numeros = '-'.join(numeros)  # Concatenando com hífen

print(lista_numeros) # Saída: 1-2-3-4-5


'''
Nesse exemplo, uma lista de números é concatenada em uma única string usando um hífen como separador. 
O método .join() retorna a string resultante.
'''

# EXEMPLO 3:
conjunto_letras = {'a', 'b', 'c', 'd'}
string_letras = ''.join(conjunto_letras)  # Concatenando sem separador

print(string_letras) # Saída: abcd

'''
Nesse exemplo, um conjunto de letras é concatenado em uma única string sem nenhum separador. 
O método .join() retorna a string resultante
'''