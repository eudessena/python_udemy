"""
laço while

utilizado para realizar ações ENQUANTO uma condição for verdadeira


"""

x = 0

while x < 10:
    print(x)
    x = x + 1

# continue --> ele não vai mais executar as linhas posteriores a palavra continue..

# ex

x = 0

while x < 8:
    if x == 3:
        x = x + 1
        continue  # vai pular o numero 3

    print(x)
    x = x + 1
print('acabou')

# break --> finaliza o loop

x = 0
while x < 10:
    if x == 3:
        print(x)
        break
    print(x)
    x += 1  # x = x + 1
print('acabou')


# simulando um laço que percorre linhas e colunas

x = 0

while x < 10:
    y = 0
    while y < 5:
        print(f'({x},{y})')
        y += 1
    x += 1
print('fim')
# a cada ciclo do X o Y vai repetir até Y menor que 5


