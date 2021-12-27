"""
manipulando strings

* strings indices
* cada caratere de uma string tem um indice
* fatiamento de string (inicio:fim:passo)
* funções built-in len, abs, type, print, etc.....

documentação...
https://docs.python.org/3/library/stdtypes.html ( tipos built-in )
https://docs.python.org/3/library/functions.html ( funções built-n)


"""

texto = 'python s2'  # indices... [0 1 2 3 4 5 6 7 8] --> positivos
                     #             p y t h o n   s 2
# negativos                      -[9 8 7 6 5 4 3 2 1]
# acessando pelo indice [] --> a usar colchetes eu to dizendo para o interpretador do python que vou acesar o indice
print(texto[0])

# fatiamento string

nv_str = texto[2:6]  # vai printar do indice 2 ao indice 6 - 1
print(nv_str)

nn = "kskl7fsdsd"
print(nn[0:8:2])  # vai do zero ao fim da string pulando de 2 em 2

z = 'sena_sena'
print(z[:8])

