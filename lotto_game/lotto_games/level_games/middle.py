from lotto_game.lotto_games.level_games.simple import SimpleLottoGame


class MiddleLottoGame(SimpleLottoGame):

    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.time = 15
