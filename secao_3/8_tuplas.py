"""
tuplas em python

parecida com lista "porém não se pode editar os elementos" (adicionar,remover, modificar o valor de um indice) - imutáveis
estrutura iterável (for, while)
aceita diferentes tipos da dados
valores acessados por indices
possivel criar sem paranteses ou seja o que indica ser uma tupla é a virgula apos o valor

"""


from typing import List


tupla = ('eudes', 1, 2, 3, 4)
print(type(tupla))

# iteração
for t in tupla:
    print(t)

# fatiamento
print(tupla[2:]) # indica pegar do indice 2 ate o fim da tupla

# sem parenteses

tupla1 = 1, 2, 3, 4, 'a'

# tupla vazia
t = ()

# tupla de um elemento

t = 1, # necessario usar a virgula 

# concatenando tuplas

t1 = 1, 2, 3
t2 = 4, 5, 6
t3 = t1 + t2
print(t3)

# desempacotando tuplas

t1 = 1, 2, 3

v1, v2, v3 = t1

print(v1, v2, v3)

# o restante dos valores vai pra *_

t1 = 1, 2, 3, 4

v1, v2, *_ = t1

print(v1, v2)

# multiplicando uma tupla

t = ('e') * 7  # o valor dentro da tupla vai ser multiplicado 7 vezes

# converter tupla em lista

t1 = 1, 2, 3, 4 
t1 = list(t1)

# convertendo em tupla novamente

t1 = tuple(t1)

"""
maceteee

se quiser alterar os dados de uma tupla so converter em uma lista e depois converter novamente em tupla

t = (1, 2, 3, 4, 5)

t = list(t) # passar o iterável dentro do parenteses
t[1] = 7  # to alterando o valor 2 por 7
t = tuple(t)

saidaaa

(1, 7, 3, 4, 5)


apredizados gerais


estruturas com indices sao acessados por colchetes

ex: lista = [1, 2, 3]
    tupla = (1, 2, 3)
    
    acessando....
    
    l = lista[1] --> saida numero 2
    t = tupla[2] --> saida numero 3



 
"""





    
    