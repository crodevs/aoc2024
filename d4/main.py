def main():
    print(part1("test.txt"))

def part1(filename: str) -> int:
    lines: list[str] = []
    x_list: list[tuple] = []
    row = 0
    col = 0

    for l in get_next_line(filename):
        lines.append(l)
        for c in l:
            if c == 'X':
                x_list.append((row, col))
            col += 1
        row += 1
        col = 0

    total = 0
    for x in x_list:
        # right
        print(lines[x[0]][x[1]:x[1] + 4])
        if lines[x[0]][x[1]:x[1] + 4] == "XMAS":
            total += 1
        # left
        elif lines[x[0]][x[1] - 4:x[1]:-1] == "XMAS":
            total += 1
        # up 
        elif [line[x[1]] for line in lines[x[0]:x[0] - 4:-1] if x[0] >= 3] == "XMAS":
            total += 1
        # down
        elif [line[x[1]] for line in lines[x[0]:x[0] + 4] if x[0] <= 6] == "XMAS":
            total += 1
        # diag up left
        elif [line[x[1] - 4] for line in lines[x[0]:x[0] - 4:-1] if x[0] >= 3 and x[1] >= 3] == "XMAS":
            total += 1
        # diag up right
        elif [line[x[1] + 4] for line in lines[x[0]:x[0] - 4:-1] if x[0] >= 3 and x[1] <= 6] == "XMAS":
            total += 1
        # diag down left
        elif [line[x[1] - 4] for line in lines[x[0]:x[0] + 4] if x[0] <= 6 and x[1] >= 3] == "XMAS":
            total += 1
        # diag down right
        elif [line[x[1] + 4] for line in lines[x[0]:x[0] + 4] if x[0] <= 6 and x[1] <= 6] == "XMAS":
            total += 1

    return total

def get_next_line(filename: str):
    with open(filename, "r") as file:
        for line in file:
            yield line

if __name__ == "__main__":
    main()