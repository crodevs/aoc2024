
def main():
    print(part1("input.txt"))
    print(part2("input.txt"))


def part1(filename: str) -> str:
    left_list: list[int] = []
    right_list: list[int] = []

    for line in get_next_line(filename):
        left_list.append(line.split()[0])
        right_list.append(line.split()[1])

    total = 0

    for j in range(len(right_list)):
        min_l = 99999
        min_r = 99999
        lindex = 0
        rindex = 0

        for i in range(len(left_list)):
            l = int(left_list[i])
            if l < min_l:
                min_l = l
                lindex = i

            r = int(right_list[i])
            if r < min_r:
                min_r = r
                rindex = i

        left_list.pop(lindex)
        right_list.pop(rindex)
        total += abs(min_l - min_r)

    return total

def part2(filename: str):
    left_list: list[int] = []
    right_list: list[int] = []

    for line in get_next_line(filename):
        left_list.append(line.split()[0])
        right_list.append(line.split()[1])

    total = 0
    num_l = -1

    for j in range(len(left_list)):
        rcount = 0

        if (num_l == int(left_list[j])):
            continue

        num_l = int(left_list[j])

        for i in range(len(right_list)):

            if num_l == int(right_list[i]):
                rcount += 1

        total += abs(num_l * rcount)

    return total
    
def get_next_line(filename: str):
    with open(filename, "r") as file:
        for line in file:
            yield line
            

if __name__ == "__main__":
    main()