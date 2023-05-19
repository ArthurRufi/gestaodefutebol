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

        while True:
            goleiroentrada = (input("Goleiro proprio? "))
            goleiro = int()

            if goleiroentrada.isdigit():
                goleiro = int(goleiroentrada)
                break
            else:
                goleiroentrada = input('Coloque um numero valido: ')
                goleiro = int(goleiroentrada)
                continue
        
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


    def quantidade_de_jogadores_do_evento(self):

        self.listadejogadores = []
        qtd = int(input("Insira a quantidade todal de jogadores: ")) 
        
        if qtd <=50:
            self.quantidadetotal = qtd
        else:
            print ("Quantidade indisponivel nessa versão, MAXIMO 50")
        
        
    def nome_dos_jogadores(self):
        #pegar ids registrados e repassar nomes dos jogadores
        
        for id_jogador in self.jogadores:
            with open(f'D:\\PythonArquivos\\pyarchives\\gestaofutebol\\datainfos\\{id_jogador}.txt', 'r') as jogador:
                identificador = jogador.readlines()
                nome = identificador[0].rstrip()           
            print(nome)
        
        if len(self.jogadores) == 0:
            print("Insira jogadores")
            return False

        else:
            return True
    

    def init_event(self, condition):

        if condition == 1:
            self.quantidade_de_jogadores_do_evento()
            self.quantidade_por_time()
    
        
