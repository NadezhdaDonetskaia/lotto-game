#!/usr/bin/env python
import random


class LottoGame():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def start(self):
        kegs = list(range(1, 91))
        while True:
            n = random.choice(kegs)
            kegs.remove(n)
            info = input(f'{self.player1}\n{self.player2}\n'
                         f'Бочонок {n} осталось {len(kegs)}\nХотите зачеркнуть? y/n: \n')
            if info == 'y':
                if n not in self.player1.nums:
                    print(f'{self.player1.name} проиграл!')
                    break
                else:
                    self.player1.cross_out_num(n)
            else:
                if n in self.player1.nums:
                    print(f'{self.player1.name} проиграл!')
                    break
            self.player2.cross_out_num(n)
            if len(self.player1.nums) == 0:
                print(f'{self.player1.name} победил!')
                break
            elif len(self.player2.nums) == 0:
                print(f'Компьютер {self.player2.name} выиграл!')
                break
