from time import sleep
from threading import Thread, Lock
from random import randint

lock = Lock()

class Bank():
    def __init__(self, balance = 0):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            donat = randint(50,500)
            self.balance += donat
            if self.balance >= 500 and lock.locked():
                lock.release()

            print(f'Пополнение: {donat}. Баланс: {self.balance}')
            sleep(0.001)
        return self.balance

    def take(self):
        for _ in range(100):
            donat = randint(50,500)
            print(f'Запрос на {donat}')

            if self.balance >= donat:
                self.balance -= donat
                print(f'Снятие: {donat}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')

            sleep(0.001)
        return self.balance

Hoper = Bank()

deposit_donat = Thread(target = Hoper.deposit, args = ())
deposit_take = Thread(target = Hoper.take, args = ())

deposit_donat.start()
deposit_take.start()
deposit_donat.join()
deposit_take.join()

print(f"Итоговый баланс: {Hoper.balance}")


















