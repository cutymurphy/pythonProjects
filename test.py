# 1---------------------------------------------------------------------------------------------------
import task5 as task5

r1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19][2:-2]
print(r1)

# 2---------------------------------------------------------------------------------------------------
def fibonacci(n):
    a, b = 0, 1
    i = 1
    while i <= n:
        yield b
        a, b = b, a + b
        i += 1
fibonacci_seq = []
for i in fibonacci(7):
    fibonacci_seq.append(i)
print(tuple(fibonacci_seq))

# 3---------------------------------------------------------------------------------------------------
generator_expr = (val for val in [14, 20, 18, 81, 30, 9, 45, 62, 100] if val % 3 == 0)
print(generator_expr)
# print([val for val in [14, 20, 18, 81, 30, 9, 45, 62, 100] if val % 3 == 0])

# 4---------------------------------------------------------------------------------------------------
import random as rnd

def unstable(func):
    def wrapper(*args, **kwargs):
        if rnd.randint(0, 1) < 1:
            return None
        else:
            return func(*args, **kwargs)
    return wrapper

@unstable
def add(a, b):
    return a + b

res = add(8, 10)
print(res)

# 5---------------------------------------------------------------------------------------------------
m = [[14, 12, 3],
     [11, 2, 9],
     [14, 30, 18],
     [17, 8, 20]]
c1 = list(map(lambda row: row[0], m))
print(c1)


# 6---------------------------------------------------------------------------------------------------
print([list(c) for c in zip(*m)])


# 7---------------------------------------------------------------------------------------------------
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def eq(self, other):
        return self.x == other.x and self.y == other.y

    @property
    def quarter(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x > 0 and self.y < 0:
            return 4
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        else:
            return 0

p1 = Point(-1, -1)
p2 = Point(1, 1)
print(p1.distance_to(p2))
print(p1.eq(p2))
print(p1.quarter, p2.quarter)



class IterableIterator:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

it = IterableIterator(2, 8)
print(list(it))


def generator():
    i = 1
    while (i <= 10):
        yield i
        i += 1
for i in generator():
    print(i)


import random
colors = ['red', 'green', 'yellow', 'cyan']
print(colors)
random.shuffle(colors)
print(colors.pop(0))


def shift_row_left(array, row_index):
    row = array[row_index]
    first_elem = row[0]
    row[0] = row[1]
    row[1] = row[2]
    row[2] = row[3]
    row[3] = first_elem

arr = [[1, 2, 3, 4], [1, 2, 3, 4]]
print(arr)
task5.Logic.Logicshift_col_up()
print([list(c) for c in zip(*arr)][0])