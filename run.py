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
        self.score = 0

        # Creates the board without showing ships positions
        for i in range(size):
            self.board.append(["O"] * size)

        # Creates randomly the ships position
        for i in range(ships):
            row, col = self._generate_ship_location()
            self.ship_row.append(row)
            self.ship_col.append(col)

    def play(self):
        """
        Method that starts the game and allows player to play
        It will keep asking for coordinates till valid ones are chosen.
        """
        print("Let's play!\n")
        self.print_board()
        for turn in range(self.turns):
            print("Turn", turn + 1,"\n")
            while True:
                guess_row = int(input(f"Guess row (0-{self.size - 1})"))
                guess_col = int(input(f"Guess column (0-{self.size - 1})"))
                t = self.validate_choice(guess_row, guess_col)

                if t:
                    print("\nFire!!\n")
                    self.board[guess_row][guess_col] = "X"  # changes the O into X
                    break

            for i in range(self.ships):
                if guess_row == self.ship_row[i] and guess_col == self.ship_col[i]:
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
            
            self.print_board()

            if self.score == self.ships:
                print("You destroyed all the ships! Good job!!\n")
                break

    def validate_choice(self, guess_row, guess_col):
        """
        Checks if choices input are valid 
        """
        try:   
            if (guess_row < 0 or guess_row >= self.size 
                or guess_col < 0 or guess_col >= self.size):
                raise ValueError(f"Please insert a value between 0 and {self.size - 1}")
            elif self.board[guess_row][guess_col] == "X":
                raise ValueError(f"You shot here already! {guess_row} {guess_col}")
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.")
            return False
        return True

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


size = int(input("How many rows and columns would you like to create? "))
ships = int(input("How many ships would you like to be on the board? "))
turns = int(input("How many turns would you like to have to play? "))

game = Battleship(size, ships, turns)
game.play()
