from math import prod
import sys


class Submarine():
    """
    Basic submarine class
    """


    def __init__(self, hpos:int = 0, vpos:int = 0) -> None:

        if vpos >= 0:
            self.vpos = vpos
        else:
            print(f"Vertical position {vpos} above surface. Moving to surface. Splash!")
            self.vpos = 0

        self.hpos = hpos
        print(f"Sub created at position: {self.report_position()}")

    
    def move(self, direction: str, value: int) -> None:

        directions = {"forward", "up", "down"}
        print(f"Trying to move {direction} {value}")
        if direction.lower() not in directions:
            raise ValueError(f"Invalid direction. Valid directions are: {directions}")
        else:
            print("Moved successfully")
            if direction.lower() == "forward":
                self.move_forward(value)
            elif direction.lower() == "up":
                try:
                    self.move_up(value)
                except ValueError as e:
                    print(e)
            elif direction.lower() == "down":
                self.move_down(value)
    

    def move_forward(self, value: int) -> None:

        self.hpos += value


    def move_up(self, value:int) -> None:

        if self.vpos - value < 0:
            raise ValueError("Invalid move: would move sub above surface")
        else:
            self.vpos -= value
    

    def move_down(self, value:int) -> None:

        self.vpos += value


    def report_position(self):

        return (self.hpos, self.vpos)


def process_line(line: tuple, sub: Submarine) -> None:

    directions = line.split(' ')
    sub.move(directions[0], int(directions[1]))


def main():
    my_sub = Submarine()

    for line in sys.stdin:
        try:
            process_line(line.rstrip(), my_sub)
        except Exception as e:
            print(e)
    
    print(f"Final position: {my_sub.report_position()}")
    print(f"Product: {prod(my_sub.report_position())}")


if __name__ == "__main__":
    main()
