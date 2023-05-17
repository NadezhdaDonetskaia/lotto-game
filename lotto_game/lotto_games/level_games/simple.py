import random
import threading
from queue import Queue
from lotto_game.lotto_games.lotto_game import LottoGame


class SimpleLottoGame(LottoGame):

    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.time = 30

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
            return result.get()

