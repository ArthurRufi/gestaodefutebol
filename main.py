from jogadores import *
from habilidades import Habilidades
from entradas import Entradas
import os

e = Entradas()

e.charmar()
h = Habilidades(e.nome_saida(), e.get_nascimento(), "91", e.id_saida(), "akaka")
h.criarhabilidades()

os.system('cls')
print(f'Nome: {h.nome}')
print(f'ID: {h._id}')
print(f'Nascimento: {h._nascimento}')
'''
exemplo de recebimento tratamento de erros
if e.nome_saida() == False:
    print("not name")
else:
    print("erro inesperado")
'''