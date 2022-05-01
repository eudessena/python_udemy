# crie uma função qie ecibe uma saudação com os parametros saudação e nome.

def saudacao(saudacao='ola',nome='humano'):
    print(saudacao, nome)

saudacao('oi', 'eudes')

# crie um função que recebe 3 números como parametros e exiba a soma entre eles

def soma(n1,n2,n3):
    return n1 + n2 + n3

print(soma(1,2,4))    

# crie uma função que recebe dois numeros. o primeiro é um valor e o segundo um percentual(ex: 10%)
# retorne o valor do primeiro numero somado do aumento do percentual do mesmo.

def number(n1,n2):
    n2 * (n2/100)
    a = n1  + n2
    return a

valor = number(100,10)
print(valor)

# fizz buzz - se o parametro da função for divisivel por 2, retorne fizz, se o parametro da função
# for divisivel por 5, retorne buzz. se o parametro da função for divisivel por 5 e 3 retorne 
# fizzbuzz, caso contrario, retorne o numero enviado.

def fb(num):
    if num % 2 == 0 and num % 5 == 0:
        fizzbuzz = f'{num} is divisible by 2 and 5'
        return fizzbuzz
    if num % 2 == 0:
        fizz = f'{num} is divisible by 2'
        return fizz
    if num % 5 == 0:
        buzz = f'{num} is divisible by 5'
        return buzz
    
    return f'{num} is not divisible by 2 not for 5'
    
value = fb (17)
print(value)     
        