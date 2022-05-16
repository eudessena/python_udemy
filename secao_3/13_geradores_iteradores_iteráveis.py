"""
geradores, iteradores e iteráveis

um iteravel é um objeto que se pode iterar sobre ele mas nao necessáriamente é um iterador
um iterador retorna um valor de cada vez  

iteradores tem o metodo next
iteraveis tem o metodo iter   

"""

# objeto iterável

l = [1,2,3,4,5]
print(hasattr(l, '__iter__')) # função hasattr retorna se o objeto é iteravel
                              # recebe dois parametros, o objeto + o metodo '__iter__

# checando se a lista é um iterador  
print(hasattr(l, '__next__')) #recebe dois parametros, o objeto + o metodo '__next__
                              
# iterador

for v in l:  # o for transforma o objeto iterável em um iterador    
    print(v)     



         





