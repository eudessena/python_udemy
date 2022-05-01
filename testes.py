def saudacao():
    return "olá Eudes"

def mestre(func):
    return func() # essa função tem a função de executar outras funções kkk
                  # a função ta recebendo outra função como argumento
results = mestre(saudacao)
print(results)



# 

def mestre1(func, *args, **kwargs):
    return func(*args, **kwargs)


def nome(nome):
    return f'Olá {nome}'

def saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

executando1 = mestre1(nome, "eudes")
executando2 = mestre1(saudacao, 'boa noite', 'seu lindo')

print(executando1)
print(executando2)

    
    
    

    





    

