#!/usr/bin/env python
import random
from get_form_card import get_form_card


class LottoCard:
    def __init__(self, name):
        self.name = name
        self.list = self.fill_card(get_form_card())
        self.nums = []

    def __str__(self):
        card_str = f'{self.name}:\n{"-" * 26}\n'
        for line in self.list:
            card_str += f'{" ".join(str(x).ljust(2) for x in line)}\n'
        return card_str

    def get_num(self, num):
        while True:
            if num == 0:
                n = random.choice(range(1, 10))
            elif num == 8:
                n = random.choice(range(80, 91))
            else:
                n = random.choice(range(num * 10, num * 10 + 10))
            if n not in self.nums:
                self.nums.append(n)
                return n

    def fill_card(self, billet):
        """
        заполняем болванку карточки случайными числами
        """
        for i in range(3):
            for j in range(9):
                if billet[i][j]:
                    billet[i][j] = self.get_num(j)
                else:
                    billet[i][j] = ' '
        return billet

    def _cross_out_num_(self, num):
        for i in range(3):
            for j in range(9):
                if num == self.list[i][j]:
                    self.list[i][j] = '--'
                    self.nums.remove(num)
                    break
