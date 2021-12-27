"""
indices

0123456789...........33

elementos com indice sao iteraveis
"""

frase = 'o rato roeu a roupa do rei de roma'
tam_frase = len(frase)
cont = 0
while cont <= tam_frase:
    print(frase[cont], cont)
    cont += 1

# adicionado o valor de uma string em uma nova string
frase = 'o rato roeu a roupa do rei de roma'
tam_frase = len(frase)
cont = 0
nv_str = ''
while cont <= tam_frase:
    nv_str += frase[cont]
    print(nv_str)
    cont += 1
else:
    print(nv_str)

# adicionado o valor de uma string em uma nova string, fazendo verificação da letra 'r' e alterando pra maiuscula
frase = 'o rato roeu a roupa do rei de roma'
tam_frase = len(frase)
cont = 0
nv_str = ''
while cont <= tam_frase:
    letra = frase[cont]
    if letra == "r":
        nv_str += "R"
    else:
        nv_str += letra
    cont += 1
print(nv_str)
