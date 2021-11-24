"""
Variáveis
regras -- iniciar com letras, pode conter números, separação por _ e usar letras minúsculas
definindo var -- nome + valor
"""

nome = 'eudes sena'
idade = 24
altura = 1.67
e_maior = idade > 18
peso = 82

print('nome:', nome)
print('idade:', idade)
print('altura:', altura)
print('é maior de idade:', e_maior)

imc = peso / altura ** 2
print(nome, "tem", idade, "anos de idade e seu imc é", imc)
