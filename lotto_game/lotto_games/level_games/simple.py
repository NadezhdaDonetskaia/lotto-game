import random
import os
from threading import Timer
from lotto_game.lotto_games.lotto_game import LottoGame


def timer():
    print('\nВремя вышло, вы проиграли.')
    os._exit(1)


class SimpleLottoGame(LottoGame):
    def rounds(self):
        time_round = 30
        t = Timer(time_round, timer)
        n = random.choice(self.kegs)
        self.kegs.remove(n)
        t.start()
        try:
            print("У вас есть %d секунд чтобы ввести ответ...\n" % time_round)
            player_answer = input(f'{self.player1}\n{self.player2}\n'
                                  f'Бочонок {n} осталось {len(self.kegs)}\n'
                                  f'Хотите зачеркнуть? y/n: ')
            return self.is_correct_answer(player_answer, n)
        finally:
            t.cancel()
