"""
while / else

contadores e acumuladores


"""

contador = 1
acumulador = 0
while contador <= 5:

    if contador >= 2:
        break  # nesse caso o else não é executado porque a expressão não se tornou FALSE
    acumulador += contador  # somando o todos os numeros do laço, acumulando o valor
    contador += 1
else:  # quando a expressão do bloco while for FALSE o bloco ELSE vai ser executado
    print(acumulador)

print('porém isso seria executado')
