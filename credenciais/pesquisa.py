import os

class Pesquisa:
    

    def __init__(self):
        
        self.pesquisanome = str
        self.pesquisaid = str
        self.pesquisadata = str
        
        pass
    
    #O IDEAL DA PESQUISA É QUE ELA SEJA REGISTRADA POR ID

    def pesquisa_por_nome():
        pass


    def pesquisa_por_id(self):
        
        l = input("Insira o id do cidadão: ")
        self.pesquisaid = l

        if os.path.exists(f'D:\PythonArquivos\pyarchives\gestaofutebol\\fileshabilidades\\{self.pesquisaid}.txt'):
            with open(f'D:\PythonArquivos\pyarchives\gestaofutebol\\fileshabilidades\\{self.pesquisaid}.txt', 'r') as arquivo:
                for linha in arquivo:
                    print(linha.strip())

        else:
            print("Jogador não registrado")
        


    def pesquisa_por_data():
        pass