# ------------ FOR -------------------------
for contador_musica in range(3):
    print(f"Música {contador_musica}")

    # de 1 até 11, pulando de 2 em 2
    # for (let i = 1; i < 12; i += 2) em JavaScript

for i in range(1, 12, 2): # inicio, final, de 2 em 2
    print(i)


# ------------ WHILE -----------------------
cp = 0
while cp < 10:
    cp += 1

    if cp == 3:
        continue # ignora tudo que está abaixo e volta para o início. (tipo um filtro)

    if cp == 7:
        break # quebra o loop e prossegue com o código.

    print(f"Produto {cp}")

    # while decrescente de 4 até 1

i = 4
while i > 0:
    print(i)
    i -= 1