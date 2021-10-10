class Queue():
    def __init__(self):
        self.queue = []

    def set_data(self, col):
        self.queue = col

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        pop_obj = None
        if not self.queue:
            print("Empty")
        else:
            pop_obj = self.queue[0]
            self.queue = self.queue[1:]
        return pop_obj

    def is_empty(self):
        if not self.queue:
            return True
        else:
            return False


def is_nqueen_condition(next, col, n_queen):
    if next in col:
        return False
    else:
        for i, item in enumerate(col, 0):
            # Nqueen과 대각선이 겹치는지 확인
            if (item == next - len(col) + i) or (item == next + len(col) - i):
                return False
    return True


def bfs(n_queen):
    if(n_queen == 1):
        return "1"

    queue = Queue()
    for i in range(1, n_queen + 1):
        queue.push([i])

    while not queue.is_empty():
        col = queue.pop()
        for next in range(1, n_queen + 1):
            appended_col = col[:]
            if is_nqueen_condition(next, col, n_queen):
                appended_col.append(next)
                if(len(appended_col) == n_queen):
                    return appended_col
                queue.push(appended_col)
