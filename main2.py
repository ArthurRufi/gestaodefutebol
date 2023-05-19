from modulos.sistema import *
from front import Tema


t = Tema()
mainwindow = t.janela1()
print(mainwindow)
if mainwindow == '1':

    pesquisa = t.interface_pesquisa()

elif mainwindow == '2':

    cadastrar = t.cadastrar()