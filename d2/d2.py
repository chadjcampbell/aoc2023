def main():

    def part1():
        dict = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        with open('d2real.txt') as file:
            nums = []
            for line in file:
                possible = True
                before_col, after_col = line.split(':')
                game_num = before_col.split(' ')[1]
                games = after_col.split(';')
                for g in games:
                    dice = g.split(',')
                    for d in dice:
                        d.strip()
                        dice_num, color = d.split()
                        if dict[color] < int(dice_num):
                            possible = False
                if possible:
                    nums.append(int(game_num))

            total = sum(nums)
            print(f'part1: {total}')

    def part2():
        with open('d2real.txt') as file:
            nums = []
            for line in file:
                dict = {
                    'red': 0,
                    'green': 0,
                    'blue': 0
                }
                _, after_col = line.split(':')
                games = after_col.split(';')
                for g in games:
                    dice = g.split(',')
                    for d in dice:
                        d.strip()
                        dice_num, color = d.split()
                        if dict[color] < int(dice_num):
                            dict[color] = int(dice_num)
                nums.append(dict['red']*dict['green']*dict['blue'])
            total = sum(nums)
            print(f'part2: {total}')

    part1()
    part2()


if __name__ == "__main__":
    main()
