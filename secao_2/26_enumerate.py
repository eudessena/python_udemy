"""
enumerate no python --> enumerar elementos da lista #LIST

lista é um conjunto de elementos e esses elementos tem indices
"""
# nesse caso temos indices na vertical e na horizontal
# lista dentro de lista, um lista ta sendo o valor de outra lista

lista = [

    ['eudes', 'francisco', 'barreto'],  # i dentro do indice 0 da lista mae tem o indice 0,1,2
                                        # da lista filha
                                        
    ['de', 'sena','solange'], # outro valor
    ['maria', 'barreto', 'mae'] # outro valor
]

# acessando o valor solange
print(lista[1][2])


enumerada = enumerate(lista)
print(enumerada) # retorna um objeto enumerate, podemos iterar sobre ele
# saida
# <enumerate object at 0x7f93f426e880>

print(list(enumerada))  # convertendo o meu objeto em uma lista

# saida 

# [ --> esse colchetes externos representam o objeto enumerate do qual geramos uma lista
# indices...
#    0  1  --> nesse caso o 0 e 1 vai ser pra todas as 3 tuplas
#   (0, ['eudes', 'francisco', 'barreto']), # 0  valores da lista mae 
#   (1, ['de', 'sena', 'solange']),  # 1
#          0     1        2
#   (2, ['maria', 'barreto', 'mae']).       # 2

# ]

# ex, acessar sena.
# enumerada = list(enumerate(lista))
# print(enumerada[1][1][1])


# enumerando lista

lista1 = [1,2,3,4,5,6,7]
for v1, v2 in enumerate(lista1, 10):  # to dizendo pra começar a enumerar do 10
    print(v1, v2)


 # mais sobre enumerate

lista2 = [1,2,3,4,5,6,7]   

for v1 in enumerate(lista2):
    valor_enumerado, valor_lista = v1
    print(valor_enumerado, valor_lista)

# desempacotando

for v1 in enumerate(lista2):
    valor_enumerado, valor_lista = v1
    n1, n2, n3 = valor_lista
    print(n1, n2, n3)

    # vai receber os 3 valores de cada lista filha 

