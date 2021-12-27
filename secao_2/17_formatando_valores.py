"""
formatando valores com modificadores

:s --> strings
:d --> inteiros
:f --> float
:.(numero)f --> numero de casas decimais

: (caractere) ( < ou > ou ^) (quantidade )(tipo --> s,d,f)

o que vc quer que seja adicionado + onde + quantidade menos o valor da var

onde o vai ser adicionado as casas

> --> esquerda
< --> direita
^ --> centro

explicando...

define a quantidade de casas que uma determinada var terá e caso nao seja toda completada é pre definido um complete

ex:

a = 1
print(f'{a:0<10}')

eu to dizendo que a var A vai ter 10 casas mas nesse caso A so tem uma casa entao será completado por
por 9 zeros a direita do valor de A

a = 1
print(f'{a:0<10.2f}')

dar combinar com outro tipo de formatação nesse exemplo esta combinado com o de casas decimais

"""

a = 10
b = 3

d = a / b
print('{:.2f}'.format(d))  # formatando a quantidade de casas decimais com o format


a = 10
b = 3

d = a / b
print(f'{d:.2f}')  # formatando a quantidade de casas decimais com o fstring


a = 1
print(f'{a:0<10}')

a = 1
print(f'{a:0<10.2f}')


# com string

a = 'eudes'
print(f'{a:#^50}')  # to dizendo que minha var vai ter 50 casas e que onde subtraido pelo valor da var a diferença vai
# vai ser preenchida por cerquilha

a = 'eudes'
print('{:#^50}'.format(a))


print(a.title())  # primeiras letras maisculas
print(a.lower())  # tudo minusculo
print(a.upper())  # tudo maiusculo
