import re


def main():

    def part1():

        def is_symbol(c):
            return not c.isdigit() and c != '.'

        def check_part(num, matrix, row, end):
            start = end - len(num) + 1
            print(num)
            for i in range(3):
                for j in range(len(num)+2):
                    if -1+i+row >= 0 and -1+i+row < len(matrix) and -1+j+start >= 0 and -1+j+start < len(matrix[0]):
                        print(matrix[-1+i+row][-1+j+start])
                        if is_symbol(matrix[-1+i+row][-1+j+start]):
                            print('ding!')
                            return True
            return False

        with open('d3real.txt') as file:
            matrix = [[column for column in rows.strip()] for rows in file]
            nums = []
            for row_num, row in enumerate(matrix):
                num = ''
                for idx, col in enumerate(row):
                    if col.isdigit():
                        num += col
                    else:
                        if num.isdigit() and check_part(num, matrix, row_num, idx-1):
                            nums.append(int(num))
                        num = ''
                        continue
                    # have to check numbers at the end of the line!
                    if col.isdigit() and num.isdigit() and check_part(num, matrix, row_num, idx-1) and idx == len(row)-1:
                        nums.append(int(num))

            print(f'Part 1: {sum(nums)}')

    def part2():
        with open('d3test.txt') as file:
            for line in file:
                ...

    part1()
    part2()


if __name__ == "__main__":
    main()
