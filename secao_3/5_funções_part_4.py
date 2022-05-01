'''
funções parte 4 

escopo de variável

local e global

'''

var = 'hello' # escopo global


def aff():
    var = 'help' # (é uma nova variavel mesmo tendo o mesmo nome da global, nao esta sendo
    # modificado o valor da global, esta sendo criada uma var local )
    print(var)
    
def afff():
    print(var) # esta sendo acessado pq var é global    


afff() # saida global
aff()  # saida local   