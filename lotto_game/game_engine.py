from .lotto_game import LottoGame
from .level_games.simple import SimpleLottoGame
from .level_games.middle import MiddleLottoGame
from .level_games.hard import HardLottoGame
from .lotto_card.lotto_card import LottoCard


def game_engine():
    player = LottoCard(input('Давай знакомиться: '))
    computer = LottoCard('Computer')
    print(f'Добро пожаловать в игру лото, {player}!\n'
          f'Твоя задача - зачеркнуть все числа в карточке раньше компьютера.\n'
          f'Тебе нужны внимательность, скорость (если уровень посложнее) и удача.\n')
    level = input('Выберем уровень:\n'
                  '0 - самый простой, у тебя неогранниченное время на ответ\n'
                  '1 - посложнее, у тебя 30 секунд на ответ\n'
                  '2 - средний, 10 секунд на ответ\n'
                  '3 - сложный, время на ответ будет сокращаться вместе с числами в карточке\n'
                  'На какой сложности играем? (0 по-умолчанию): ')
    if level == '1':
        game = SimpleLottoGame(player, computer)
    elif level == '2':
        game = MiddleLottoGame(player, computer)
    elif level == '3':
        game = HardLottoGame(player, computer)
    else:
        game = LottoGame(player, computer)
    return game
