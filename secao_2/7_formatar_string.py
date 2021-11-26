"""
formatação de string
duas formas
fstrings
função formart
"""

nome = 'eudes sena'
idade = 24
altura = 1.67
e_maior = idade > 18
peso = 82
imc = peso / altura ** 2
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # :.valorf define a quantidade de casas decimais

print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))

print('{0} tem {1} anos de idade e seu imc é {2} {0} {1}'.format(nome, idade, imc))
# ordem de 0 há... colocando a numeração é possivel chamar a var em outro trecho do print usando {numero}

print('{n} tem {id} anos de idade e seu imc é {i}'.format(n=nome, id=idade, i=imc))
# usando parametros nomeados dentro das chaves para associar a var, dar pra fazer a mesma coisa que texto acima.
