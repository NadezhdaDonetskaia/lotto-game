from lotto_game.lotto_games.level_games.simple import SimpleLottoGame, timer


class MiddleLottoGame(SimpleLottoGame):

    @timer(time=10)
    def rounds(self):
        super().rounds()
