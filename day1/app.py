import os

def count_depth_increases(lines: list) -> int:
    count_increases = 0
    for index, li in enumerate(lines):
        if index < len(lines) - 1:
            if li < lines[index+1]:
                count_increases += 1
    return count_increases


def main():
    with open(os.getcwd() + '/input.txt', 'r') as input:
        inputlist = [ int(line) for line in input.read().splitlines() ]

    print(count_depth_increases(inputlist))
    

if __name__ == "__main__":
    main()
