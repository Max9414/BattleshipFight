from random import randint


class Battleship:
    """
    Game class. The class will provide the player with the choice
    to create the grid with as many rows and columns he wants from
    a minimum of 4 to a maximum of 8, for playability reasons.
    """
    def __init__(self, size, ships, turns):
        self.size = size
        self.ships = ships
        self.turns = turns
        self.board = []
        self.ship_row = []
        self.ship_col = []

        for i in range(size):
            self.board.append(["O"] * size)


Battleship(5, 3, 5)