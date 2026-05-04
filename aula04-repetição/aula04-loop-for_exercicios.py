# ATIVIDADE 05

lista = list(map(int, input("Digite os 5 numeros: ").split()))
maior = 0

for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]


print(maior)


# ATIVIDADE 03

quant_musica = int(input("Digite a quantidade de músicas da sua playlist(DB): "))

for i in range(quant_musica):
    print(f"Música {i}")



for i in range(0, 4):
    for j in range(0, 3, 2):
        print(f"i: {i}, j: {j}")