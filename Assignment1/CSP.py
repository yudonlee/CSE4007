from typing import get_origin


def is_nqueen_condition(next, col):
    if next in col:
        return False
    else:
        for i, item in enumerate(col, 0):
            # Nqueen과 대각선이 겹치는지 확인
            if (item == next - len(col) + i) or (item == next + len(col) - i):
                return False
    return True


dfs_finish = False
dfs_result = []


def search(n_queen, col):
    global dfs_finish, dfs_result
    if dfs_finish:
        return
    if(len(col) == n_queen):
        dfs_finish = True
        dfs_result = col
        return

    for next in range(1, n_queen + 1):
        if(is_nqueen_condition(next, col)):
            appended_col = col[:]
            appended_col.append(next)
            search(n_queen, appended_col)


def csp(n_queen):
    global dfs_finish, dfs_result
    result = []
    for i in range(1, n_queen + 1):
        col = [i]
        if not dfs_finish:
            search(n_queen, col)
        else:
            result = dfs_result
            dfs_finish = False
            dfs_result = []
            break

    return result
