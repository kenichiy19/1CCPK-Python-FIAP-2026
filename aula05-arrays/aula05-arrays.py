nome = ["Max", "Bob", "Carlos", "Ana"]

for i in range(len(nome)):
    for j in range(i + 1, len(nome)):
        print(nome[i], nome[j])
