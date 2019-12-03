from operator import add, mul
codes = {1: add, 2: mul}


def run_intcode(position, input):
    opcode = input[position]
    if opcode == 99:
        return input

    lookup1 = input[position + 1]
    lookup2 = input[position + 2]
    lookup3 = input[position + 3]
    if len(input) <= lookup1 | len(input) <= lookup2 | len(input) <= lookup3:
        return [0]

    op = codes[opcode]
    input[lookup3] = op(input[lookup1], input[lookup2])

    return run_intcode(position + 4, input)


def gravity_assist(input):
    for x in range(99, 0, -1):
        for y in range(99, 0, -1):
            attempt = input.copy()
            attempt[1] = x
            attempt[2] = y
            result = run_intcode(0, attempt)

            if result[0] == 19690720:
                print(f'x: {x}, y: {y}')
                return result


def main():
    with open("input.txt", encoding='utf-8') as f:
        input = list(map(int, f.readline().split(',')))
        result = gravity_assist(input)
        print(result)


# 152702
# 4576384
if __name__ == "__main__":
    main()
