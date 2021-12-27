# desafio 1

numero = input('informe um numero: ')

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar!')
else:
    print(f'{numero} isso não é um numero inteiro')
# desafio 2

horario = input('informe o horário atual')
if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print("informe um horário entre 0 e 23")
    else:
        if horario <= 11:
            print('bom dia')
        elif horario <= 17:
            print("boa tarde")
        else:
            print('boa noite!')
else:
    print(f'{horario} formato inválido')

# desafio 3

nome = input('informe seu nome: ')

if len(nome) <= 4:
    print(f'seu nome é {nome} e ele é curto')
elif len(nome) <= 6:
    print(f'seu nome é {nome} e tem um tamanho normal')
else:
    print('seu nome é {} e tem um tamanho grande'.format(nome))





