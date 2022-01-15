"""
listas em python ( lista é um tipo de dado )  a lista é iteravel
fatiamento
append, insert, pop, del, clear, extend, +
min max
range


obs: diferença da lista para variável é que a var so tem um valor(um tipo de dado) e a lista pode ter varios valores
(de varios tipos de dados )

var = "eudes sena"
lista = ["eudes sena", 7, True, 7.0.....]
"""


# indices
#        0  1  2  3  4
lista = [1, 2, 3, 4, 5]
# -      5  4  3  2  1


# alterando coisas na lista atraves de seu indice

l = ['hello','boy']
l[0] = 'ola'
print(l)

# fatiamento da lista "exibindo os 3 primeiros valores da lista"

l = ['hello','boy', 7, 8, 'bla bla bla']
print(l[0:3])  # obs: [0:3] o indice de parada no caso o '3' não é incluido ou seja é indice - 1

# algumas funções usadas na lista

#  função extend... funciona como extensão da lista, ex: l1 extende a l2

l1 = [1, 2, 3]  # juntando duas listas
l2 = [4, 5, 6]
l3 = l1 + l2
print(l3)
# ouuuuuuuuu
l1.extend(l2)
print(l1)

# função append insere um valor ao final da lista

l4 = [1, 2, 3, 4].append(5)
print(l4)

# função insert adiciona um valor a lista no indice que a gente desejar

l1 = [1, 2, 3]
l1.insert(0, 'e')  # to mandando adiciona no indice zero a string 'e'

# função pop apaga o ultimo elemento da lista

l1 = [1, 2, 3]
l1.pop() # vai apagar o 3

# função del apaga o elemento que passamos pelo indice

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del(l1[3:5]) # vai apagar o 4 e 5
print(l1)


# função max e min - sabendo qual o maioor e menor valor existente na lista

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(max(l1))
print(min(l1))


# usando a função range para criar uma lista

l5 = list(range(1,50))  # retorna uma lista com valores de 1 a 49
print(l5)