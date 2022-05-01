"""
funções (def) em python - (return) - parte 2

anotações:
funções sempre que chegam ao final retornam algum valor 
obs: mesmo sem colocar return no fim

sempre que a função encontrar a palavra return ela nao desce mais
nada abaixo do return da função será executado 

obs: se ao chamar a função não for usado os () ela não é executada

uma função pode retornar qualquer coisa em python
"""

def funcao(var):
    print(var)
    

# o corpo vai ser executado e quando chegar ao fim da função será retornado None

variavel = funcao('oi') # a variavel vai receber o valor do retorno da função   

if variavel:
    print(variavel) 
else:
    print('nenhum valor')    

# retornando o valor do argumento passado a var

def funcao(var):
    return var 

variavel = funcao('oi') 

if variavel:
    print(variavel) 
else:
    print('nenhum valor')    

# feito em aula...
# moral da história

# podemos usar o return para não executar o código abaixo dele, apenas se necessário

def divisao(a,b):
    if b == 0:  # sera checado se b é igual a zero e caso seja vai retornar None
        return  # se b for diferente de zero a função pula pra o segundo return 
    return a / b # e executa a divisão 

divide = divisao(8,4)

if divide:
    print(divide)
else:
    print('conta inválida')    
    

# uma função retornando outra função

def a(nome):
    return nome
    
def b():
    return a
var = b()  # var vai ser igual a função a ou seja var assume o valor da função a porque a função               
print(type(var)) # b tem como retorno o a função a

# logo podemos usar var como se fosse a

print(var('agora eu sou função kkkkkk'))

      