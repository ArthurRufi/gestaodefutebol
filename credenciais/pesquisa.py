import os

class Pesquisa:
    

    def __init__(self):
        
        self.pesquisanome = ''
        self.pesquisaid = ''
        self.pesquisadata = ''
        
        pass
    
    #O IDEAL DA PESQUISA É QUE ELA SEJA REGISTRADA POR ID

    def pesquisa_por_nome():
        pass


    def pesquisa_por_id(self):
        
        l = input("Insira o id do cidadão: ")
        self.pesquisaid = l
        print(l)

        '''Organizar para entregar informações ultima linha deve ser o id para pesquisa de habilidades'''
        if os.path.exists(f'D:\PythonArquivos\pyarchives\gestaofutebol\credenciais\\{self.pesquisaid}.txt'):
            with open(f'D:\PythonArquivos\pyarchives\gestaofutebol\credenciais\\{self.pesquisaid}.txt', 'r') as arquivo:
                for linha in arquivo:
                    print(linha.strip())
            return True
        else:
            print("Jogador não registrado")
            return False



    def pesquisa_por_data():
        pass