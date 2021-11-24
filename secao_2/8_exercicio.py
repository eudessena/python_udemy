nome = 'eudes sena'
idade = 24
altura = 1.67
peso = 82.0
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2
print(f'{nome} nasceu no ano de {ano_nascimento} e tem o imc de {imc:.2f}')
print('{} nasceu no ano de {} e tem o imc de {:.2f}'.format(nome, ano_nascimento, imc))
print('{0} nasceu no ano de {1} e tem o imc de {2:.2f}'.format(nome, ano_nascimento, imc))
print('{n} nasceu no ano de {a} e tem o imc de {i:.2f}'.format(n=nome, a=ano_nascimento, i=imc))


print("'eudes")

