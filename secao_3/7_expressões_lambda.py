"""
expressões lambdas --> funções anonimas

usadas pra substituir funções normais que não tenham muito código

"""
# função normal


def func(a, b):
    return a * b


var = func(2, 2)
print(var)

# mesma função so que anonima
# usa uma var


a=lambda x, y:  x * y

print(a(2, 2))

# usando a expressão lambda para ordenar uma lista dentro de outra lista


lista = [
    ['p1', 20],
    ['p2', 8],
    ['p3', 7]
]
print(lista[1])
# não dar pra usar a func sort() pois o interpretador nao iria entender por se tratar de uma lista dentro de outra

# sendo necessário criar um func onde informa o indice do produto que esta dentro da segunda lista

lista.sort(key=lambda item:item[1]) # onde [1] esta indicando que se deva ordena pelo indice 1 da lista 2 ou seja
                                    # pelo preço do produto
print(lista)


