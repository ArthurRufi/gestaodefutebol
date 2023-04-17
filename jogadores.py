import os

class Jogador:
    
    def __init__(self, nome, nascimento, notas, iden):
        self.nome =  nome
        self._nascimento = nascimento
        self._notas= notas
        self._id = iden
        self.cartoes = ""
        '''não precisar receber notas e iden, receber somente o iden(identificador) e usar funções para entregar informações'''

    
    def cadastro(self):
       
        if not os.path.exists(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\datainfos\\{self._id}.txt'):
            with open(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\datainfos\\{self._id}.txt', 'a') as player:
                lista =[f'Nome: {self.nome}\n', f'Nascimento: {self._nascimento}\n', f'Notas: {self._notas}\n', f'ID: {self._id}\n']
                player.writelines(lista)
                return True
            
        else:
            print("Jogador já existe")
            return False

    
    def apagar(self):

        '''Pesquisa se o jogador existe, se existir ele retorna as informações do jogador e pergunta se deseja apagar as informações'''
        if os.path.exists(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\datainfos\\{self._id}.txt'):
            
            file = open(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\datainfos\\{self._id}.txt', 'r', )
            for linha in file:
                print(linha.rstrip())
                
                #melhorar esse close()

            confirmacao = int(input("Tem certeza?\n(1) Sim\n(2)NÃO: "))
            if confirmacao == 1:
                file.close()
                os.remove(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\datainfos\\{self._id}.txt')  
                print("JOGADOR DELETADO")
                input("Precione ENTER para sair!")

            else:
                print("NAO APAGADO")
        
        else:
            print("Arquivo inesistente")
        


    