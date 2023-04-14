from jogadores import Jogador
import os

class Habilidades(Jogador):
  
    def __init__(self, nome, nascimento, notas, iden, conjunto):
        Jogador.__init__(self,  nome, nascimento, notas, iden) 
        
        self._conjunto = conjunto

        
    def habilidadesdetalhadas(self):
        
        
        '''fazer argumentos entrarem nas chaves'''
        
        habilidadesdojogador ={"Ataque": 0, "Defesa": 1, "Passe": 2, "Velocidade": 3, "Inteligencia": 4, "Visão": 5, "Resistencia": 6, "Drible": 7}

        for k, r in habilidadesdojogador.items():
            print(r)
        '''
        **** Como vai funcionar a questão da modificação da habilidades e evolução****
        '''
        

    def criarhabilidades(self):
        ''' Caso o jogador não exista criar as habilidades, sempre chamado com a função criarjogador da classe Jogador, necessario receber id do jogador'''
        self._id

        if  os.path.isfile(f'D:\PythonArquivos\pyarchives\gestaofutebol\\fileshabilidades\\{self._id}.txt'):
            print("Jogador Já tem habilidades existentes!")

        else:
            '''Melhorar esse laço, crie um laço FOR'''
            while True:
                file = open(f'D:\PythonArquivos\pyarchives\gestaofutebol\\fileshabilidades\\{self._id}.txt', "a")
                atack = input("Insira o ataque: ")
                file.write(f'Ataque {atack}')
                file.close()
                break

    def modificarhabilidades(self):
        
        
        
        op = int(input("(1) excluir?"))
        if op == 1:
            if os.path.exists(f'D:\PythonArquivos\pyarchives\gestaofutebol\\fileshabilidades\\{self._id}.txt'):
                os.remove(f'D:\PythonArquivos\pyarchives\gestaofutebol\\fileshabilidades\\{self._id}.txt')
            else:
                print("Arquivo não existe")
            
        '''Receber Habilidades e alterar no arquivo'''
        pass