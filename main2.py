from modulos.sistema import *
from modulos.front import Tema



while True:
    tema = Tema()
    mainwindow = tema.janela1()

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
    
    elif mainwindow == '3':
    
        pesquisa = tema.interface_pesquisa()
        jp = Pesquisa()
        jogadorpesquisa = jp.pesquisa_por_id(tema.id)
        print(tema.id)
        print(jogadorpesquisa)
    
        if jogadorpesquisa == True:
            print(tema.id)
            tema.caixa_de_aviso_cadastro_existente()
            
        else:
            print(f'jogador {tema.id} não existe')
            tema.jogador_nao_existe()
            
    
    elif mainwindow == '4':
        break

    
        
    