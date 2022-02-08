board = {1:'_', 2:'_', 3:'_', 4:'_', 5:'_', 6:'_', 7:'_', 8:'_', 9:'_'}

def print_board():
    print(board[1], board[2], board[3])
    print(board[4], board[5], board[6])
    print(board[7], board[8], board[9])

def move_zero_cross(symbol):
    print()
    print_board()
    if symbol == 'O':
        print("Ход игрока 'O' ")
    else:
        print("Ход игрока 'X' ")
    n = input('Введите номер клетки (1 - 9): ')
    try:
        n = int(n)
    except Exception:
        print('!!! Недопустимый символ')
        return move_zero_cross(symbol)
    if n not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print('!!! Неверный индекс')
        return move_zero_cross(symbol)
    elif board[n] != '_':
        print('!!! Эта клетка уже занята')
        return move_zero_cross(symbol)
    else:
        board[n] = symbol

win_table = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7)
)

def winner():
    for option in win_table:
        if board[option[0]] == board[option[1]] == board[option[2]] == 'O':
            return 'O'
        elif board[option[0]] == board[option[1]] == board[option[2]] == 'X':
            return 'X'

def dead_heat():
    dead_heat_list = [board[n] == 'O' or board[n] == 'X' for n in range(1, 10)]
    if all(dead_heat_list):
        return True

def game(symbol_start):
    symbol = symbol_start
    move_zero_cross(symbol)
    if winner() == symbol:
        print_board()
        print(f"Выиграл '{symbol}' ")
    elif dead_heat():
        print_board()
        print('Ничья')
    else:
        if symbol == 'X':
            symbol = 'O'
        else:
            symbol = 'X'
        move_zero_cross(symbol)
        if winner() == symbol:
            print_board()
            print(f"Выиграл '{symbol}' ")
        elif dead_heat():
            print_board()
            print('Ничья')
        else:
            return game(symbol_start)

def instruction():
    print('Нумерация клеток на поле:')
    print('1 2 3\n4 5 6\n7 8 9')
    print('Чтобы сделать ход, введите номер клетки')
    print('Удачи!')
    print()

def start():
    print('Кто начнёт игру?')
    symbol_start = input("Введите 'X' или 'O': ")
    if symbol_start != 'X' and symbol_start != 'O':
        print('!!! Недопустимый символ')
        print()
        return start()
    else:
        return symbol_start

instruction()
game(start())