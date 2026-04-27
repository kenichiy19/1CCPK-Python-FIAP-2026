# ATIVIDADE 02

# Parte 2 - depois da função

def verificar_nota (nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10!")
        nota = float(input("Digite novamente: "))
    return nota # quando atinge o requisito, retorna o valor

notaA = float(input("Digite a primeira nota: "))
notaA = verificar_nota(notaA) # aqui ele atualiza a variável notaA. (antes ele era um valor, mas depois da verificação, o valor precisa ser atualizado)


notaB = float(input("Digite a segunda nota: "))
notaB = verificar_nota(notaB)

# É perceptível que as estruturas de while se repetem nas duas variáveis, logo, usar uma função deixa mais otimizado.

media = (notaA + notaB) / 2
print(media) # Aqui, ele valida até números negativos, dando resultados incoerentes. (aceitando -100 como nota do aluno)

# Parte 1 - antes de função
notaA = float(input("Digite a primeira nota: "))
while notaA < 0 or notaA > 10:
    print("A nota deve estar entre 0 e 10!")
    notaA = float(input("Digite novamente: "))


notaB = float(input("Digite a segunda nota: "))
while notaB < 0 or notaB > 10:
    print("A nota deve estar entre 0 e 10!")
    notaB = float(input("Digite novamente: "))

# É perceptível que as estruturas de while se repetem nas duas variáveis, logo, usar uma função deixa mais otimizado.

media = (notaA + notaB) / 2
print(media) # Aqui, ele valida até números negativos, dando resultados incoerentes. (aceitando -100 como nota do aluno)
