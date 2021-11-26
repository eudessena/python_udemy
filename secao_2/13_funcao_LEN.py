"""
contar a quantidade de caractere de uma string
obs: espaços tbm são considerados
função LEN --> não funciona com tipos numéricos
porem o seu retorno é um valor de tipo inteiro ou seja pode fazer operações encima de seu retorno

obs aula --> em python tudo é um objeto ou seja tudo tem metodos atrelados a ele

"""

user = input('informe seu usuário: ')
qtd_caract = len(user)
print(qtd_caract)

if qtd_caract < 7:
    print("digite pelo menos 7 caractere")
else:
    print('cadastro efetuado')

