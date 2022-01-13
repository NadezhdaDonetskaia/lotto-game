#!/usr/bin/env python
import random


class LottoCard:
    def __init__(self, name):
        self.name = name
        self.list = []
        self.nums = []
        """
        формируем первые две строчи True - будещее число, False - пустота
        """
        line1 = [True] * 5 + [False] * 4
        line2 = [True] * 5 + [False] * 4
        """
        Перемешиваем первые две строчки и формируем третью,
        с учетом того, что вертикальная линия содержит не более 2х чисел
        """
        line3 = [False] * 9
        while True:
            random.shuffle(line1)
            random.shuffle(line2)
            if line1 != line2:
                ind = 5
                for i in range(9):
                    if not line1[i] and not line2[i]:
                        line3[i] = True
                        ind -= 1
                    elif line1[i] != line2[i]:
                        if ind != 0:
                            line3[i] = True
                            ind -= 1
                break
        self.list.append(line1)
        self.list.append(line2)
        self.list.append(line3)
        """
        заполняем список случайными числами
        """
        for i in range(3):
            for j in range(9):
                if self.list[i][j]:
                    self.list[i][j] = self.__create_num__(j)
                else:
                    self.list[i][j] = ' '

    def __create_num__(self, num):
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

    def __str__(self):
        card_str = f'{self.name}:\n{"-" * 26}\n'
        for line in self.list:
            card_str += f'{" ".join(str(x).ljust(2) for x in line)}\n'
        return card_str
    def _cross_out_num_(self, num):
        for i in range(3):
            for j in range(9):
                if num == self.list[i][j]:
                    self.list[i][j] = '--'
                    self.nums.remove(num)
                    break
