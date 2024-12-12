"""Игра в крестики нолики!"""
from gameparts import Board
from gameparts.exceptions import FieldIndexError, CellOccupiedError


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.fieldsize:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.fieldsize:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print('Значение должно быть неотрицательным и меньше '
                      f'{game.fieldsize}.')
                print(
                    'Пожалуйста, введите значение для строки и столбца заново.'
                    )
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты.')
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                    )
                continue
            except Exception as e:
                print(f'Возникла ошибка {e}')
            else:
                break
        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        if game.check_win(current_player):
            result_str = f'Победили {current_player}.'
            print(result_str)
            save_result(result_str)
            running = False
        elif game.is_board_full():
            result_str = 'Ничья!'
            print(result_str)
            save_result(result_str)
            running = False
        current_player = "O" if current_player == 'X' else 'X'


def save_result(text):
    file = open('results.txt', 'a')
    file.write(text + '\n')


if __name__ == '__main__':
    main()
