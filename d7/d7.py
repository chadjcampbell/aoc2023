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
        # 253755843 too high

        def compare_cards(card1, card2):
            card_order = 'AKQT98765432J'
            return card_order.index(card1) - card_order.index(card2)

        def rank_hand(counts, jokers):

            if jokers == 5 or max(counts) + jokers == 5:
                return 7
            if max(counts) + jokers == 4:
                return 6
            if max(counts) + jokers == 3 and 2 in counts:
                return 5
            if max(counts) + jokers == 3:
                return 4
            if (max(counts) + jokers == 2 and 2 in counts) or (max(counts) == 1 and jokers == 2):
                return 3
            if max(counts) + jokers == 2:
                return 2
            return 1

        def compare_hands(h1, h2):
            hand1, hand2 = h1['hand'], h2['hand']
            hand1_no_j = hand1.replace('J', '')
            hand2_no_j = hand2.replace('J', '')
            rank1 = rank_hand(
                sorted(list(Counter(hand1_no_j).values())), hand1.count('J'))
            rank2 = rank_hand(
                sorted(list(Counter(hand2_no_j).values())), hand2.count('J'))
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
                print(hands['hand'])
        print(f'Part 2: {sum}')
    part1()
    part2()


if __name__ == "__main__":
    main()
