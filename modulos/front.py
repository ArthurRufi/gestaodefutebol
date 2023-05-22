from PySimpleGUI import PySimpleGUI as sg
from modulos.pesquisa import Pesquisa


class Tema:

    def __init__(self):
        self.nome = ''
        self.id = int()
        self.nascimento = ''
        self.goleiro = bool()


    def iniciarevento(self):
        sg.theme('LightYellow')
        jogadorescombo = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        goleiroscombo = ['Sim', 'Não']
        layout4 = [
            [sg.Text('Vamos Iniciar o evento', justification= 'Center')],
            [sg.Text('Insira a quantidade total de jogadores')],
            [sg.Input(key='Tjogadores')],
            [sg.Text('Qaunto jogadores por time?', size=(20,1)), sg.Combo(jogadorescombo, default_value='Escolha', key='jogadores', size=(20,20))],
            [sg.Text('Essa partida possui goleiro?', size=(20,1)), sg.Combo(goleiroscombo, default_value='Escolha', key='goleiros', size=(20,20))],
            [sg.Button('Sair'), sg.Button('Enviar')],
            
        ]

        self._iniciar = sg.Window('Iniciar', layout= layout4, finalize=True)
        
        janelainicio = self._iniciar

        while True:
            event, values = janelainicio.read() # type: ignore
            
            if event == 'Enviar' and values ['Tjogadores'] != '':
                if values ['Tjogadores'] != '':
                    if values['goleiros'] == 'Sim':
                        self.goleiro = True
                        print('sim goleiro')
                    else:
                        print('não goleiro')
                        self.goleiro = False
                janelainicio.close()

            elif event == 'Enviar' and values ['Tjogadores'] == '':
                continue

            elif event == 'Sair' or event == sg.WIN_CLOSED:
                janelainicio.close()
                break


    def janela1(self):
        #deve retornar comandos para abertura de janelas.
        sg.theme('Dark Blue')
        layout = [
            [sg.Text('Escolha sua opção', justification= 'Center')],
            [sg.Radio('Evento', 'g', key='Evento')],
            [sg.Radio('Gestão de jogadores', 'g', key='Gestão')],
            [sg.Radio('Pesquisa de jogador', 'g', key='Pesquisa')],
            [sg.Button('Enviar'), sg.Button('Sair')],
            [sg.Image('archivesimages\\bola-2.png')]
        ]
        self.main = sg.Window('Opções', layout=layout, finalize=True)
        
        janelamain = self.main
        janelamain.maximize()

        while True:
            event, values = janelamain.read() # type: ignore

            if event == 'Enviar':

                if values['Evento'] == True:
                    janelamain.close()
                    return '1'
                    
                elif values ['Gestão'] == True:
                    janelamain.close()
                    return '2'
                
                elif values ['Pesquisa'] == True:
                    janelamain.close()
                    return '3'
                
            elif event == 'Sair' or event == sg.WIN_CLOSED:
                janelamain.close()
                break

        janelamain.close()
        
    

    def interface_pesquisa(self):
        sg.theme('LightYellow')

        layout2 = [
            [sg.Text('Insira o id do jogador')],
            [sg.Input(key='Nome2')],
            [sg.Button('Pesquisar'), sg.Button('Sair')]
            
        ]

        self.pesquisa = sg.Window('Pesquisa', layout=layout2, finalize=True)

        janelaatual = self.pesquisa
        
        event, values = janelaatual.read() # type: ignore

        if event == 'Pesquisar':
            self.id = values['Nome2']
            return values
        elif event == 'Sair' or event == sg.WIN_CLOSED:
            janelaatual.close()
        
        janelaatual.close()

                

    def cadastrar(self):
        sg.theme('LightYellow')
        layout3 = [
                [sg.Text('Insira os dados do jogador')],
                [sg.Text('Nome', size=20), sg.Input(key= 'Name')],
                [sg.Text('ID', size=20), sg.Input(key= 'id')],
                [sg.Text('Nascimento', size=20), sg.Input(key= 'nascimento')],
                [sg.Button('Enviar'), sg.Button('Sair')],
            ]

        self.consulta = sg.Window('Cadastro', layout=layout3, finalize=True)

        janelamain = self.consulta

        while True:
            event, values = janelamain.read() # type: ignore

            if event == 'Enviar':

                if values['Name'] != '' and values['id'] != '' and values['nascimento'] != '':
                    
                    self.nome = values['Name']
                    self.id = values['id']
                    self.nascimento = values['nascimento']
                    print(f'nome = {self.nome}, id = {self.id}, nascimento = {self.nascimento}')
                    return '1'
                    
                elif values['Name'] == '' and values['id'] == '' and values['nascimento'] == '':
                    print (f'valores inexistentes ou algum valor vazio, {values}')
                    return '1'
                
            elif event == 'Sair' or event == sg.WIN_CLOSED:
                janelamain.close()
                break
            
            janelamain.close()


    def caixa_de_aviso_cadastro_existente(self):
        pass