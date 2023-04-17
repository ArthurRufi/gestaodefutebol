import os

class Pesquisa:
    

    def __init__(self):
        
        self.pesquisanome = ''
        self.pesquisaid = ''
        self.pesquisadata = ''
        
        pass
    
    #O IDEAL DA PESQUISA É QUE ELA SEJA REGISTRADA POR ID

    def pesquisa_por_nome(self):
        '''Iniciar sistema de pesquisa por nome'''
        
        pass


    def pesquisa_por_id(self, p):
        
        self.pesquisaid = p
        print(p)

        '''Organizar para entregar informações ultima linha deve ser o id para pesquisa de habilidades'''
        if os.path.exists(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\credenciais\\{self.pesquisaid}.txt'):
            os.system('cls')
            with open(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\credenciais\\{self.pesquisaid}.txt', 'r') as arquivo:
                for linha in arquivo:
                    print(linha.strip())
            return True
        else:
            print("Jogador não registrado")
            return False



    def pesquisa_por_data(self):
        pass



    def limpar(self):
        clear = os.system('cls')
        return clear