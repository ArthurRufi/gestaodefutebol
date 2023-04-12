from jogadores import *
from habilidades import Habilidades
from entradas import Entradas

e = Entradas()
e.nome_entrada()
e.nome_saida()

h = Habilidades(e.nome_saida(), "01/01/1000", "91", "555", "akaka")
print (h.nome )
h.criarhabilidades()


