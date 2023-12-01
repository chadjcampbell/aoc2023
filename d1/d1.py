def main():


    def part1():
        with open('d1real.txt') as file:
            nums = []
            for line in file:
                s,e = 0,len(line)-1
                num = ''
                while True:
                    if line[s].isdigit():
                        num += line[s]
                        break
                    s+=1
                while True:
                    if line[e].isdigit():
                        num += line[e]
                        break
                    e-=1
                nums.append(int(num))
            total = sum(nums)
            print(f'part1: {total}')


    def part2():
        with open('d1test.txt') as file:
            strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            help_dict = {
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
                start,end = 0,len(line)-1
                num = ''
                str1 = ''
                str2 = ''
                while True:
                    if line[start].isdigit():
                        num += line[start]
                        break
                    else:
                        str1 += line[start]
                    for s in strings:
                        if s in str1:
                            num+=help_dict[s]
                            break
                    start+=1
                while True:
                    if line[end].isdigit():
                        num += line[end]
                        break
                    else:
                        str2 += line[end]
                    for s in strings:
                        if s in str2:
                            num+=help_dict[s]
                            break
                    end-=1
                nums.append(int(num))
            total = sum(nums)
            print(f'part2: {total}')


    part1()
    part2()
                    


if __name__ == "__main__":
    main()