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
def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

count = count_letters('abacaxi')
print(count)