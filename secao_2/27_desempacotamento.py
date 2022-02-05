"""
desempacotamento de listas em python

"""

lista = ["eudes", "solange", "lara", "rozangela"]

n1, n2, n3, n4 = lista 

# python associa cada valor da lista a uma variavel em ordem
# obs: a quantidade de variavel nao pode ser menor que a quantidade valores da lista

n1, n2, = lista # retorna erro

# resolvendo

n1, n2, *outra = lista 

# ao colocar * + qualquer_nome
# o valor que nao esta sendo desempacotado ta sendo gerado uma nova lista
# ou seja o valor "lara" e "rozangela" esta sendo lançado em "*outra" e sendo gerado
# uma nova lista so com esses valores 


# pegando o ultimo valor da lista tbm

n1, n2, *outra, qualquer_nome = lista

# essa var ultima var vai receber o ultimo valor da lista


# pegando os 2 ultimos valores da lista

*outra, n1, n2 = lista



