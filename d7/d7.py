from collections import Counter
import functools


def main():
    def part1():

        def compare_cards(card1, card2):
            card_order = 'AKQJT98765432'
            return card_order.index(card1) - card_order.index(card2)

        def rank_hand(counts):
            if 5 in counts:
                return 7
            if 4 in counts:
                return 6
            if 3 in counts and 2 in counts:
                return 5
            if 3 in counts:
                return 4
            if 2 in counts:
                counts.pop()
                if 2 in counts:
                    return 3
                else:
                    return 2
            return 1

        def compare_hands(h1, h2):
            hand1, hand2 = h1['hand'], h2['hand']
            rank1 = rank_hand(sorted(list(Counter(hand1).values())))
            rank2 = rank_hand(sorted(list(Counter(hand2).values())))
            if rank1 != rank2:
                return rank2 - rank1
            for (card1, card2) in zip(hand1, hand2):
                card_comparison = compare_cards(card1, card2)
                if card_comparison != 0:
                    return card_comparison
            return 0

        with open('real7.txt') as file:
            data = []
            for line in file:
                strings = line.strip().split()
                data.append({'hand': strings[0], 'score': int(strings[1])})
            sorted_data = sorted(data, key=functools.cmp_to_key(
                compare_hands), reverse=True)
            sum = 0
            for idx, hands in enumerate(sorted_data):
                sum += hands['score']*(idx+1)
        print(f'Part 1: {sum}')

    def part2():
        with open('test7.txt') as file:
            ...
        print(f'Part 2:')

    part1()
    part2()


if __name__ == "__main__":
    main()
