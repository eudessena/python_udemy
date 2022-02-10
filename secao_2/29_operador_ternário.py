"""
operador ternária em python

"""
# sem operador ternário
logged_user = False

if logged_user:
    msg = 'user logado'
else:
    msg = 'user nao logado'

print(msg)        


# com operador ternário

logged_user = False

msg = "user logado" if logged_user else "user nao logado"

print(msg)


idade = 17

msg = 'pode acessar' if idade >= 18 else 'nao pode acessar'

print(msg)
