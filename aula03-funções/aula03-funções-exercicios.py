# EXERCÍCIO 10



# EXERCÍCIO 09
estado = int(input("Digite o código do estado de origem: "))
peso = float(input("Digite o peso em toneladas: "))
carga = int(input("Digite o código da carga: "))

pesokg = peso * 1000
print(f"O peso da carga é {pesokg} kg")
match carga:
    case preco if preco >= 10 and preco <= 20:
        preço = pesokg * 100
        print(f"O preço é de R$ {preço:.2f}")
    case preco if preco >= 21 and preco <= 30:
        preço = pesokg * 250
        print(f"O preço é de R$ {preço:.2f}")
    case preco if preco >= 31 and preco <= 40:
        preço = pesokg * 340
        print(f"O preço é de R$ {preço:.2f}")

match estado:
    case imposto if imposto == 1:
        imposto = preço * 0.35
        print(f"O valor do imposto é de R$ {imposto:.2f}")
    case imposto if imposto == 2:
        imposto = preço * 0.25
        print(f"O valor do imposto é de R$ {imposto:.2f}")
    case imposto if imposto == 3:
        imposto = preço * 0.15
        print(f"O valor do imposto é de R$ {imposto:.2f}")
    case imposto if imposto == 4:
        imposto = preço * 0.05
        print(f"O valor do imposto é de R$ {imposto:.2f}")
    case imposto if imposto == 5:
        imposto = preço * 0
        print(f"O valor do imposto é de R$ {imposto:.2f}")

total = preço + imposto
print(f"O valor total é igual a R$ {total:.2f}")

# EXERCÍCIO 08
salario = float(input())

if salario <= 280.0:
    bonus = salario * 0.2
    salario_novo = salario + bonus
    print(f"Seu salário antigo: R$ {salario:.2f}")
    print(f"Percentual do aumento aplicado: 20%")
    print(f"O valor do aumento: R$ {bonus:.2f}")
    print(f"Seu salário atual: R$ {salario_novo:.2f}")

if salario > 280.0 and salario <= 700:
    bonus = salario * 0.15
    salario_novo = salario + bonus
    print(f"Seu salário antigo: R$ {salario:.2f}")
    print(f"Percentual do aumento aplicado: 15%")
    print(f"O valor do aumento: R$ {bonus:.2f}")
    print(f"Seu salário atual: R$ {salario_novo:.2f}")

if salario > 700 and salario <= 1500:
    bonus = salario * 0.1
    salario_novo = salario + bonus
    print(f"Seu salário antigo: R$ {salario:.2f}")
    print(f"Percentual do aumento aplicado: 10%")
    print(f"O valor do aumento: R$ {bonus:.2f}")
    print(f"Seu salário atual: R$ {salario_novo:.2f}")

if salario > 1500:
    bonus = salario * 0.05
    salario_novo = salario + bonus
    print(f"Seu salário antigo: R$ {salario:.2f}")
    print(f"Percentual do aumento aplicado: 5%")
    print(f"O valor do aumento: R$ {bonus:.2f}")
    print(f"Seu salário atual: R$ {salario_novo:.2f}")

# EXERCÍCIO 07
nascimento = int(input())
idade = 2026 - nascimento

if idade >= 18:
    print(f"Seu voto é obrigatório esse ano! Você tem {idade} anos!")
elif idade >= 16 and idade < 18:
    print(f"Seu voto é opcional esse ano! Você tem {idade} anos!")
else:
    print(f"Seu voto é proibido esse ano! Você tem {idade} anos!")


# EXERCÍCIO 06
num_A = int(input())
num_B = int(input())
car_A = input()

match car_A:
    case "+":
        soma = num_A + num_B
        print("Sua soma deu:", soma)
    case "-":
        menos = num_A - num_B
        print("Sua subtração deu:", menos)
    case "*":
        mult = num_A * num_B
        print("Sua multiplicação deu:", mult)
    case "/":
        div = num_A / num_B
        print("Sua divisão deu:", div)


# EXERCÍCIO 05
A = int(input())
B = int(input())

if A > B:
    if A % B == 0:
        print("São multiplos!")
    else:
        print("Não são múltiplos!")

else:
    if B % A == 0:
        print("São multiplos!")
    else:
        print("Não são múltiplos!")

# EXERCÍCIO 04
notas = list(map(float, input().split()))
media = sum(notas)/len(notas)

if media >= 7:
    print("Aprovado! Sua média é:", media)
elif media >= 5 and media < 7:
    print("Em recuperação! Sua média é:", media)
else:
    print("Reprovado! Sua média é:", media)


# EXERCÍCIO 03
num_a = float(input())
num_b = float(input())

if num_a > num_b:
    print("Primeiro número é maior!")
elif num_a == num_b:
    print("Números iguais")
else:
    print("Segundo número é maior!")


# EXERCICIO 02
numero = int(input())

if numero%2 != 0:
    print("O número é ímpar!")

else:
    print("O número é par!")