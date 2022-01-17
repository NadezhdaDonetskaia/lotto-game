#!/usr/bin/env python
from ..lotto_game import LottoGame
from ..lotto_card.lotto_card import LottoCard

player1 = LottoCard('Gamer')
player2 = LottoCard('Comp')
game = LottoGame(player1, player2)


def start():
    game.start()


if __name__ == '__main__':
    start()
