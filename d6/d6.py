def main():

    def part1():
        with open('real6.txt') as file:
            data = file.readlines()
            _, times_str = data[0].split(':')
            _, dist_str = data[1].split(':')
            times = [int(t) for t in times_str.split()]
            dist = [int(d) for d in dist_str.split()]
            print(times)
            print(dist)
            answer = 1
            for idx, time in enumerate(times):
                wins = 0
                for i in range(time + 1):
                    speed = i
                    remaining_time = time - speed
                    traveled = speed * remaining_time
                    if traveled > dist[idx]:
                        wins += 1
                answer *= wins
        print(f'Part 1: {answer}')

    def part2():
        with open('test6.txt') as file:
            ...

    part1()
    part2()


if __name__ == "__main__":
    main()
