def main():

    def part1():
        history = []
        with open('test9.txt') as file:
            for line in file:
                strings = line.strip().split()
                ints = [int(x) for x in strings]
                history.append(ints)
        for nums in history:
            ...
        print(history)
        print(f'Part 1: ')

    def part2():
        with open('test9.txt') as file:
            ...
        print(f'Part 2: ')

    part1()
    part2()


if __name__ == "__main__":
    main()
