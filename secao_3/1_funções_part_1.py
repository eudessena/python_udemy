"""
funções (def) em python ( parte 1 )

anotações:

as funções são criadas pra vocẽ não repetir as coisas
as funções podem receber parametros
os parametros sao var
funções com parametros devem receber argumentos/valor

"""
# definindo a função

def funcao():
   print("oi ")   
# chamando a função

funcao()    

# função com parametro

def name(nome):
    print(nome)

# ao chamar a função nome tenho que passar o argumento/valor do parametro nome

name('eudes sena')


# deixando um valor padrão para o parametro caso não seja enviado nenhum argumento na hora de
# chamar a função, evitando assim um erro na execução

def name(nome='eudes'):
    print(nome)

name()  # se eu nao passar argumento na chamada da função a mesma vai assumir o argumento/valor 
        # pre definido no parametro.  
        

# obs: os parametros devem receber os argumentos de forma posicionais em ordem

def teste(idade,nome):
    print(idade,nome)
 
teste('eudes', 24) # aqui o parametro idade vai receber nome e o nome vai receber idade
                   # ou seja esta errado
teste(24, 'eudes')  # jeito certo

# obs: se uma função tem N parametros ao chamar a função todos esse parametros devem ser 
# satisfeitos pelos argumentos/valor                    


# quebrando essa regra da ordem

# argumentos nomeados

def teste(idade,nome):
    print(idade,nome)
    
teste(nome='eudes', idade=24)  # invertendo a ordem dos parametros na hora de passar or argumentos 

# função feita na aula

def saudacao(msg='olá', nome='eudes sena'):
    msg.replace('l', '5')  # função replace troca uma coisa por outra
    nome.replace('s', '5')
    return f'{msg} {nome}'

variavel = saudacao()  # essa var ta recebendo o retorno da função

print(variavel)                     