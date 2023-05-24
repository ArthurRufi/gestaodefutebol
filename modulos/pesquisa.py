from modulos.crudbd import DB

class Pesquisa(DB):
    

    def __init__(self):
        
        self.pesquisanome = ''
        self.pesquisaid = ''
        self.pesquisadata = ''
        
        

    def pesquisa_por_nome(self):
        '''Iniciar sistema de pesquisa por nome'''
        
        pass


    def pesquisa_por_id(self, p):
        
        id_verify = self.pesquisa_id(p)
        if id_verify:
            print('existe')
        else:
            print ('nao')


    def pesquisa_por_data(self):
        pass


p = Pesquisa()
p.pesquisa_id('111')

    
