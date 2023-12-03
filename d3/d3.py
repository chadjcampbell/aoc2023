def main():

    def part1():
        with open('d3test.txt') as file:
            matrix = [[col for col in row.strip()] for row in file]
            print(matrix)

    def part2():
        with open('d3test.txt') as file:
            for line in file:
                ...

    part1()
    part2()


if __name__ == "__main__":
    main()
