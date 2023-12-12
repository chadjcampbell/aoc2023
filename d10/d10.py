def main():

    def part1():
        def find_start(grid):
            for i, row in enumerate(grid):
                for j, cell in enumerate(row):
                    if cell == 'S':
                        return [i, j]

        def convert_start(start, grid):
            ...

        def find_next(cell, grid):
            ...

        with open('test10.txt') as file:
            grid = [[c for c in row.strip()]for row in file]
            grid.insert(0, ['.' for i in range(len(grid))])
            grid.append(['.' for i in range(len(grid)-1)])
            for row in grid:
                row.insert(0, '.')
                row.append('.')
            print(grid)
        start = find_start(grid)
        convert_start(start, grid)
        print(start)
        next = find_next(start, grid)
        steps = 0
        while next != start:
            next = find_next(next, grid)
            steps += 1

        print(f'Part 1: {steps/2}')

    def part2():
        with open('test10.txt') as file:
            ...
        print(f'Part 2: ')

    part1()
    part2()


if __name__ == "__main__":
    main()
