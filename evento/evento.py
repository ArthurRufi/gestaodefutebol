#vai receber todas a funcionalidades do evento e retornar da devida maneira

class Evento:

    def  __init__(self, jogadores):
        self.quantidadepre = ''
        self.jogadores = jogadores


    def quantidade_por_time(self):
        qtd = int(input("Quantos jogadores por time?"))
        return qtd


    def jogagores_do_evento(self):
        pass