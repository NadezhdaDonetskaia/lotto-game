import random
import os
import threading
from lotto_game.lotto_games.lotto_game import LottoGame


def timer(time=30):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"\nУ вас есть {time} секунд чтобы ввести ответ...\n")
            t = threading.Thread(target=func, args=args, kwargs=kwargs, daemon=True)
            t.start()
            t.join(time)

            if t.is_alive():
                print("Время истекло. Вы проиграли")
                return False
            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator


class SimpleLottoGame(LottoGame):
    @timer()
    def rounds(self):
        super().rounds()

