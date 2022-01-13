#!/usr/bin/env python
import random
from .lotto_card import LottoCard


class LottoGame(LottoCard):
    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def _cross_out_num_(self, num):
        for i in range(3):
            for j in range(9):
                if num == self.list[i][j]:
                    self.list[i][j] = '--'
                    self.nums.remove(num)
                    break

    def start(self):
        kegs = list(range(1, 91))
        while True:
            n = random.choice(kegs)
            kegs.remove(n)
            ans = input(f'{self.player1}\n{self.player2}\nБочонок {n} осталось {len(kegs)}\nХотите зачеркнуть? y/n: \n')
            if ans == 'y':
                if n not in self.player1.nums:
                    print(f'{self.player1.name} проиграл!')
                    break
                else:
                    self.player1._cross_out_num_(n)
            else:
                if n in self.player1.nums:
                    print(f'{self.player1.name} проиграл!')
                    break
            self.player2._cross_out_num_(n)
            if len(self.player1.nums) == 0:
                print(f'{self.player1.name} победил!')
                break
            elif len(self.player2.nums) == 0:
                print(f'Компьютер {self.player2.name} выиграл!')
                break
