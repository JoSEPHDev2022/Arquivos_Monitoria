# EXEMPLO DE LÓGICA DE PROGRAMAÇÃO ERRADA:
# Utilizando ferramenta de depuração para achar o erro.
resposta = input('Você gosta de programação? (sim/nao): ')

while resposta != 'sim' or 'nao':
    print('Resposta inválida! Responda com "sim" ou "nao"')
    resposta = input('Você gosta de programação?: ')

if resposta == 'sim':
    print('Legal! Eu também adoro!')
elif resposta == 'nao':
    print('Fico triste com essa resposta... :(')

'''
Com a depuração, percebemos que ao executar o código, nossa lógica utilizada
na linha 5 (definição do loop while) está errada, pois utilizamos o operador lógico OR.
Ou seja, o loop será executado caso a resposta do usuário seja diferente de "sim" OU diferente de "nao".

Akém disso, para checarmos se ambas variáveis são corretas, temos que escrever o nome da variável novamente antes da condicional.
EVITE ISSO:

while resposta != 'sim' or 'nao':

BUSQUE POR ISSO:
        
             ↓↓↓↓                   ↓↓↓↓
while (resposta != 'sim') or (resposta != 'nao'):

Como na linha abaixo, se o usuário inserir a resposta "nao":
                
            condição 1: True        OU      condição 2: False       Com o OR: True + False = True = Loop iniciado
while       resposta != 'sim'       or      resposta != 'nao':

Como a primeira condição é verdadeira, entramos no nosso loop, pois o operador OR executa o loop
caso QUALQUER UMA condição seja verdadeira, sendo que queremos que nosso código de loop execute caso
AS DUAS condições sejam verdadeiras (se o usuário inserir uma resposta que seja diferente de "sim" E de "nao")
E para isso utilizamos o AND. Caso o usuário insira "nao":


            condição 1: True         E      condição 2: False      Com o AND: True + False = False = Loop evitado
while       resposta != 'sim'       and     resposta != nao

Assim, caso o usuário digite "nao" ou "sim" uma das condições que definimos será falsa, não entrando no erro
que está dentro do nosso loop, corrigindo o código.
'''
# Código correto:
resposta = input('Você gosta de programação? (sim/nao): ')

#         condição 1       E       condição 2       Se AMBAS forem verdadeiras, entre no loop
while (resposta != 'sim') and (resposta != 'nao'):

    print('Resposta inválida! Responda com "sim" ou "nao"')
    resposta = input('Você gosta de programação?: ') 

# Com as respostas validadas (sendo "sim" ou "nao"), saia do loop e venha para os ifs:
if resposta == 'sim':
    print('Legal, você é dos meus!')
elif resposta == 'nao':
    print('Fico triste com essa resposta... :(')
    
#==============================================================================================================================#
# Utilizando inputs de usuários dentro da função range:
numero_inicial = int(input('Qual o primeiro número pra percorrer: '))    # RANGE só opera com INT
numero_final = int(input('Até onde quer percorrer: '))                   # RANGE só opera com INT
passadas = int(input('De quantos em quantos números você quer pular: ')) # RANGE só opera com INT

for numero in range(numero_inicial, numero_final, passadas):
    # caso o número seja par, printar numero
    if numero % 2 == 0: 
        print(numero)
    # caso seja impar, printar mensagem
    else:
        print('Numero impar')

# EXEMPLO DE USO DE WHILE EM UM QUIZ:
while True:
    quiz = int(input('Quanto é 10 + 10? '))
    # se a resposta for correta, print a mensagem e FINALIZE o loop
    if quiz == 20:
        print('Resposta correta')
        break
    # caso contrário, printe a mensagem e REINICIE o loop, até a resposta ser correta
    else:
        print('Resposta errada, tente novamente!')
