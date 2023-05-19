import os
from modulos.jogadores import *
from modulos.habilidades import Habilidades
from modulos.entradas import Entradas
from modulos.pesquisa import Pesquisa
from eventopath.evento import Evento
from eventopath.times import Times
from eventopath.partida import Partida

class Sistema:
    def __init__(self):
        self.color = ''
        self.clear = ''

    def limpar(self):
        clear = os.system('cls')
        return clear
    

    def cor(self):
        cores = os.system('color 2')
        return cores
    
    #função para definir tratar os numeros inseridos
    def is_num(self):
        pass