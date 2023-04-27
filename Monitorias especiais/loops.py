# # Pegando input do usuário:
resposta = float(input('Quanto é 10 + 10? '))

# # Checando resposta:
if resposta == 20:
    print('Resposta Correta! 10 + 10 é igual a 20.')
else:
    print(f'Resposta errada! 10 + 10 não é igual a {resposta}')
#=========================================================================================================
# LOOP WHILE:
resposta = float(input('Quanto é 10 + 10? '))

while resposta != 20:
    resposta = float(input('Quanto é 10 + 10? '))

while True: #Ao executar o código, entre no loop:
    # Faça a pergunta
    resposta = float(input('Quanto é 10 + 10? '))

    # SE a resposta for errada:
    if resposta == 20:
        print('Certo.')
        break
    else:
        print('Errado!')
        continue
#=========================================================================================================
# LOOP FOR
for numero in range(0, 10, 2):
    print(numero)

for numero in range(0, 20):
    if numero % 2 == 0:
        print(numero)