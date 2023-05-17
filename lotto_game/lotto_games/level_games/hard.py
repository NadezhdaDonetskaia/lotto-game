import random
# import math
import threading
from queue import Queue
from lotto_game.lotto_games.level_games.simple import SimpleLottoGame


class HardLottoGame(SimpleLottoGame):

    def set_time(self):
        self.time = round((30 ** (1 / 89)) ** (len(self.kegs)-1), 2)

    def get_answer(self, number_keg):
        print(f"\nУ тебя есть {self.time} секунд чтобы ввести ответ...\n")
        result = Queue()

        def inner():
            result.put(input(f'{self.player1}\n{self.player2}\n'
                             f'Бочонок {number_keg} осталось {len(self.kegs)}\n'
                             f'Хотите зачеркнуть? y/n: \n'))

        t = threading.Thread(target=inner, daemon=True)
        t.start()
        t.join(self.time)

        if t.is_alive():
            print("Время истекло. Вы проиграли")
            return False
        else:
            self.set_time()
            return result.get()




