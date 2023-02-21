import random

def game(field):
    try:
        y, x = input().split()
        x = int(x)
        y = int(y)
    except ValueError:
        print("Введите числа")
        return 1
    try:
        if field[x][y] is None:
            field[x][y] = "x"
    except IndexError:
        print("Неправильные координаты")
        return 1
    if 
    while True:
        temp_x = random.randint(0, 2)
        temp_y = random.randint(0, 2)
        if field[temp_x][temp_y] is None:
            field[temp_x][temp_y] = "o"
            break
        else:
            continue
    

field = [[None, None, None],
        [None, None, None],
        [None, None, None]]

while game(field):
    pass

print(field)