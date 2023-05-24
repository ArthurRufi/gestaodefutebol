import psycopg2


class DB():
    def __init__(self):
        self.host ='localhost'
        self.port = '5432'
        self.database = 'jogadores'
        self.user = 'arthur'
        self.password = '86128931' 

    def criar_banco(self):
        
        conn = self.bancoiniciar()
        cursor = conn.cursor()

        insert_query = (f"CREATE TABLE jogadores_infos (id SERIAL PRIMARY KEY, nome VARCHAR(255) NOT NULL, nascimento DATE NOT NULL)")
        cursor.execute(insert_query)
        conn.commit()

        cursor.close()
        conn.close()


    def bancoiniciar(self):
        host = self.host
        port = self.port
        database = self.database
        user =  self.user
        password = self.password
        conn = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
        self.conn = conn
        return conn
    

    def pesquisa_id(self, id):
        conn = self.bancoiniciar()

        curso = conn.cursor()
        id_pesquisa = id

        query = f'SELECT * FROM jogadores_infos WHERE id = {id_pesquisa}'
        curso.execute(query)
        resultado = curso.fetchone()
        conn.close()

        if resultado:
            return True
        else:
            return False
        
    def pesquisa_nome(self, nome):
        conn = self.bancoiniciar()

        curso = conn.cursor()
        nome_pesquisa = nome

        query = 'SELECT * FROM jogadores_infos WHERE nome = %s'
        curso.execute(query, (nome_pesquisa,))
        resultado = curso.fetchone()

        if resultado:
            return True
        else:
            return False


        