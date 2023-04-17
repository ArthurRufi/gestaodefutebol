import os
from jogadores import *
from fileshabilidades.habilidades import Habilidades
from credenciais.entradas import Entradas
from credenciais.pesquisa import Pesquisa
from eventopath.evento import Evento
from eventopath.times import Times

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