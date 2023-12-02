def main():

    dict = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    def part1():
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
        with open('d1real.txt') as file:
            dict = {
                'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9',
                'zero': '0'
            }
            nums = []
            for line in file:
                start, end = 0, len(line)-1
                num1found, num2found = False, False
                num = ''
                str1 = ''
                str2 = ''
                while not num1found:
                    if line[start].isdigit():
                        num += line[start]
                        num1found = True
                        break
                    else:
                        str1 += line[start]
                    for s in dict:
                        if s in str1:
                            num += dict[s]
                            num1found = True
                            break
                    start += 1
                while not num2found:
                    if line[end].isdigit():
                        num += line[end]
                        num2found = True
                        break
                    else:
                        str2 = line[end] + str2
                    for s in dict:
                        if s in str2:
                            num += dict[s]
                            num2found = True
                            break
                    end -= 1
                nums.append(int(num))
            total = sum(nums)
            print(f'part2: {total}')

    part1()
    # part2()


if __name__ == "__main__":
    main()
