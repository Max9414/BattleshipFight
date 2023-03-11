from random import randint


class Battleship:
    """
    Game class. The class will provide the player with the choice
    to create the grid with as many rows and columns he wants from
    a minimum of 4 to a maximum of 8, for playability reasons.
    """

    def __init__(self, board_size, nr_ships, nr_turns):
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
        self.pc_score = 0

        # Creates the board without showing ships positions
        for i in range(self.size):
            self.board.append(["O"] * self.size)
            self.pc_board.append(["O"] * self.size)

        # Creates randomly the ships position for pc and player
        for i in range(self.ships):
            row, col = self._generate_ship_location(
                self.ship_row, self.ship_col
            )
            self.ship_row.append(row)
            self.ship_col.append(col)
            self.board[self.ship_row[i]][self.ship_col[i]] = "@"
            row, col = self._generate_ship_location(
                self.ship_row_pc, self.ship_col_pc
            )
            self.ship_row_pc.append(row)
            self.ship_col_pc.append(col)

    def play(self):
        """
        Starts the game and allows player to play
        It will keep asking for coordinates till valid ones are chosen.
        """
        print("Let's play!\n")
        self._print_boards()
        for turn in range(self.turns):
            print("\nTurn", turn + 1, "\n")
            not_selected = False
            while not not_selected:
                # if row and col already selected, the loop will continue
                choice = False
                while not choice:
                    # if choice is not correct, the loop will continue
                    guess_row = input(f"Select row (0-{self.size - 1})")
                    choice = self._validate_choice(guess_row)
                choice = False
                while not choice:
                    # if choice is not correct, the loop will continue
                    guess_col = input(f"Select column (0-{self.size - 1})")
                    choice = self._validate_choice(guess_col)

                # as value is already being checked, we can transorm
                # the values into integers
                guess_row = int(guess_row)
                guess_col = int(guess_col)

                # check if position has already been selected
                if self.pc_board[guess_row][guess_col] != "X":
                    not_selected = True
                else:
                    print("You shot here already, select again!")

                # if position has not been selected, shoots
                if not_selected:
                    print("\nFire!!\n")
                    self.pc_board[guess_row][
                        guess_col
                    ] = "X"  # changes the O into X

            for i in range(self.ships):
                if (
                    guess_row == self.ship_row_pc[i]
                    and guess_col == self.ship_col_pc[i]
                ):
                    hit = True
                    self.score += 1
                    break
                else:
                    hit = False

            if hit:
                print("Good Job! You hit a Battleship!!\n")

            if turn == self.turns - 1:
                print("Nice try, your chances are over!")
                break

            if not hit:
                print("Nice try, shoot again!\n")

            not_selected = False
            print("PC turn\n")
            while not not_selected:
                pc_row = randint(0, self.size - 1)
                pc_col = randint(0, self.size - 1)
                if self.board[pc_row][pc_col] != "X":
                    not_selected = True
                    self.board[pc_row][pc_col] = "X"
                    if self.board[pc_row][pc_col] == "@":
                        hit = True
                    else:
                        hit = False
            if hit:
                print(
                    f"The pc shot at the position {pc_row}, {pc_col} and hit a ship!\n "
                )
                self.pc_score += 1
            else:
                print(
                    f"The pc shot at the position {pc_row}, {pc_col} and ... splash! It's just water\n "
                )

            print(f"Your score is {self.score}\n")
            print(f"The pc score is {self.pc_score}\n")
            self._print_boards()

            if self.score == self.ships:
                print("You destroyed all the ships! Good job!!\n")
                break

    def _validate_choice(self, guess):
        """
        Checks if choices input are valid
        """
        try:
            guess = int(guess)
            if guess < 0 or guess >= self.size:
                raise ValueError(
                    f"the value must be between 0 and {self.size - 1}"
                )
            return True
        except Exception as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

    def _generate_ship_location(self, ship_row, ship_col):
        """Generate random position of the boats

        Args:
            ship_row (list): list of integers
            ship_col (list): list of integers

        Returns:
            int: int for row and column
        """
        while True:
            row = randint(0, self.size - 1)
            col = randint(0, self.size - 1)
            counter = 0
            if not ship_row:
                return row, col
            for j, i in zip(ship_row, ship_col):
                if row != j or col != i:
                    counter += 1
            if counter == len(ship_row):
                break
        return row, col

    def _show_board(self, board):
        """
        Generate the board in a suitable way to play battleship.
        """
        for row in board:
            print(" ".join(row))

    def _print_boards(self):
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
            choice = int(
                input("Invalid input, please select a number between 3 and 9 ")
            )
        else:
            print(f"{choice} selected")
            break
    return choice


while True:
    try:
        size = int(
            input(
                "How many rows and columns would you like to create?\n "
                "Please select a number between 3 and 9 "
            )
        )
        size = check_inputs(size)
        ships = int(
            input(
                "How many ships would you like to be on the board?\n "
                "Please select a number between 3 and 9 "
            )
        )
        ships = check_inputs(ships)
        turns = int(
            input(
                "How many turns would you like to have to play?\n "
                "Please select a number between 3 and 9 "
            )
        )
        turns = check_inputs(turns)
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer value.\n")


game = Battleship(size, ships, turns)
game.play()
