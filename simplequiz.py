import random
x = 0
y = 0
answer = 0
wrong = False
while not wrong:
    x = random.randint(0, 12)
    y = random.randint(0, 12)
    answer = int(input(f'{x} * {y} = '))
    if not answer == x * y:
        wrong = True
