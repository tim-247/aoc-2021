def process_file(infile: str) -> dict:

    with open(infile, 'r') as input:
        lines = [ line.rstrip() for line in input ]
        numbers = lines[0].rstrip().split(',')
        boardlines = lines[1:]
        boards = [
            boardlines[i+1:i+6]  # noqa: E226
            for i in range(0, len(boardlines), 6)
        ]
        boards = [ [ line.split() for line in board ] for board in boards ]
        return { 'numbers': numbers, 'boards': boards}


def check_winner(drawn_numbers: list, board: list) -> tuple:

    lines = board
    columns = [
        [ line[index] for line in lines ]
        for index, char in enumerate(lines[0])
    ]
    to_check = lines + columns
    for line in to_check:
        if all (number in drawn_numbers for number in line):
            return (True, get_score(lines, drawn_numbers))
    return (False, None)


def get_score(to_check: list, drawn_numbers: list) -> int:

    unmarked_numbers = []
    for line in to_check:
        for num in line:
            if num not in drawn_numbers:
                unmarked_numbers.append(int(num))

    return (sum(unmarked_numbers) * int(drawn_numbers[-1]))


def part1(game: dict) -> None:

    game['drawn_numbers'] = [ game['numbers'].pop(0) ]
    # Check winners
    while len(game['numbers']) > 0:
        for board in game['boards']:
            if check_winner(game['drawn_numbers'], board):
                print(get_score(board, game['drawn_numbers']))
                game['numbers'] = []  # Triggers break in parent loop
        try:
            game['drawn_numbers'].append(game['numbers'].pop(0))
        except IndexError:
            break


def part2():
    pass


if __name__ == "__main__":

    game = process_file('day4/input.txt')
    part1(game)
