import re


def main():
    def part1():
        with open('test5.txt') as file:
            data = file.readlines()
            seed_string = data[0].split()[1:]
            seeds = [int(num) for num in seed_string]
            print(seeds)
            maps = []
            map_num = 0
            for idx, line in enumerate(data):
                if 'seeds' not in line:
                    if ':' in line:
                        map += 1

    def part2():
        ...

    part1()
    part2()


if __name__ == "__main__":
    main()
