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

    def part2():

        def get_wins(winners, card):
            win_count = 0
            for win in winners:
                if win in card:
                    win_count += 1
            return win_count

        with open('real4.txt') as file:
            data = file.readlines()
            card_counts = [1 for _ in range(len(data))]
            for i, line in enumerate(data):
                _, nums = line.split(':')
                win_nums, card_nums = nums.split('|')
                winners = win_nums.split()
                card = card_nums.split()
                wins = get_wins(winners, card)
                for _ in range(card_counts[i]):
                    for j in range(wins):
                        card_counts[i+j+1] += 1

        print(f'Part 2: {sum(card_counts)}')

    part1()
    part2()


if __name__ == '__main__':
    main()
