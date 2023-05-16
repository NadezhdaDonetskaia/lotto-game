import random
import os
import threading
from lotto_game.lotto_games.lotto_game import LottoGame


class SimpleLottoGame(LottoGame):
    def rounds(self):
        n = random.choice(self.kegs)
        self.kegs.remove(n)

        print(f"\nУ вас есть {30} секунд чтобы ввести ответ...\n")

        def get_player_answer():
            player_answer = input(f'{self.player1}\n{self.player2}\n'
                                  f'Бочонок {n} осталось {len(self.kegs)}\n'
                                  f'Хотите зачеркнуть? y/n: \n')
            return self.is_correct_answer(player_answer, n)

        timer = threading.Thread(target=get_player_answer, daemon=True)
        timer.start()
        timer.join(30.0)

        if timer.is_alive():
            print("Время истекло.")
            return False

        else:
            return get_player_answer()
