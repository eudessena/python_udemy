"""
entrada de dados do usuário

input() --- recebe o dado em formato de string

"""

nome = input('qual o seu nome? ')
# o que for digitado sera atribuido na var nome em formato de string
print(f'o usuário digitou {nome} ' f' {type(nome)}')


# EXemplos do casting para receber os dados via input e onverter para o tipo de dado desejado

idade = input('informe sua idade: ')
ano_nasc = 2021 - int(idade)
# ouuuuuuuu
idade = int(input('informe sua idade: '))
ano_nasc = 2021 - idade


