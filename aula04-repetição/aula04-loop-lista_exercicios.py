# ATIVIDADE 05
lista = list(map(int, input("Digite 5 números: ").split()))

for i in range(lista):
    if i > i + 1:
        i = i + 1

        print(i)


# ATIVIDADE 04
numeros = list(map(int, input("Digite 5 números: ").split()))

soma = sum(numeros)

print(soma)



# ATIVIDADE 03
numero = int(input("Digite o numero: "))
for tabuada in range(0, 26):
    print(numero * tabuada)


# print(numero x 1, numero x 2)

# ATIVIDADE 02
for i in range(0, 101, 10):
    print(i)

# ATIVIDADE 01
print("Olá, Mundo!")

escolha = input("Deseja repetir?: (sim/não): ")

while escolha == "sim":
    print("Olá, Mundo!")
    escolha = input("Deseja repetir?: (sim/não): ")

    if escolha == "não":
        break

print("Fim!")