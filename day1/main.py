import sys

"""
Solved generically. Pass block size as first command line argument. Default is 1.
"""


def count_depth_increases(lines: list, block_size: int=1) -> int:
    count_increases = 0
    blocks = []
    for index, line in enumerate(lines):
        block = (tuple(lines[index:index+block_size]))
        if len(block) == block_size:
            blocks.append(block)

    for index, block in enumerate(blocks):
        if index < len(blocks) -1 :
            if sum(block) < sum(blocks[index+1]):
                count_increases += 1

    return count_increases


def main():
    block_size = int(sys.argv[1]) or 1
    inputlist = [ int(line.rstrip()) for line in sys.stdin ]

    print(count_depth_increases(inputlist, block_size))
    

if __name__ == "__main__":
    main()
