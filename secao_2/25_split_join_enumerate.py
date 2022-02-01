"""
split, join e enumerate em python

* split --> dividir a string  e gerar uma lista dessa string # str
* join --> juntar uma lista e gerar uma string # str
* enumerate --> enumerar elementos de uma lista # list / para objeto iteráveis

# mais conceito de iteráveis kkk
aquilo que você pode usar o FOR pra percorrer sobre ele

"""

string = "o brasil é o país do futebol, o brasil é penta."

lista = string.split(' ') # Argumento de separação na lista é o espaço nesse caso

print(lista)
# saida ["o", "brasil", "é", .....etc]

lista2 = string.split(',') # argumento de separação é a virgula
print(lista2)


# contando quantas vezes a palavra aparece 

for i in lista:
    print(f'a palavra {i} apareceu {lista.count(i)}x na frase')


nome = "eudes sena " 

print(nome.strip())  # função strip remove o espaço do inicio e fim da string


# função join

string = "o brasil é penta"
lista = string.split(' ')

string2 = " ".join(lista)  # o que está entre aspas é qual caratere vai ser usado na separaçao
                           # dos elementos da lista para formar a string



 # função enumerate

lista = ['noosa', 'mannn', 'nos que ta']

for v1, v2 in enumerate(lista):
    print(f"indice/numerador {v1} valor {v2}")

    # v1 ta pegando o indice do valor
    # v2 ta pegando o valor

# acessando uma lista dentro de outra lista
lista3 = [
   # 0  1  2  indices..... 
    [1, 2, 3], # 0
    [3, 4, 5], # 1
    [8, 6, 7]  # 2
]
for v1, v2 in lista3:
    print(v1, v2)

# por se tratar de listas dentro de lista temos o indices da lista "mae" e da lista "filha" 
# dai temos indices na vertical e horizontal

# ex acessar o numero 5 --> print(lista3[1][2])

