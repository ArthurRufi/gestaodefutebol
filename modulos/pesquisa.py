from modulos.crudbd import DB

class Pesquisa(DB):
    
    def __init__(self):

        self.pesquisanome = ''
        self.pesquisaid = ''
        self.pesquisadata = ''
        self.host ='localhost'
        self.port = '5432'
        self.database = 'jogadores'
        self.user = 'arthur'
        self.password = '86128931'
        self.ver = bool()
        

    def pesquisa_por_nome(self, nome):
        nome_verify = self.pesquisa_nome(nome)
        self.namever = nome_verify
        
        if nome_verify:
            return nome
        else:
            return None
        


    def pesquisa_por_id(self, p):
        a = p
        id_verify = self.pesquisa_id(a)
        self.ver = id_verify
        
        if self.pesquisa_id(a):
            print('existe')
            return True
        else:
            print('nnnnn')
            return False


    def pesquisa_por_data(self):
        pass