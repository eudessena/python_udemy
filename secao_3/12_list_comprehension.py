"""
List Comprehension em Python

usado para...

otimização/perfomance
menor escrita


"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# iterando usando list comp

ex1 = [var for var in l]  # ex1 vai ser igual a l
print(ex1)

# multiplicando cada elemento da lista

ex2 = [v * 2 for v in l]  # ex2 vai conter cada valor de l multiplicado por 2
print(ex2)

# criando uma tupla pra cada elemento

ex3 = [(v,) for v in l]
print(ex3)

# saida
# [(1,), (2,), (3,), (4,), (5,), (6,), (7,), (8,), (9,)]

# multiplicando cada elemento da lista colocando um numero a mais em cada tupla gerada

ex3 = [(v, v2) for v in l for v2 in range(1)]
print(ex3)

# saida 
# [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0)]

# usando a função replace

l1 = ['eudes', "luiza,", "solange", "lara"]

ex4 = [v.replace('a', '@') for v in l1]
print(ex4)


# vendo valores divisiveis por 2 e por 8 em um intervalo de 0 a 99

l3 = list(range(100))
ex5 = [v for v in l3 if v % 2 == 0 if v % 8 == 0] 
print(ex5)