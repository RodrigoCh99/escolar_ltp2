# função para validar o login:
def get_idlogin(cursor, login, senha):
    # executar o select:
    cursor.execute(f'select idlogin from login where login = "{login}" and senha = "{senha}" ')

    # recuperando 1 retorno do BD
    idlogin = cursor.fetchone()

    # Fechar o cursor
    cursor.close()

    # retorno do Idlogin
    return idlogin[0]

def get_notas(cursor, idlogin):
    # Executar o SQL
    cursor.execute(f'select disciplinas.nome , notas.nota1, notas.nota2, notas.nota3, disciplinas.iddisciplinas from disciplinas, notas where notas.idlogin = "{ idlogin }" and notas.iddisciplinas = disciplinas.iddisciplinas')

    # recuperando os retornos do BD
    disciplinas = cursor.fetchall()

    print(disciplinas)

    # Fechar o cursor
    cursor.close()

    # retorno das disciplinas
    return disciplinas


def get_detalhes(cursor, iddisciplinas):
    # Executar o SQL
    cursor.execute(f'select disciplinas.nome, disciplinas.descricao from disciplinas where iddisciplinas = "{ iddisciplinas }"')

    # recuperando os retornos do BD
    detalhes = cursor.fetchall()

    print(detalhes)

    # Fechar o cursor
    cursor.close()

    # retorno das disciplinas
    return detalhes