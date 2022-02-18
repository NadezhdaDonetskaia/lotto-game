import random


class LottoGame():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.kegs = list(range(1, 91))

    def rounds(self):
        n = random.choice(self.kegs)
        self.kegs.remove(n)
        player_answer = input(f'{self.player1}\n{self.player2}\n'
                              f'Бочонок {n} осталось {len(self.kegs)}\n'
                              f'Хотите зачеркнуть? y/n: \n')
        return self.is_correct_answer(player_answer, n)

    def is_correct_answer(self, answer, num):
        if answer == 'y':
            if num not in self.player1.nums:
                print(f'{self.player1.name} проиграл!')
                return False
            else:
                self.player1.cross_out_num(num)
        else:
            if num in self.player1.nums:
                print(f'{self.player1.name} проиграл!')
                return False
        self.player2.cross_out_num(num)
        if len(self.player1.nums) == 0:
            print(f'{self.player1.name} победил!')
            return False
        elif len(self.player2.nums) == 0:
            print(f'Компьютер выиграл!')
            return False
        return True

    def start(self):
        while True:
            result = self.rounds()
            if not result:
                break
