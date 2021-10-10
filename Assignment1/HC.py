import random
MAX = 90000


def countOverlap(col, n_queen):
    # queen이 이동할 좌표, 원래 queen이 있는 장소.
    count = 0
    for index, item in enumerate(col, 0):
        for j in range(index + 1, n_queen):
            if col[j] == item:
                count += 1
            if col[j] == item + (j - index) or col[j] == item - (j - index):
                count += 1
    return count


def randomRestart(col, number):
    for i in col:
        i = random.randint(0, number - 1)


def findHeuristic(col, n_queen):
    h = MAX
    rows = []
    indexRow = 0
    indexCol = 0
    for i in range(0, n_queen):
        for j in range(0, n_queen):
            origin = col[j]
            col[j] = i
            count = countOverlap(col, n_queen)
            if(h > count):
                h = count
                indexRow = i
                indexCol = j
                rows = [(i, j)]
            elif h == count:
                rows.append([i, j])
            col[j] = origin

    index = random.choice(rows)
    indexRow = index[0]
    indexCol = index[1]
    col[indexCol] = indexRow

    return h


def hc(n_queen):
    if n_queen == 1:
        return [1]
    elif n_queen == 2 or n_queen == 3:
        return []
    col = [0 for i in range(n_queen)]
    randomRestart(col, n_queen)
    h = -1
    while h > 0 or h < 0:
        result = findHeuristic(col, n_queen)
        if(result == h):
            randomRestart(col, n_queen)
        else:
            h = result
    for i in range(0, n_queen):
        col[i] += 1
    return col
