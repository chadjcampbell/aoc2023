def main():
    def part1():

        def map_seeds(seeds, maps, key):
            for idx, seed in enumerate(seeds):
                for map in maps[key]:
                    dmin = map[0]
                    smin = map[1]
                    smax = map[1] + map[2]
                    if seed >= smin and seed <= smax:
                        diff = seed - smin
                        seeds[idx] = dmin + diff
            return seeds

        with open('real5.txt') as file:
            data = file.readlines()
            seed_string = data[0].split()[1:]
            seeds = [int(num) for num in seed_string]
            maps = {}
            map_num = 0
            for line in data:
                if 'seeds' not in line and len(line) > 1:
                    if ':' in line:
                        map_num += 1
                        maps[f'map{map_num}'] = []
                    else:
                        maps[f'map{map_num}'].append(
                            [int(n) for n in line.split()])
            for key in maps.keys():
                seeds = map_seeds(seeds, maps, key)

        print(f'Part 1: {min(seeds)}')

    def part2():
        ...

    part1()
    part2()


if __name__ == "__main__":
    main()
