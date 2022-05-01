"""
funções (def) em python ( *args, **kwargs )- parte 3

anotações:
argumentos

*args você não sabe quantos argumentos vai vir na função  geram tuplas
*kwargs sao argumentos com palavras chave geram dicionarios
obs: args e kwargs podem ser substituidos por qualquer coisa mas fica fora do padrao da comunidade python
"""

def f(a,b, c=None, d='bla'):
    print(a,b,c, d)
# obs: a partir do momento que eu seto um valor padrao de um parametro, os demais parametros 
# depois dele tem que ter valor padrão tambe, nesse caso 'd' em diante 

#  você não sabe quantos argumentos vai vir na função (*args)
# o *args é basicamente um empacotamento e desempacotamento
# estao empacotados em uma tupla
def f(*args):
    print(args)
    print(args[1]) # acessando o valor 2 de args
f (1,2,3) # vai ser printado esses valores empacotados dentro de uma tupla    


def a (*args):
    print(args)
# posso usar uma lista como parametro
lista = [1,2,3]
a(*lista) # o '*' indica que to passando a lista desempacotada 



# uso **kwargs

def b (*args, **kwargs):
    print(args) # pega os argumentos normais
    print(kwargs) # vai pegar so os argumentos nomeados
    print(kwargs['nome']) # acessando a chave nome que tem valor eudes
b(1,2,3,4, nome='eudes', k='hello')    