import random
from sales import Points


def test_1_percent():
    points = Points(random.randint(1, 99))
    assert points.sale, 0.01


def test_3_percent():
    points = Points(random.randint(100, 199))
    assert points.sale, 0.03


def test_5_percent():
    points = Points(random.randint(200, 499))
    assert points.sale, 0.05


def test_10_percent():
    points = Points(random.randint(500, 10000))
    assert points.sale, 0.1
