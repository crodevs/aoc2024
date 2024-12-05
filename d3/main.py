def main():
    print(part1("input.txt"))
    print(part2("input.txt"))

def part2(filename: str) -> int:
    mul_stack: list[chr] = []
    total = 0
    num1 = ""
    num2 = ""
    enabled = True

    for c in get_next_char(filename):

        if ''.join(mul_stack[-4:]) == "do()":
            mul_stack = mul_stack[-4:]
            enabled = True

        if ''.join(mul_stack[-7:]) == "don't()":
            mul_stack = mul_stack[-7:]
            enabled = False

        if ''.join(mul_stack[-4:]) == "mul(":
            if c == ',':
                mul_stack.append(c)
                continue
            if not c.isdigit():
                num1 = ""
                num2 = ""
                mul_stack.clear()
                continue
            num1 += c
            continue

        if ''.join(mul_stack[-5:]) == "mul(,":
            if c == ')':
                mul_stack.append(c)
                continue
            if not c.isdigit():
                num1 = ""
                num2 = ""
                mul_stack.clear()
                continue
            num2 += c
            continue

        if ''.join(mul_stack[-6:]) == "mul(,)":
            if enabled:
                total += int(num1) * int(num2)

            num1 = ""
            num2 = ""
            mul_stack.clear()

        mul_stack.append(c)

    return total

def part1(filename: str) -> int:
    mul_stack: list[chr] = []
    total = 0
    num1 = ""
    num2 = ""

    for c in get_next_char(filename):

        if ''.join(mul_stack[-4:]) == "mul(":
            if c == ',':
                mul_stack.append(c)
                continue
            if not c.isdigit():
                num1 = ""
                num2 = ""
                mul_stack.clear()
                continue
            num1 += c
            continue

        if ''.join(mul_stack[-5:]) == "mul(,":
            if c == ')':
                mul_stack.append(c)
                continue
            if not c.isdigit():
                num1 = ""
                num2 = ""
                mul_stack.clear()
                continue
            num2 += c
            continue

        if ''.join(mul_stack[-6:]) == "mul(,)":
            total += int(num1) * int(num2)
            num1 = ""
            num2 = ""
            mul_stack.clear()

        mul_stack.append(c)

    return total

def get_next_char(filename: str) -> chr:
    with open(filename, "r") as file:
        for line in file:
            for c in line:
                yield c

if __name__ == "__main__":
    main()