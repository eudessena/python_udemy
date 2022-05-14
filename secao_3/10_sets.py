"""
sets (conjuntos)

add (adiciona), update (atualiza), clear, discard
union | (une)
interserction & (todos os elementos presentes nos dois sets)
difference - (elementos apenas do set da esquerda)
symmetric_difference ^  (elementos que estão nos dois sets mas não em ambos)

parece com lista mas
sets so comportam elementos unicos, caso haja elementos repetidos {2,2,2,3} ele so considera {2,3}
não tem indice
pode iterar mas nao pode acessar o valor diretamente pelo indice

"""

# criando um set

s = {1,2,3,4,5}

# set vazio

s = set()

# adicionado valores

s.add(1) # so aceita um argumento
s.add(2)

# removendo valor

s.discard(2)


# update
 
# similar a add 
# diferença - ela recebe um iterável e itera sobre o valor ou seja
# se passar uma string "eudes" ela vai ser fatiada 
# so aceita valores iteraveis 
# obs: os sets não respeitam ordem, pode embaralhar as coisas
# Ex:
# s.update('python')
# saida --> 'n', 'y', 't', 'h', 'o', 'p' --> é um exemplo de como pode acontecer

s.update('eudes')

# convertendo lista em set

l = [1,1,1,1,2,2,2,3,3,3]
l = set(l) # ao converter todos os elementos repetidos da lista serão removidos

# função union
s1 = {1,2,3}
s2 = {1,2,3,4,5}

s3 = s1 | s2
print(s3)

#  função intersection

s1 = {1,2,3}
s2 = {1,2,3,4,5}

s3 = s1 & s2

print(s3)



#  função difference

s1 = {1,2,3, 7}
s2 = {1,2,3,4,5}

s3 = s1 - s2

print(s3)

#  função simetric difference

s1 = {1,2,3, 7}
s2 = {1,2,3,4,5}

s3 = s1 ^ s2

print(s3)

# feito em aula

l1 = [1,1,1,2,3,4,5]
l2 = [1,2,2,2,2,4,5]

# convertendo a lista em set e comparando ambas

l1 = list(set(l1))
l2 = list(set(l2)) # como se ler... to convertendo a lista em set e depois o set em lista

print(l1 == l2 )  # retorno true  

# comparando sem comprometer a lista

if set(l1) == set(l2):
    print('l1 é igual a l2')
else:
    print('diferente')    