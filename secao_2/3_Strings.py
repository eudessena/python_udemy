"""
tudo em python é um objeto
string tipo primitivo em python
string(cadeia de caractere) no python - tudo que estiver entre aspas

caractere de escape

"""

print('hello, "sena"')  # melhor usar essa maneira
print("hello, 'eudes' ")
print("hello, \"eudes\" ")  # caractere de escape \ para o interpretador ignorar as aspas colocadas no eudes
print('hello, \'eudes\' ')   # não é legal usar carectere de escape, somente se for extremamente necessário

#  o interpretador ler a barra "\" como argumento

print('eudes \n sena')  # quebra de linha \n
print(r'eudes \n sena')  # o "r" diz para o interpretador nao executar nada dentro do que esta nas aspas do print,
# logo o \n nao será executado
