class Jogador:
    def __init__(self, nome, nascimento, notas, iden):
        self._nome =  nome
        self._nascimento = nascimento
        self._notas= notas
        self._id = iden
        '''não precisar receber notas e iden, receber somente o iden(identificador) e usar funções para entregar informações'''
        

class Pontos(Jogador):
    def __init__(self, tops, cabecapoints, pontosproprios, jogador):
        self._toptree = tops
        self._cabeca = cabecapoints
        self._pontos = pontosproprios
        self._idenfication =  jogador
        

        print (self._cabeca)
    