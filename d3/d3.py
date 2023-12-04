def main():

    def part1():

        def is_symbol(c):
            return not c.isdigit() and c != '.'

        def check_part(num, matrix, row, end):
            start = end - len(num) + 1
            for i in range(3):
                for j in range(len(num)+2):
                    if -1+i+row >= 0 and -1+i+row < len(matrix) and -1+j+start >= 0 and -1+j+start < len(matrix[0]):
                        if is_symbol(matrix[-1+i+row][-1+j+start]):
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
        # 83245878 too low
        # ANSWER SHOULD BE 83279367

        def build_num(row, col, matrix):
            num = ''
            while True:
                if col-1 >= 0 and matrix[row][col-1].isdigit():
                    col -= 1
                else:
                    break
            while True:
                num += matrix[row][col]
                if col+1 < len(matrix[0]) and matrix[row][col+1].isdigit():
                    col += 1
                else:
                    return int(num)

        def check_part(row, col, matrix):
            nums = []
            adj = [[-1, -1], [-1, 0], [-1, 1],
                   [0, -1], [0, 1],
                   [1, -1], [1, 0], [1, 1]]
            for a in adj:
                if matrix[row+a[0]][col+a[1]].isdigit():
                    num = build_num(row+a[0], col+a[1], matrix)
                    if num not in nums:
                        nums.append(num)
            return nums

        with open('d3real.txt') as file:
            matrix = [[column for column in rows.strip()] for rows in file]
            nums = []
            for row_num, row in enumerate(matrix):
                for col_num, col in enumerate(row):
                    if col == '*':
                        parts = check_part(row_num, col_num, matrix)
                        if len(parts) == 2:
                            nums.append(parts[0]*parts[1])
            print(f'Part 2: {sum(nums)}')

    part1()
    part2()


if __name__ == "__main__":
    main()
