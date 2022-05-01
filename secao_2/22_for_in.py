"""
for in python

iterando em string com for

for ler iteráveis

iteráveis é algo que você pode percorrer

função built in range ( start=0, stop, step=1 )

utilizado para coisas que finitas

 frase = 'o rato roeu a roupa do rei de roma'
 
 for letra in frase:
     print(letra)
     
for lê algo que chamamos de "iterável" (do inglês iterable)... Um iterável é algo que você pode percorrer (geralmente tem índices, como a string - ou não, como generators)...
O que o for faz é solicitar ao iterador 
(que vamos aprender mais pra frente) da string: "Ei string, você tem um próximo valor?", e a string responde -> "Sim, aqui está" (letra) ou "Não, erro -> StopIteration".

O que "letra" é nesse código, é o valor que a string entrega na parte do "Sim". Isso ocorre repetidas vezes até o iterável 
(a string) falar que não tem mais valores. Nesse caso seu iterador (que vamos ver pra frente) vai levantar um erro (literalmente). Ao chegar na letra "a" 
final (de roma) o for vai solicitar mais um valor para a string. Nesse momento, como eles já acabaram, ela lança um erro chamado de StopIteration.
O for é programado, pelos desenvolvedores do Python, para capturar esse erro e parar as solicitações. Por esse motivo, nós não vemos erro e o for termina o código (
do contrário isso se tornaria um loop infinito).

A parte mais legal disso tudo, é que enquanto o for solicita o valor e recebe de volta algo da string (uma letra), ele nos permite fazer algo com esse valor.
Por exemplo, você fez "print(letra)", mas poderia ser qualquer outra coisa.     

"""

texto = "eudes"

for letra in texto:
    print(letra)

# para cada letra em texto mostre a letra
# obs: a var "letra" pode ser qualquer outro nome

for n in range(10):
    print(n)
# retorna uma lista de numeros de 0 a 10 - 1


text2 = 'eudes sena'
nv_name = ''
for l in text2:
    if l == 'e':
        nv_name += l.upper()
    elif l == 's':
        nv_name += l.upper()
    else:
        nv_name += l
print(nv_name)

# usando for em string e alterando as propriedades de algumas letras
