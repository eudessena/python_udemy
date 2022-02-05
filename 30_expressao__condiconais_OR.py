"""

expressões condicionais com o OR

"""

nome = input('digite seu nome')

if nome:
    print(nome)
else:
    print('vazio')    

# usando o OR

nome = input('digite seu nome')
print(nome or "vazio")  # o OR vai checar a expressão true e a primeira true que ele achar
                        # ele executa

print(nome or 0 or False or "hello") # vai executar o hello


# mais coisas

a = 0
b = None
c = False
d = {}
e = []
f = 22
g = "eudes"

variavel = a or b or c or d or e or f or g
print(variavel)

# embora 'f' e 'g' sejam verdadeira, ele vai parar na 'f' ou seja na primeira true que achar