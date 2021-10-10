import os
import BFS
import CSP
import HC


def makeOutput(number, result, case):
    outputPath = str(number) + "_" + case + "_output.txt"
    output_file = open(outputPath, "w")
    print(outputPath)
    if not result:
        output_file.write("No solution\n")
    else:
        list_to_str = [str(item) for item in result]
        list_to_str = ", ".join(list_to_str) + "\n"
        output_file.write(list_to_str)
    output_file.close()

def main():
    input_path = "input.txt"
    input_file = open(input_path, "r")

    for line in input_file:
        case = line.split()
        number = int(case[0])
        result = []
        if case[1] == 'bfs':
            result = BFS.bfs(number)
            makeOutput(number, result, 'bfs')
        elif case[1] == 'csp':
            result = CSP.csp(number)
            makeOutput(number, result, 'bfs')
        elif case[1] == 'hc':
            result = HC.hc(number)
            makeOutput(number, result, 'bfs')


if __name__ == "__main__":
    main()
