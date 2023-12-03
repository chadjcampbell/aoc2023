def main():

    def part1():
        #326901 is too low
        #530537 too low
        #885057 wrong

        def is_symbol(c):
            return not c.isdigit() and c != '.'


        def get_num(coords, matrix):
            num = ''
            row,col = coords
            while True:
                if matrix[row][col-1].isdigit():
                    col-=1
                else:
                    break
            while True:
                num += matrix[row][col]
                if matrix[row][col+1].isdigit():
                    col+=1
                    continue
                else:
                    return num

        with open('d3real.txt') as file:
            matrix = [[column for column in rows.strip()] for rows in file]
            coords = []
            nums = []
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j].isdigit():
                        coords.append([i,j])
            skips = 0
            for c in coords:
                if skips:
                    skips-=1
                    continue
                adj = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
                for a in adj:
                    try:
                        if is_symbol(matrix[c[0]+a[0]][c[1]+a[1]]):
                            nums.append(int(get_num(c, matrix)))
                            itter=1
                            while matrix[c[0]][c[1]+itter].isdigit() and c[1]<len(matrix[0]):
                                skips+=1
                                itter+=1 
                            break
                    except IndexError:
                        continue
            print(sum(nums))

                    
                    

    def part2():
        with open('d3test.txt') as file:
            for line in file:
                ...

    part1()
    part2()


if __name__ == "__main__":
    main()
