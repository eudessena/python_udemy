"""

for / else em python.
break, continue

iterar --> passar sobre cada elemento do iterável

"""

var = ["eudes", "Sena", "barreto"]

for valor in var:
    if valor.lower().startswith('s'):
        print('coemaça com s ', valor)
    else:
        print('não começa com s', valor)    

 # função startswith --> testa se o valor de algum elemento começa com determinada letra   
 # a lower ta pegando o valor da string convertendo pra minuscula e logo em seguida a checagem
 # é realizada


bla = ['Hello', 'eudes', 'barreto']

palavra = False

for i in bla:
    if i.lower().startswith('h'):
        palavra = True
if palavra:
    print('existe a palavra com h')        
else:
    print('não existe palavra com h')

# usando o else no laço for

bla = ['Hello', 'eudes', 'barreto']


for i in bla:
    if i.lower().startswith('h'):
        break           
else:
    print('não existe palavra com h')    