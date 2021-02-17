import random


class Sale:
    def __init__(self):
        self.sale = 0

    def __get__(self, instance, owner):
        if 0 < instance.points < 100:
            self.sale = 0.01
        elif 100 <= instance.points < 200:
            self.sale = 0.03
        elif 200 <= instance.points < 500:
            self.sale = 0.05
        elif instance.points >= 500:
            self.sale = 0.1
        return self.sale


class Points:
    sale = Sale()

    def __init__(self, points):
        self.points = points


if __name__ == '__main__':
    automate = Points(random.randint(0, 1000))
    price = 1000 - 1000 * automate.sale
    print(price)
