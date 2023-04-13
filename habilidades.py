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
        n = self._id

        if  os.path.isfile(f'D:\PythonArquivos\pyarchives\gestaofutebol\\{n}.txt'):
            print("Jogador Já tem habilidades existentes!")

        else:
            print("Criar habilidades")    


    def modificarhabilidades():
        
        '''Receber Habilidades e alterar no arquivo'''
        pass