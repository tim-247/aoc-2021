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
        if direction.lower() not in directions:
            raise ValueError(f"Invalid direction. Valid directions are: {directions}")
        else:
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

        print(f"Moving: forward {value}")
        self.hpos += value


    def move_up(self, value:int) -> None:

        print(f"Attempting move: up {value}")
        if self.vpos - value < 0:
            raise ValueError("Invalid move: would move sub above surface")
        else:
            print("Successful move")
            self.vpos -= value
    

    def move_down(self, value:int) -> None:

        print(f"Moving: down {value}")
        self.vpos += value


    def report_position(self) -> tuple:

        return (self.hpos, self.vpos)


class AdvancedSubmarine(Submarine):
    """
    Advanced submarine class for part 2 of the puzzle
    """

    def __init__(self, hpos: int = 0, vpos: int = 0, aim:int = 0) -> None:
        super().__init__(hpos=hpos, vpos=vpos)
        self.aim = aim
        print(f"Sub aim: {aim}")
    

    def move_down(self, value: int) -> None:
        print(f"Adding {value} to aim")
        self.aim += value
    

    def move_up(self, value: int) -> None:
        print(f"Subtracting {value} from aim")
        self.aim -= value
    

    def move_forward(self, value: int) -> None:
        print(f"Attempting move forward {value}, aim {self.aim}")
        if self.vpos + self.aim * value < 0:
            raise ValueError("Invalid move: would move sub above surface")
        else:
            print("Successful move")
            self.vpos += self.aim * value
            self.hpos += value
            print(f"New position: {self.report_position()}")


def process_line(line: tuple, sub: Submarine) -> None:

    directions = line.split(' ')
    sub.move(directions[0], int(directions[1]))


def main():
    sub_1 = Submarine()
    sub_2 = AdvancedSubmarine()
    lines = [ line for line in sys.stdin ] 

    print("Executing part 1")
    for line in lines:
        try:
            process_line(line.rstrip(), sub_1)
        except Exception as e:
            print(e)
    
    print(f"Final position: {sub_1.report_position()}")
    print(f"Product: {prod(sub_1.report_position())}")

    print("Executing part 2")
    for line in lines:
        try:
            process_line(line.rstrip(), sub_2)
        except Exception as e:
            print(e)
    
    print(f"Final position: {sub_2.report_position()}")
    print(f"Product: {prod(sub_2.report_position())}")


if __name__ == "__main__":
    main()
