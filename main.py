field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
num = 0
def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()


def ask():
    while True:
        cords = input("     Сделайте Ваш ход: ").split()

        if len(cords) != 2:
            print(" Возможно ввести только две координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Возможно ввести только числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Данный координаты вне диапозона! ")
            continue

        if field[x][y] != " ":
            print(" Данная клетка занята... ")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))
                )
    for cord in win_cord:
        symbols = []
        for s in cord:
            symbols.append(field[s[0]][s[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

while True:
    num+=1

    show()

    if num % 2 == 1:
        print(" Ход крестиков ")
    else:
        print(" Ход ноликов ")

    x, y = ask()

    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if check_win():
        break

    if num == 9:
        print(" Ничья! ")
        break

def chek_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1,1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2 ), (1, 1), (2, )), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0 ), (2, 0)),
                ((0, 1), 1, 1), (2, 1), ((0, ), (1, 2), (2, 2))
    )

    for cord in win_cord:
        symbol = []
        for i in cord:
            symbol.append(field[i[0]][i[1]])
        if symbol == ["X","X","X"]:
            print(" Выиграл X !!! ")
            return True
        if symbol == ["0","0","0"]:
            print(" Выиграл 0 !!! ")
            return True

