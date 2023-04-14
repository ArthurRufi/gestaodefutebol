import os

class Jogador:
    
    def __init__(self, nome, nascimento, notas, iden):
        self.nome =  nome
        self._nascimento = nascimento
        self._notas= notas
        self._id = iden
        '''não precisar receber notas e iden, receber somente o iden(identificador) e usar funções para entregar informações'''

    
    def cadastro(self):
       
        if not os.path.exists(f'D:\PythonArquivos\pyarchives\gestaofutebol\credenciais\\{self._id}.txt'):
            with open(f'D:\PythonArquivos\pyarchives\gestaofutebol\credenciais\\{self._id}.txt', 'a') as player:
                lista =[f'Nome: {self.nome}\n', f'Nascimento: {self._nascimento}\n', f'Notas: {self._notas}\n', f'ID: {self._id}\n']
                player.writelines(lista)
            
        else:
            print("Jogador já existe")

    
    def apagar(self):
        if os.path.exists(f'D:\PythonArquivos\pyarchives\gestaofutebol\credenciais\\{self._id}.txt'):
            
            confirmacao = int(input("Tem certeza?\n(1) Sim\n(2)NÃO"))
            if confirmacao == 1:
                os.remove(f'D:\PythonArquivos\pyarchives\gestaofutebol\credenciais\\{self._id}.txt')  
            else:
                print("NAO APAGADO")
        
        else:
            print("Arquivo inesistente")
        

class Pontos(Jogador):
    
    def __init__(self, tops, cabecapoints, pontosproprios):
        Jogador.__init__(self)
        self._toptree = tops
        self._cabeca = cabecapoints
        self._pontos = pontosproprios
        self._idenfication =  self.nome
        

        print (self._cabeca)
    