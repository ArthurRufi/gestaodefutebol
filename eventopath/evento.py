#vai receber todas a funcionalidades do evento e retornar da devida maneira

class Evento:

    def  __init__(self):
        self.quantidadepre = 0
        self.jogadores = list()
        self.goleirossele = list()
        self.quantidadetotal = 0

    def quantidade_por_time(self):
        
        #SE HOUVER GOLEIRO PROPRIO RETORNAR TRUE SE NÃO RETORNAR FALSE PARA TRABALHAR COM ISSO NO MAIN
        #INSERIR QUANTIDADES PREDEFINIDAS PARA FACILITAR O PROCESSO

        goleiro = int(input("Goleiro proprio? "))
        qtd = 0
        
        if goleiro == 1:
            qtd = int(input("Insira a quantidade de jogadores com goleiro: "))
             
            print (f'Quantidade de jogadores: {qtd - 1}')
            self.quantidadepre = qtd
            return True
        
        else:
            qtd = int(input("Insira a quantidade de jogadores sem goleiro: "))
            self.quantidadepre = qtd
            qtddegoleiros = int(input("Insira a quantidade de goleiros do evento: "))
            for x in range(qtddegoleiros):
                goleiros = input(f"Insira o nome do goleiro {x}: ")
                self.goleirossele.append(goleiros)
            
            
            return False


    def id_jogadores_evento(self):

        self.listadejogadores = []
        self.quantidadetotal = int(input("Insira a quantidade todal de jogadores: ")) 
        for qtddejogador in range(self.quantidadetotal):
            inserir = input("Insira o id do jogador: ")
            #Inserir meio para o amostrar nome do jogador e outra referencia
            self.listadejogadores.append(inserir)
        
        self.jogadores = self.listadejogadores
        
        

    #avaliar se esses metodos devem ir para a classe Time
    def nome_dos_jogadores(self):
        #pegar ids registrados e repassar nomes dos jogadores
        
        for id_jogador in self.jogadores:
            with open(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\datainfos\\{id_jogador}.txt', 'r') as jogador:
                identificador = jogador.readlines()
                nome = identificador[0].rstrip()           
            print(nome)
        
        if len(self.jogadores) == 0:
            print("Insira jogadores")

        else:
            for x in self.jogadores:
                print(x)

    
        
