# TUPLAS SÃO IMUTÁVEIS

t = ('a', 'b', 'c', 'd', 'e')
print(t[0])

# Tupla de um único elemento
t1 = 'a',
print(type(t1))

t = tuple() # tupla vazia

t = tuple('texto')
print(t)
print(t[1:3])

# Como tuplas são imutáveis, você não pode alterar os elementos.
# Mas você pode substituir um tupla com outra.

t = ('T',) + t[1:] # Adiciona T e completa com a primeira tupla 'tuple()' a partir do elemento t[1] = 'e'
print(t)

# Versão A
a = 5
b = 10
print(f"a: {b}, b: {a}")

temp = a
a = b
b = temp
print(f"a: {b}, b: {a}")

# Versão B
a = 5
b = 10
print(f"a: {b}, b: {a}")

a, b = b, a
print(f"a: {b}, b: {a}")

# Separação de e-mails
email = 'user@gmail.com' # Aqui vemos que temos duas partes, o 'usuário' e o 'domínio' separados pelo '@'
username, domain = email.split('@')

print(username, domain)

