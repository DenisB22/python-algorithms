def set_queen(row, col, queens_map):
    queens_map[row][col] = '*'


def remove_queen(row, col, queens_map):
    queens_map[row][col] = '-'


def can_place_queen(row, col, left_diagonal, right_diagonal, rows, cols, left_diagonals, right_diagonals):
    if row not in rows and col not in cols and left_diagonal not in left_diagonals and right_diagonal not in right_diagonals:
        return True


def put_queens(row, rows, cols, left_diagonals, right_diagonals, queens_map):
    if row == 8:
        for row in queens_map:
            print(' '.join(row))
        print()
        return

    for col in range(8):
        left_diagonal = row - col
        right_diagonal = row + col

        if can_place_queen(row, col, left_diagonal, right_diagonal, rows, cols, left_diagonals, right_diagonals):
            rows.add(row)
            cols.add(col)
            left_diagonals.add(left_diagonal)
            right_diagonals.add(right_diagonal)

            set_queen(row, col, queens_map)
            put_queens(row + 1, rows, cols, left_diagonals, right_diagonals, queens_map)
            remove_queen(row, col, queens_map)

            rows.remove(row)
            cols.remove(col)
            left_diagonals.remove(left_diagonal)
            right_diagonals.remove(right_diagonal)


queens_map = [['-' for x in range(8)] for y in range(8)]

put_queens(0, set(), set(), set(), set(), queens_map)