from random import randint


class Battleship:
    """
    Game class. The class will provide the player with the choice
    to create the grid with as many rows and columns he wants from
    a minimum of 4 to a maximum of 8, for playability reasons.
    """
    def __init__(self, board_size, nr_ships, nr_turns):
        print("start of init")
        self.size = board_size
        self.ships = nr_ships
        self.turns = nr_turns
        self.board = []
        self.pc_board = []
        self.ship_row = []
        self.ship_col = []
        self.ship_row_pc = []
        self.ship_col_pc = []
        self.score = 0

        # Creates the board without showing ships positions
        for i in range(self.size):
            self.board.append(["O"] * self.size)
            self.pc_board.append(["O"] * self.size)

        # Creates randomly the ships position for pc and player
        for i in range(self.ships):
            row, col = self._generate_ship_location()
            self.ship_row.append(row)
            self.ship_col.append(col)
            self.board[self.ship_row[i]][self.ship_col[i]] = "@"
            row, col = self._generate_ship_location()
            self.ship_row_pc.append(row)
            self.ship_col_pc.append(col)

        print("end of init")

    def play(self):
        """
        Method that starts the game and allows player to play
        It will keep asking for coordinates till valid ones are chosen.
        """
        print("Let's play!\n")
        self.print_boards()
        for turn in range(self.turns):
            print("\nTurn", turn + 1, "\n")
            choice = False
            while not choice:
                guess_row = int(input(f"Guess row (0-{self.size - 1})"))
                guess_col = int(input(f"Guess column (0-{self.size - 1})"))
                choice = self.validate_choice(guess_row, guess_col)

                if choice:
                    print("\nFire!!\n")
                    self.pc_board[guess_row][guess_col] = "X"  # changes the O into X
                    break

            for i in range(self.ships):
                if (guess_row == self.ship_row_pc[i] and
                    guess_col == self.ship_col_pc[i]):
                    hit = True
                    self.score += 1
                    break
                else:
                    hit = False

            if hit:
                print("Good Job! You hit a Battleship!!\n")
            else:
                if turn == self.turns - 1:
                    print("Nice try, your chances are over!")
                    break
                else:
                    print("Nice try, shoot again!\n")

            self.print_boards()

            if self.score == self.ships:
                print("You destroyed all the ships! Good job!!\n")
                break

    def validate_choice(self, guess_row, guess_col):
        """
        Checks if choices input are valid
        """
        try:
            guess_row = int(guess_row)
            guess_col = int(guess_col)
            if (guess_row < 0 or guess_row >= self.size or guess_col < 0 or guess_col >= self.size):
                raise ValueError(f"Please insert a value between 0 and {self.size - 1}")
            elif self.board[guess_row][guess_col] == "X":
                raise ValueError(f"You shot here already! {guess_row} {guess_col}")
        except Exception as e:
            print(f"Invalid data: {e}, please try again.")
            return False
        return True

    def _generate_ship_location(self):
        """
        Generate the random position of the ships,
        without showing it visually on the screen.
        """
        print("Generate ship start")
        while True:
            row = randint(0, self.size - 1)
            col = randint(0, self.size - 1)
            if row not in self.ship_row and col not in self.ship_col:
                return row, col
        print("End of generate ships")

    def _show_board(self, board):
        """
        Generate the board in a suitable way to play battleship.
        """
        for row in board:
            print(" ".join(row))

    def print_boards(self):
        """
        To avoid repetition, created method to print the boards
        to play the game that will be used at the beginning and
        end for the play metod
        """
        print("Your board\n")
        self._show_board(self.board)
        print("\nPC board\n")
        self._show_board(self.pc_board)


def check_inputs(choice):
    """
    Checker for input choices from player
    """
    while True:
        if choice >= 10 or choice < 3:
            choice = int(input("Please select a number between 3 and 9 "))
        else:
            print(f"{choice} selected")
            break
    return choice

while True:
    try:
        size = int(input("How many rows and columns would you like to create?\n "
                        "Please select a number between 3 and 9 "))
        size = check_inputs(size)
        ships = int(input("How many ships would you like to be on the board?\n "
                        "Please select a number between 3 and 9 "))
        ships = check_inputs(ships)
        turns = int(input("How many turns would you like to have to play?\n "
                        "Please select a number between 3 and 9 "))
        turns = check_inputs(turns)
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer value.")

print(size)
print(ships)
print(turns)
game = Battleship(size, ships, turns)
game.play()
