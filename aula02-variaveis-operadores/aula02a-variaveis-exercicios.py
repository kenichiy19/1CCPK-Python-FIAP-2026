# EXERCÍCIO 01

pi = 3.14159
raio = 5
area = pi*raio**2
areaA = round(area, 2) # round() é para arredondar os números

print(f"A área do círculo é igual a {areaA}.")

# EXERCÍCIO 02

TF = 212
TC = (TF - 32) * 5/9
TCa = round(TC, 1)

print(f"A temperatura é igual {TCa}°C.")

# EXERCÍCIO 03

livro = 25
caneta = 5
(total) = float((livro*3) + (caneta*2))
totalA = round(total, 2)
print(f"o gasto total foi de {totalA} reais")

# EXERCÍCIO 04

distancia = 150
vmedia = 60
tempo = distancia/vmedia
print(f"O tempo percorrido foi de aproximadamente {tempo} horas.")

# EXERCÍCIO 05

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
soma = nota1 + nota2
media = soma/2
mediaA = round(media, 2)

print(f"A sua média é igual a {mediaA}.")

# EXERCÍCIO 06

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
peso1 = int(input("Digite o peso da primeira nota: "))
peso2 = int(input("Digite o peso da segunda nota: "))

calculo1 = nota1*peso1
calculo2 = nota2*peso2

media = (calculo1 + calculo2)/(peso1 + peso2)
mediaA = round(media, 2)

print(f"A média da sua nota é igual a {mediaA}.")

# EXERCÍCIO 07

print("Bem-vindo(a)! Por favor, preencha o formulário!")

nome1 = input("Digite o nome do produto: ")
quant1 = int(input("Digite a quantidade requerida do produto: "))
valor1 = float(input("Digite o valor unitário do produto: "))
total1 = quant1*valor1
total1A = round(total1, 2)

print("Muito bem! Agora insira os dados do segundo produto!")

nome2 = input("Digite o nome do produto: ")
quant2 = int(input("Digite a quantidade requerida do produto: "))
valor2 = float(input("Digite o valor unitário do produto: "))
total2 = quant2*valor2
total2A = round(total2, 2)

total3 = total1A + total2A

print("Excelente! Aguarde um momento...")
print(f"O valor total a ser pago é igual a: R$ {total3}.")

# EXERCÍCIO 08

valorprod = float(input("Digite o valor do produto: "))
valorpago = float(input("Digite o valor pago pelo cliente: "))

troco = valorpago - valorprod

print(f"O troco da compra é igual a R$ {troco}.")















