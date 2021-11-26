"""
documentação e built-in utéis



"""

# caso o user digite um tipo nao numerico
# funções isnumeric isdigit isdecimal --> que dizem se uma string pode ser convertida pra numero (int,float)
# essa funções tem um problema pois so checam numero inteiros e positivos

# essa resolução tem um problema porque se for digitado algum float ele nao vai entender
a = input('n1')
b = input('n2')

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    print(a + b)
else:
    print('erro')

# corrigindo

a = input('n1')
b = input('n2')

try: # to dizendo.. tenta fazer isso
    a = int(a)
    b = int(b)
    print(a + b)
except: # caso nao consiga, faça isso
    print('erro')
