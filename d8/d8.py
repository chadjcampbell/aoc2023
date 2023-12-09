def main():

    def part1():
        with open('real8.txt') as file:
            data = file.readlines()
        directions = data[0].strip()
        nodes = {}
        for i in range(2, len(data)):
            node, LR_string = data[i].strip().split('=')
            L, R = LR_string.split(',')
            nodes[node.strip()] = [L.strip()[1:], R.strip()[:-1]]
        start = 'AAA'
        end = 'ZZZ'
        current = start
        steps = 0
        while current != end:
            for dir in directions:
                if dir == 'L':
                    next = nodes[current][0]
                else:
                    next = nodes[current][1]
                steps += 1
                current = next
                if current == end:
                    break

        print(f'Part 1: {steps}')

    def part2():
        with open('real8.txt') as file:
            data = file.readlines()
        directions = data[0].strip()
        nodes = {}
        for i in range(2, len(data)):
            node, LR_string = data[i].strip().split('=')
            L, R = LR_string.split(',')
            nodes[node.strip()] = [L.strip()[1:], R.strip()[:-1]]
        starts = []
        for n in nodes.keys():
            if n.endswith('A'):
                starts.append(n)
        steps = 0
        for start in starts:
            current = start
            while not current.endswith('Z'):
                for dir in directions:
                    if dir == 'L':
                        next = nodes[current][0]
                    else:
                        next = nodes[current][1]
                    steps += 1
                    current = next
                    if current.endswith('Z'):
                        break

        print(f'Part 2: {steps}')

    part1()
    part2()


if __name__ == "__main__":
    main()
