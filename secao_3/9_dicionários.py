"""
Dicionários em python

 é um estrutura de dados que suporta um par chave e valor {chave:valor, chave:valor, ....}
 
 chave é o 'indice do dicionário'
 
similar a lista a diferança é que na lista o python gera os indices automaticamente e nos dicionários
nós podemos gerar os indices (que são as chaves)

ex: d = { chave(indice) : valor }

estrutura iterável

chaves dentro do dicionário precisam ser únicas

caso sejam repetidas o valor da ultima chave que vai ser acessado

d = {'c1': 8, 'c1': 7}

print(d[c1]) --> saida vai ser 7

possivel usar qualquer tipo de dados imutável para definir chaves

ex: str, numeros, tuplas






"""

# criando um dicionário 

d1 = {'chave1': 'valor chave 1'}





# adicionando uma nova chave/valor

d1['chave2'] = 'valor chave 2'

# adicionando com a função update

# update recebe um dicionario como parametro podendo colocar várias chaves/valor

d1.update({'chave3': 'valor da chave 3'})

# atualizando o valor de uma chave

d1['chave1'] = 'valor 1' # chave1 de d1 vai ter  'valor da chave 1' substituido por 'valor 1'

# usando o update para atualizar o valor de uma chave

d1.update({'chave2':  'valor 2'}) # chave1 de d1 vai ter  'valor da chave 2' substituido por 'valor 2'


# outra forma de construir dicionário

d = dict(chave1='valor1', chave2='valor2' )

# fazendo verificação caso busque uma chave que não existe

d = {'c1': 2, 'c2': 3}


print(d['c3'])  # chave não existente nesse dic, vai gerar um key error e não vai executar a linha abaixo

print('olá') # linha não será executada

# SOLUÇÕES...

if 'c3' in d:  # verificação se chave existe
    print(d['c3'])

print('olá')

if 'c3' not in d: # criando chave caso nao exista
    d['c3'] = 4
print(d['c3']) # printando o valor da chave criada acima


# busca de chave pela função get
# o get vai retornar um valor None caso a chave não exista dentro do dic

a = d.get('c4')
print(a)

# usando o if para verificação no get

if d.get('c4') is not None: # se o retorno de get nao for None será printado o valor da chave
    print(d['c4'])

# excluindo chaves no dic função del

del d['c3'] # apaga a chave 'c3' e seu devido valor


# checando chaves e valores de um dicionarios

dic = {
    
    'chave1': 7,
    'chave2': 8,
    'chave3': 9
}


# checando a chave 

print('chave4' in dic) # retorna false
# ou
print('chave4' in dic.keys()) # retorna false

# checando o valor da chave

print(7 in dic.values() )  # retorna true    


# iterando em dicionarios

# iterando nas chaves

dic = {
    
    'chave1': 7,
    'chave2': 8,
    'chave3': 9
}

for k in dic:
    print(k)
    
 # ou
 
for k in dic.keys():
     print(k)   

# iterando nos valores

for v in dic.values():
    print(v)    

# iterando em chave e valor ao mesmo tempo

for k in dic.items(): # saida gera uma tupla com chave/valor
    print(k)    
    
# iterando usando duas var no for

for k, v in dic.items():
    print(k, v)  # saida normal sem ser tupla
    
# copiando um dicionário

# obs: usar o operador = não está copiando um dic e sim fazendo uma referência

nv_dic = dic # forma errada
nv_dic['chave1'] = 10 # nv_dic e dic vão ser alterados

# usando a função copy

nv_dic = dic.copy() # copia rasa shallow copy
nv_dic['chave1'] = 10 # apenas o nv_dic vai ser alterado mas se houver algum tipo de dado mutavel dentro do dic, ex uma lista
# vai ser alterado no nv_dic e no dic da mesma maneira

# copiando com um modulo importado jeito correto de copiar

import copy

nv_dic = copy.deepcopy(dic) # jeito certo

# concatenando dicionarios

d1 = {
    'a' : 1,
    'b' : 2 
}

d2 = {
    'c': 3,
    'd': 4
}

d1.update(d2) # jeito usado
print(d1)

### feito na aula

clientes = {
    'cliente_1':{
        
        'nome': 'eudes',
        'sb': 'sena'
    },
    
    'cliente_2': {
        
        'nome': 'luiza',
        'sb': 'moura'
        
    }
}    

for clientes_k, clientes_v in clientes.items():
    print(f'exibindo {clientes_k}')
    
    for dados_k, dados_v in clientes_k.items():
        print(f'\t {dados_k} = {dados_v}')
        