def main():

    def all_zeros(arr):
        for a in arr:
            if a != 0:
                return False
        return True

    def part1():

        def get_next(nums):
            if all_zeros(nums):
                return 0
            diffs = []
            for i in range(1, len(nums)):
                diffs.append(nums[i]-nums[i-1])
            nums.append(nums[-1] + get_next(diffs))
            return nums[-1]

        history = []
        with open('real9.txt') as file:
            for line in file:
                strings = line.strip().split()
                ints = [int(x) for x in strings]
                history.append(ints)

        sum = 0
        for nums in history:
            next = get_next(nums)
            sum += next
        print(f'Part 1: {sum}')

    def part2():

        def get_prev(nums):
            if all_zeros(nums):
                return 0
            diffs = []
            for i in range(1, len(nums)):
                diffs.append(nums[i]-nums[i-1])
            nums.insert(0, nums[0] - get_prev(diffs))
            return nums[0]

        history = []
        with open('real9.txt') as file:
            for line in file:
                strings = line.strip().split()
                ints = [int(x) for x in strings]
                history.append(ints)

        sum = 0
        for nums in history:
            prev = get_prev(nums)
            sum += prev
        print(f'Part 2: {sum}')

    part1()
    part2()


if __name__ == "__main__":
    main()
