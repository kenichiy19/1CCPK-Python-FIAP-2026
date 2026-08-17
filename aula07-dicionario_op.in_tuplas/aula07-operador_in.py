eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {'one': 'uno',
          'two': 'dos',
          'three': 'tres'
}

print(eng2sp)
print(eng2sp['two'])

# OPERADOR IN
# Ele acusa se algo aparecer como chave no dict
print('one' in eng2sp)

# values()
valores_dict = eng2sp.values()
print('one' in valores_dict)

print()

# EXEMPLPO

# Um dicionário como uma coleção de contadores

# Cada uma dessas opções executa o mesmo cálculo, mas o implementa de forma diferente.
# Uma implementação é um modo de executar um cálculo; algumas implementações sao melhores de outras.
# Por exemplo, uma vantagem da implementação de dicionário é que não precisamos saber de antemão quais letras aparecem na string e só é preciso criar espaço para as letras qye realmente venham a aparecer.

# CONTADOR
def count_letters(texto): # Define a função chamada 'count_letters' que recebe uma string 's' como parâmetro de entrada
    frequencia = dict() # Cria um dicionário vazio, onde as chaves serão as letras e os valores serão a quantidade de vezes que cada letra aparece.
    for letra in texto: # Percorre cada caractere 'c' presente na string 's', da esquerda para direita.
        if letra not in frequencia: # Verifica se a letra ainda não está registrada no dicionário.
            frequencia[letra] = 1 # Se for a primeira vez, ela é adicionada como chave com valor inicial 1.
        else: # Caso já esteja no dicionário, é adicionado +1 no seu contador.
            frequencia[letra] += 1
    return frequencia # Ao percorrer todos os caracteres, a função retorna o dicionário preenchido.

count = count_letters('abacaxi')
print(count)

# CONTADOR DE PALAVRAS
def count_words(texto):
    frequencia2 = dict()
    palavras = texto.split()

    for palavra in palavras:
        if palavra not in frequencia2:
            frequencia2[palavra] = 1
        else:
            frequencia2[palavra] += 1
    return frequencia2

frase = "o gato pulou o muro e o gato correu"
contagem = count_words(frase)
print(contagem)
