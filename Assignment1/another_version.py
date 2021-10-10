import os
import BFS
import CSP
import HC


def main():
    input_path = "input.txt"
    input_file = open(input_path, "r")
    output_file = open("output.txt", "w")

    for line in input_file:
        case = line.split()
        number = int(case[0])
        result = []
        if case[1] == 'bfs':
            result = BFS.bfs(number)
        elif case[1] == 'csp':
            result = CSP.csp(number)
        elif case[1] == 'hc':
            result = HC.hc(number)
        if not result:
            output_file.write("No solution\n")
        else:
            list_to_str = [str(item) for item in result]
            list_to_str = ", ".join(list_to_str) + "\n"
            output_file.write(list_to_str)
    output_file.close()


if __name__ == "__main__":
    main()
