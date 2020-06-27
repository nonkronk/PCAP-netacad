def is_sudoku(num_list):
    row_list = num_list
    col_list = create_col_list(num_list)
    x_list = create_x_list(num_list)
    valid_list = True
    for i in range(9):
        check = is_valid(row_list[i], col_list[i], x_list[i])
        valid_list *= check
        if not valid_list:
            return False
    return True

def create_col_list(num_list):
    col_list = []
    for r in range(9):
        col = ''
        for c in range(9):
            col += num_list[c][r]
        col_list.append(list(col))
    return col_list

def create_x_list(num_list):
    x_list = []
    for xr in range(0, 9, 3):
        for xc in range(0, 9, 3):
            x = ''
            for r in range(3):
                for c in range(3):
                    x += num_list[r + xr][c + xc]
            x_list.append(list(x))
    return x_list

def is_valid(r, c, x):
    for i in range(9):
        n = str(i+1)
        if n not in r or n not in c or n not in x:
            return False
    return True

if __name__ == '__main__':
    num_list = []
    for i in range(9):
        row = input()
        num_list.append(list(row))
    msg = 'Yes' if is_sudoku(num_list) else 'No'
    print(msg)
