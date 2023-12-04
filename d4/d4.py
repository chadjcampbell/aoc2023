def main():
    def part1():
        with open('real4.txt') as file:
            total = 0
            for line in file:
                score = 0
                _, nums = line.split(':')
                win_nums, card_nums = nums.split('|')
                winners = win_nums.split()
                card = card_nums.split()
                for win in winners:
                    if win in card:
                        if score == 0:
                            score += 1
                        else:
                            score *= 2
                total += score

        print(f'Part 1: {total}')

    part1()


if __name__ == '__main__':
    main()
