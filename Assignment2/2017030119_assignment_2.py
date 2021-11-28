from os import stat
import random
# moving from [row][col]

immediate_reward = [0] * 25
reachable_state = []
bomb_state = []


def makeOutput(path, max_q):
    outputPath = "output.txt"
    output_file = open(outputPath, "w")

    list_to_str = [str(item) for item in path]
    list_to_str = " ".join(list_to_str) + "\n"
    output_file.write(list_to_str)
    output_file.write(str(max_q))
    output_file.close()


def not_out_of_range(row, col):
    if (row < 0 or row > 4 or col < 0 or col > 4):
        return False
    return True


def make_reachable_list():
    global reachable_state
    result = []
    for i in range(0, 5):
        for j in range(0, 5):
            input = []
            if i < 4:
                input.append((5 * (i + 1) + j))
            if j < 4:
                input.append((5 * i + j + 1))
            if i > 0:
                input.append((5 * (i - 1) + j))
            if j > 0:
                input.append((5 * i + j - 1))
            result.append(input)
    reachable_state = result


def max(next_state, q_learning_table):
    # action후 state에서 q_learing_table을 기준으로 max값을 출력한다.
    dest_list = reachable_state[next_state]

    result = 0

    for dest in dest_list:
        if q_learning_table[next_state][dest] > result:
            result = q_learning_table[next_state][dest]

    return result


def move(state, q_learning_table):
    global r, bomb_state

    next_state_list = reachable_state[state]

    next = random.choice(next_state_list)

    q_learning_table[state][next] = immediate_reward[next] + \
        r * max(next, q_learning_table)
    if next != 24 and next not in bomb_state:
        move(next, q_learning_table)


def search(start, path, q_learning_table):
    path.append(start)
    dest_list = reachable_state[start]

    next = -1
    result = 0

    if start != 24:
        for dest in dest_list:
            if q_learning_table[start][dest] > result:
                result = q_learning_table[start][dest]
                next = dest
        search(next, path, q_learning_table)


def main():
    global immediate_reward, reward_state, r, bomb_state
    input_path = "Assignment2/input.txt"
    # input_path = "Assignment2/input_ppt.txt"
    input_file = open(input_path, "r")
    r = 0.9
    map = []
    for line in input_file:
        map.append(line)

    q_learning_table = [[0] * 25] * 25
    make_reachable_list()

    for i in range(0, 5):
        for j in range(0, 5):
            if map[i][j] == 'B':
                immediate_reward[5 * i + j] = -100
                bomb_state.append(5 * i + j)
            elif map[i][j] == 'G':
                immediate_reward[5 * i + j] = 100
            elif map[i][j] == 'T':
                immediate_reward[5 * i + j] = 1

    for i in range(0, 10000):
        move(0, q_learning_table)

    path = []
    search(0, path, q_learning_table)
    print(path)
    print(max(0, q_learning_table))
    makeOutput(path, max(0, q_learning_table))


if __name__ == "__main__":
    main()
