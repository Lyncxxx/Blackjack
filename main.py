import random



valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
naipes = ["Copas", "Ouros", "Espadas", "Paus"]

class Carta:
    def __init__(self, valor, naipe):
        self.naipe = naipe
        self.valor = valor

    def __str__(self):
        return f'{self.valor} de {self.naipe}'

class Baralho:
    def __init__(self):
        self.lista_de_cartas = [Carta(valor, naipe) for naipe in naipes for valor in valores]

    def exibir_baralho(self):
        for carta in self.lista_de_cartas:
            print(carta, end=' ')
        print()

    def embaralhar(self):
        random.shuffle(self.lista_de_cartas)
        print('Cartas embaralhadas com sucesso!')

    def distribuir_carta(self):
        carta_do_topo = self.lista_de_cartas[0]
        self.lista_de_cartas.pop(0)
        return carta_do_topo

class Jogador:
    def __init__(self):
        self.mao = []
        self.pontuacao = 0

    def ver_mao(self):
        for carta in self.mao:
            print(f'{carta}, ', end='')
        print()

    def pedir_carta(self):
        while True:
            carta = jogo.baralho.distribuir_carta()
            if carta not in self.mao:
                self.mao.append(carta)
                break

    def calcular_pontucao(self):
        pontuacao_provisoria = 0
        for carta in self.mao:
            if carta.valor.isnumeric():
                pontuacao_provisoria += int(carta.valor)
            elif carta.valor in 'KQJ':
                    pontuacao_provisoria += 10
            else:
                pontuacao_provisoria += 1
        self.pontuacao = pontuacao_provisoria
        return self.pontuacao

    def verfificar_estouro(self):
        if self.pontuacao > 21:
            print('O jogador estourou!')
            return True
        else:
            return False

class Jogo:
    def __init__(self):
        self.baralho = Baralho()
        self.jogadores = []

    def inicializar_jogo(self):
        """
        Prepara o baralho e destribui as duas cartas iniciais
        :return: none
        """
        jogo.baralho.embaralhar()
        jogo.fluxo_de_jogo()

    def fluxo_de_jogo(self):
        for c in range(2):
            dealer.pedir_carta()
            jogador.pedir_carta()
        jogo.turno_do_jogador()
        jogo.turno_do_dealer()
        jogo.verificar_vencedor()

    def turno_do_jogador(self):
        print('JOGADOR')
        while True:
            jogador.calcular_pontucao()
            jogador.ver_mao()
            print(f'Pontuação: {jogador.pontuacao}')
            if jogador.verfificar_estouro():
                break
            res = str(input('Deseja mais uma carta?[s/n] ')).strip().lower()[0]
            if res == 's':
                jogador.pedir_carta()
            if res == 'n':
                break

    def turno_do_dealer(self):
        print()
        print('DEALER')
        dealer.calcular_pontucao()
        dealer.ver_mao()
        print(f'Pontuação: {dealer.pontuacao}')
        print()
        if jogador.pontuacao <= 21:
            while dealer.pontuacao < jogador.pontuacao and dealer.pontuacao < 21:
                dealer.pedir_carta()
                print('DEALER')
                dealer.calcular_pontucao()
                dealer.ver_mao()
                print(f'Pontuação: {dealer.pontuacao}')
                print()

    def verificar_vencedor(self):
        if jogador.pontuacao <= 21 < dealer.pontuacao or dealer.pontuacao < jogador.pontuacao <= 21:
            print('Jogador venceu!')
        elif jogador.pontuacao == dealer.pontuacao:
            print('Deu empate!')
        else:
            print('Dealer venceu!')

jogo = Jogo()
jogador = Jogador()
dealer = Jogador()
jogo.jogadores.extend([jogador, dealer])
jogo.inicializar_jogo()
