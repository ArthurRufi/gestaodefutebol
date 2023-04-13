class Jogador:
    
    def __init__(self, nome, nascimento, notas, iden):
        self.nome =  nome
        self._nascimento = nascimento
        self._notas= notas
        self._id = iden
        '''não precisar receber notas e iden, receber somente o iden(identificador) e usar funções para entregar informações'''

    
    def cadastro():
        #Caso não existá o jogador usar esse metodo.
        pass

class Pontos(Jogador):
    
    def __init__(self, tops, cabecapoints, pontosproprios):
        Jogador.__init__(self)
        self._toptree = tops
        self._cabeca = cabecapoints
        self._pontos = pontosproprios
        self._idenfication =  self.nome
        

        print (self._cabeca)
    