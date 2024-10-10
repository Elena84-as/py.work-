from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        number_power= 100
        number_days = 0
        print(f'{self.name} , на нас напали!')
        for i in range(number_power):
            if number_power > 0:
                number_power -= self.power
                number_days += 1
                sleep(1)
                print(f'{self.name} сражается{number_days}дня  ,осталось {number_power} воинов.')
                if number_power < 0:
                    print(f'{self.name}одержал победу спустя{number_days}дней!')



first_knight = Knight('Sir Lancelot', 10)
second_knight =  Knight('Sir Galahad',20)


first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')

