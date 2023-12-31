import mysql.connector
from mysql.connector import Error
class Dbconnect:
    def __init__(self):
        self.mydb = None
    #FUNÇÃO PARA CONECTAR O BD COM O CÓDIGO
    def connect_database(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                port='3306',
                database='loginscreen'
            )

        except Exception as erro:
            if erro.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro de autenticação: Usuário ou senha incorretos.")
            elif erro.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("O Banco de dados não existe.")
            elif erro.errno == mysql.connector.errorcode.CR_CONN_HOST_ERROR:
                print("Erro de conexão: Host do banco de dados não encontrado.")
            else:
                print(f"Erro não identificado: {erro}")

    #PEGANDO O CURSOR PARA REFERENCIAR NO CODIGO
    def get_cursor(self):
        return self.connection.cursor()