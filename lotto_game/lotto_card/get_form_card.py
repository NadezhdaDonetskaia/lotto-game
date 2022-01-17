#!/usr/bin/env python
import random


def get_form_card():
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
    form_card = [line1, line2, line3]
    return form_card
