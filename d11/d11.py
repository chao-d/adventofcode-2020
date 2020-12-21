import utils.read_input as inp
import copy

lst = inp.to_origin_list()
board = [[c for c in line] for line in lst]
adjs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def simulate(board):
    row, col = len(board), len(board[0])
    tmp = copy.deepcopy(board)
    while True:
        changed = False
        board = copy.deepcopy(tmp)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'L':
                    found_occ = False
                    for adj in adjs:
                        curr_x, curr_y = i + adj[0], j + adj[1]
                        if 0 <= curr_x < row and 0 <= curr_y < col and \
                                board[curr_x][curr_y] == '#':
                            found_occ = True
                            break
                    if not found_occ:
                        tmp[i][j] = '#'
                        changed = True
                elif board[i][j] == '#':
                    num_adj_occ = 0
                    for adj in adjs:
                        curr_x, curr_y = i + adj[0], j + adj[1]
                        if 0 <= curr_x < row and 0 <= curr_y < col and \
                                board[curr_x][curr_y] == '#':
                            num_adj_occ += 1
                    if num_adj_occ >= 4:
                        tmp[i][j] = 'L'
                        changed = True
        if not changed:
            break
    return tmp


def count_occupied(board):
    row, col = len(board), len(board[0])
    count = 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == '#':
                count += 1
    return count


def simulate_dir(board):
    row, col = len(board), len(board[0])
    tmp = copy.deepcopy(board)

    while True:
        changed = False
        board = copy.deepcopy(tmp)
        for i in range(row):
            for j in range(col):
                if board[i][j] == '#':
                    num_occ = 0
                    for adj in adjs:
                        curr_x, curr_y = i + adj[0], j + adj[1]
                        while 0 <= curr_x < row and 0 <= curr_y < col and \
                                board[curr_x][curr_y] == '.':
                            curr_x, curr_y = curr_x + adj[0], curr_y + adj[1]
                        if 0 <= curr_x < row and 0 <= curr_y < col and \
                                board[curr_x][curr_y] == '#':
                            num_occ += 1
                            if num_occ >= 5:
                                break
                    if num_occ >= 5:
                        tmp[i][j] = 'L'
                        changed = True
                elif board[i][j] == 'L':
                    found_occ = False
                    for adj in adjs:
                        curr_x, curr_y = i + adj[0], j + adj[1]
                        while 0 <= curr_x < row and 0 <= curr_y < col and \
                                board[curr_x][curr_y] == '.':
                            curr_x, curr_y = curr_x + adj[0], curr_y + adj[1]
                        if 0 <= curr_x < row and 0 <= curr_y < col and \
                                board[curr_x][curr_y] == '#':
                            found_occ = True
                            break
                    if not found_occ:
                        tmp[i][j] = '#'
                        changed = True
        if not changed:
            break
    return tmp


if __name__ == "__main__":
    print(f'Part 1: {count_occupied(simulate(board))}')

    print(f'Part 2: {count_occupied(simulate_dir(board))}')
