import psycopg2


connection  = ''
connection_string = "dbname = 'Burguer Tycon' user = 'postgres' password = 'junior123' host = 'localhost'"



def conexao():
    return connection 


def select_com_retorno_geral (querry):
    connection = psycopg2.connect(connection_string)
    comando = querry
    cursor = connection.cursor()
    cursor.execute(comando)
    connection.commit()
    retorno = cursor.fetchall()
    cursor.close()
    connection.close()
    return retorno


def select_com_retorno_de_uma_linha(querry):
    connection = psycopg2.connect(connection_string)
    comando = querry
    cursor = connection.cursor()
    cursor.execute(comando)
    connection.commit()
    retorno = cursor.fetchone()
    connection.close()
    return retorno

def select_com_retorno_de_linha_determinada(querry, numero_linha):
    connection = psycopg2.connect(connection_string)
    linha = numero_linha
    comando = querry
    cursor = connection.cursor()
    cursor.execute(comando)
    connection.commit()
    retorno = cursor.fetchmany(linha)
    connection.close()
    return retorno

def conexao_de_insert(querry):
    connection = psycopg2.connect(connection_string)
    comando = querry
    executar = connection.cursor()
    executar.execute(comando)
    connection.commit()
    executar.close()
    connection.close()
    return print("Foi")

def update_status(querry):
    connection = psycopg2.connect(connection_string)
    comando = querry
    executar = connection.cursor()
    executar.execute(comando)
    connection.commit()
    executar.close()
    connection.close()
    return print('Foi')