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

        for i in range(ships):
            row, col = self._generate_ship_location()
            self.ship_row.append(row)
            self.ship_col.append(col)

    def play(self):
        """
        Method that starts the game and allows player to play
        """
        print("Let's play!")
        self.print_board()
        print("Turn", self.turns - 1)
        guess_row = int(input("Guess row (0-{})".format(self.size - 1)))
        guess_col = int(input("Guess column (0-{})".format(self.size - 1)))
        print(guess_col)
        print(guess_row)

    def _generate_ship_location(self):
        """
        Generate the random position of the ships,
        without showing it visually on the screen.
        """
        while True:
            row = randint(0, self.size - 1)
            col = randint(0, self.size - 1)
            if row not in self.ship_row and col not in self.ship_col:
                return row, col

    def print_board(self):
        """
        Generate the board in a suitable way to play battleship.
        """
        for row in self.board:
            print(" ".join(row))


Battleship(5, 3, 5)