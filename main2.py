from modulos.sistema import *
from modulos.front import Tema



while True:
    tema = Tema()
    mainwindow = tema.janela1()
    print(mainwindow)

    if mainwindow == '1':
        tema.iniciarevento()
        initevento = Evento()
        entradas = Entradas()
        pesquisas = Pesquisa()
        partida = Partida()
        
        initevento.quantidadetotal = tema.jogadores
        initevento.goleirosbool = tema.goleiro
        print(initevento.quantidadetotal)

    elif mainwindow == '2':

        cadastrar = tema.cadastrar()
        cdPlayer = Jogador(tema.nome, tema.nascimento, None, tema.id)
        if cdPlayer.cadastro(True) == False:
            #controle para caso jogador já exista ou id não correspondente
            pass
    
    elif mainwindow == '4':
        #ao retornar 1 é iniciado o sistema de pesquisa, ao retornar 2 é iniciado o sistema de cadastro.
        pesquisa = tema.interface_pesquisa()
        jp = Pesquisa()
        jp.pesquisa_por_id(tema.id)
    
    elif mainwindow == '4':
        pass
        
    break