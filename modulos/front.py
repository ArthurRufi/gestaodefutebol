from PySimpleGUI import PySimpleGUI as sg
from modulos.pesquisa import Pesquisa


class Tema:

    def __init__(self):
        self.nome = ''
        self.id = 0
        self.nascimento = ''
        self.goleiro = bool()
        self.jogadores = int()

    def iniciarevento(self):
        sg.theme('LightYellow')
        jogadorescombo = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        goleiroscombo = ['Sim', 'Não']
        jogadorestotais = [i for i in range(1, 51)]
        layout4 = [
            [sg.Text('Vamos Iniciar o evento', justification= 'Center')],
            [sg.Text('Insira a quantidade total de jogadores')],
            [sg.Text('Quantos jogadores totais?', size=(20,1)), sg.Combo(jogadorestotais, default_value='Escolha', key='jogadorestotais', size=(20,20))],
            [sg.Text('Quantos jogadores por time?', size=(20,1)), sg.Combo(jogadorescombo, default_value='Escolha', key='jogadores', size=(20,20))],
            [sg.Text('Essa partida possui goleiro?', size=(20,1)), sg.Combo(goleiroscombo, default_value='Escolha', key='goleiros', size=(20,20))],
            [sg.Button('Sair'), sg.Button('Enviar')],
            
        ]

        self._iniciar = sg.Window('Iniciar', layout= layout4, finalize=True)
        
        janelainicio = self._iniciar

        while True:
            event, values = janelainicio.read() # type: ignore
    
            if event == 'Enviar' and values ['jogadorestotais'] in jogadorestotais and values['jogadores'] in jogadorescombo and values['goleiros'] in goleiroscombo:
                if values ['jogadorestotais'] != '':
                    self.jogadores = values['jogadorestotais']
                    if values['goleiros'] == 'Sim':
                        self.goleiro = True
                        self.jogadores = values['jogadorestotais']
                    else:
                        self.goleiro = False
                janelainicio.close()

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
            [sg.Radio('Finalizar', 'f', key='Final')],
            [sg.Button('Enviar'), sg.Button('Sair')],
            [sg.Image('archivesimages\\bola-2.png')]
        ]
        self.main = sg.Window('Opções', layout=layout, finalize=True) # type: ignore
        
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
                
                elif values ['Final'] == True:
                    janelamain.close()
                    return '4'
                
            elif event == 'Sair' or event == sg.WIN_CLOSED:
                janelamain.close()
                break

        janelamain.close()
        
    

    def interface_pesquisa(self):
        sg.theme('LightYellow')

        layout2 = [
            [sg.Text('Insira o id do jogador')],
            [sg.Input(key='ID')],
            [sg.Button('Pesquisar'), sg.Button('Sair')]   
        ]

        self.pesquisa = sg.Window('Pesquisa', layout=layout2, finalize=True)
        janelaatual = self.pesquisa


        event, values = janelaatual.read() # type: ignore  
        valor = int(values['ID'])

        self.id = valor
        while True:
                
            if event == 'Pesquisar' and type(valor) == int():
                if type(valor) == int():
                    self.id = valor
                    print('achou')
                    return values
                else: 
                    print('valor deve ser inteiro')
                    break

            elif event == 'Sair' or event == sg.WIN_CLOSED:
                janelaatual.close()
            else: 
                janelaatual.close()
                

            break   

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


    def gestao(self):
        pass


    def caixa_de_aviso_cadastro_existente(self):
        sg.theme('LightBrown8')
        layout5 = [
            [sg.Text('Jogador já existe!!!')],
            [sg.Button('OK', button_color='Blue', key='OK')],
            [],
            [],
            [],
            ]

        self.caixa_de_aviso_cadastro = sg.Window('Aviso cadastr', layout=layout5, finalize=True)
        caixa = self.caixa_de_aviso_cadastro


        while True:
            event, values = caixa.read() #type: ignore

            if event == 'OK':
                caixa.close()
                break


    def jogador_nao_existe(self):
        sg.theme('LightBrown8')
        layout6 = [
            [sg.Text('Jogador não existe!!!')],
            [sg.Button('OK', button_color='Blue',key= 'OK')],
            [],
            [],
            [],
            ]

        self.caixa_de_aviso_nao_existe = sg.Window('Aviso cadastro', layout=layout6, finalize=True)
        caixa2 = self.caixa_de_aviso_nao_existe


        while True:
            event, values = caixa2.read() #type: ignore

            if event == 'OK':
                caixa2.close()
                break

    
                
        