# Você foi contratado para criar um pequeno sistema que analisa uma lista de endereços de e-mail de alunos da FIAP e gera um relatório.

# O programa deve:
# 1. Criar uma tupla com todos os nomes de usuário e exibir o primeiro e o último.
# 2. Trocar a ordem do primeiro e o último nome de usuário usando atribuição de tupla (sem variação temporária).
# 3. Exibir o relatório final, por exemplo:
    # RELATÓRIO:
        # Quantidade de e-mails por domínio:
        # fiap.com.br: 3
        # Lista de usuários: ("ana.paula", "joao.silva", "maria.souza")
        # Após trocas de posições: ("maria.souza", "joao.silva", "ana.paula")

lista_email = ("gabriel.zappelloni@fiap.com.br",
               "maykon.silva@fiap.com.br",
               "kenichi.yamamoto@fiap.com.br",
               "rodger.rios@fiap.com.br",
               "felipe.pereira@fiap.com.br"
)

usuarios = []
contagem_dominios = dict()

for email in lista_email:
    usuario, dominio = email.split('@')
    usuarios.append(usuario)

    if dominio not in contagem_dominios:
        contagem_dominios[dominio] = 1
    else:
        contagem_dominios[dominio] += 1

tupla_usuarios = tuple(usuarios)

lista_para_troca = list(tupla_usuarios)
lista_para_troca[0], lista_para_troca[-1] = lista_para_troca[-1], lista_para_troca[0]
tupla_trocada = tuple(lista_para_troca)

print("Relatório:")
print("Quantidade de e-mails por domínio:")
for dom, qtd in contagem_dominios.items():
    print(f" * {dom}: {qtd}")

print(f" * Lista de usuários: {tupla_usuarios}")
print(f" * Após troca de posições: {tupla_trocada}")
