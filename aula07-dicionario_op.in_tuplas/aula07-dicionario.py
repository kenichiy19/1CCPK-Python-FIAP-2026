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

"dicionário = {chave: valor}"
dicionario = {'chave_1': 1,
              'chave_2': 2,
              'chave_3': 3,
}

print(dicionario)

# Vamos criar um conjunto de dados com informações de matrícula de um estudante. Os dados são os seguintes:
# matricula: 2000168933
# dia do cadastro: 25
# mês do cadastro: 10
# turma: 2E

cadastro = {'matricula': 2000268933,
            'dia_cadastro': 25,
            'mes_cadastro': 10,
            'turma': '2E'
}

print(cadastro)

# Como acessar os dados desse cadastro?
print(cadastro['matricula'])

# E se agora eu precisar atualizar algum dado do aluno?
cadastro['turma'] = '2G'
print(cadastro)

# E se agora eu precisar adicionar mais um dado?
cadastro['modalidade'] = 'EAD'
print(cadastro)