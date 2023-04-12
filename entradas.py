class Entradas:
    def __init__(self):
        self.enome = ""
        self.eid = ""
        self.nascimento = ""
    
    
    def nome_entrada(self):
        n = input("Insira o nome do jogador: ")
        self.enome = n

    def eid_entrada(self):
        n = input("Insira o id do jogador: ")
        self.eid = n


    def nome_saida(self):
       
        if self.enome == "":
            print("Favor Insira um nome")
        else:
            return self.enome
    

    def id_saida(self):
        
        if self.eid == "":
            print("Favor Insira um nome")
        else:
            return self.eid
            
        
    
    def set_nascimento():
        pass


    def get_nascimento():
        pass

