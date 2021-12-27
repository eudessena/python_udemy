"""
for in python

iterando em string com for

função built in range ( start=0, stop, step=1 )

utilizado para coisas que finitas
"""

texto = "eudes"

for letra in texto:
    print(letra)

# para cada letra em texto mostre a letra
# obs: a var "letra" pode ser qualquer outro nome

for n in range(10):
    print(n)
# retorna uma lista de numeros de 0 a 10 - 1


text2 = 'eudes sena'
nv_name = ''
for l in text2:
    if l == 'e':
        nv_name += l.upper()
    elif l == 's':
        nv_name += l.upper()
    else:
        nv_name += l
print(nv_name)

# usando for em string e alterando as propriedades de algumas letras
