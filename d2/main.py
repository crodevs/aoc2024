
def main():
    print(part1("input.txt"))
    print(part2("input.txt"))

def part2(filename: str) -> str:
    reports: list[str] = []

    for line in get_next_line(filename):
        reports.append(line)

    safe_count = 0
    for r in reports:
        report = r.split()
        prev_level = int(report[0])
        prev_diff = 0
        safe = True

        print(r.split())
        # while not end of line
        # if prev and cur fails: pop and try again
        # if we fail again: fail whole report
        dampened = False
        i = 1
        while i < len(report):
            cur_level = int(report[i])
            diff = prev_level - cur_level
            print(f"{prev_level}, {cur_level}")
            i += 1

            if diff == 0:
                print("diff was 0")
                safe = False
                break
            if diff > 0 and prev_diff < 0:
                print("diff prev_diff mismatch")
                safe = False
                break
            if diff < 0 and prev_diff > 0:
                print("diff prev_diff mismatch")
                safe = False
                break
            if abs(diff) > 3:
                print("diff > 3")
                safe = False
                break

            print(f"{prev_level} and {cur_level} passed")

            prev_level = cur_level
            prev_diff = diff
            safe = True

        if safe: 
            print(f"{r.split()} was safe")
            safe_count += 1


    return safe_count

def part1(filename: str) -> str:
    reports: list[str] = []

    for line in get_next_line(filename):
        reports.append(line)

    safe_count = 0
    for r in reports:
        report = r.split()
        prev_level = int(report[0])
        prev_diff = 0
        safe = True

        for i in range(len(report)):
            if i == 0:
                continue

            cur_level = int(report[i])
            diff = prev_level - cur_level

            if diff == 0:
                safe = False
                break
            if diff > 0 and prev_diff < 0:
                safe = False
                break
            if diff < 0 and prev_diff > 0:
                safe = False
                break
            if abs(diff) > 3:
                safe = False
                break

            prev_level = cur_level
            prev_diff = diff
            safe = True

        if safe: 
            safe_count += 1

    return safe_count

        
def get_next_line(filename: str):
    with open(filename, "r") as file:
        for line in file:
            yield line
            

if __name__ == "__main__":
    main()