import random

class AutomaticPlayer:
    """ AutomaticPlayer represents the computer that an actual \
    user will play against.
    """

    def __init__(self):
        """ Initializes the AutomaticPlayer class.
        """
        self.score = []  # Keeps track of the battleships that have been hit.
        self.placements = [[], [], [], [], [], [], [], [], [], []]  # [x][y] Computer's battleship in grid format
        for i in range(10):
            for j in range(10):
                self.placements[i].append(0)
        self.battleship_set = []  # Computer's battleship in (start_x, start_y, end_x, end_y, length) format
        self.selection_history = []  # Keeps track of computer's selection to prevent repeats.

    def get_total_score(self):
        """" Sums up the total score obtained by the AutomaticPlayer.
        Input variables:
            self: The AutomaticPlayer object
        Returns:
            total(integer): Summation of score """
        total = 0
        for ship_length in range(len(self.score)):
            total += ship_length

        return total

    def guess_location(self):
        """ Represents the AutomaticPlayer's guesses.
         Guesses will not repeat.
         Returns:
             (x,y) coordinate of guess."""
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if (x, y) not in self.selection_history:
                self.selection_history.append((x, y))
                return (x, y)

    def valid_location(self, grid, x, y, ship_len, ship_orientation):
        """ Determines whether ship with length ship_len and orientation ship_orientation can be placed in grid at x,y.
        Helper function for set_battleships.
        Input variables:
            grid: A double array that represents the board
            x: Integer representing x location of the battleship's head
            y: Integer representing y location of the battleship's head
            ship_len: The length of the battleship
            ship_orientation: Will be 0 if horizontal, 1 if vertical
        Returns:
            Bool: 1 if valid, 0 if not valid"""
        if ship_orientation == 0:  # Horizontal ship
            for column in grid[x: x + ship_len]:
                if column[y] == 1:
                    return 0
        else:  # Vertical ship, x is constant
            for row in range(y-ship_len + 1, y+1):
                if grid[x][row] == 1:
                    return 0
        return 1

    def update_internal_board(self, grid, x, y, ship_len, ship_orientation):
        """Once determined that the location is valid, we will update grid to contain newly placed battleship.
        Helper function for set_battleships.
        Input variable:
            grid: A double array that represents the board
            x: Integer representing x location of the battleship's head
            y: Integer representing y location of the battleship's head
            ship_len: The length of the battleship
            ship_orientation: Will be 0 if horizontal, 1 if vertical
        Returns:
            null"""
        if ship_orientation == 0:  # Horizontal ship
            for column in grid[x: x + ship_len]:
                column[y] = 1
        else:  # Vertical ship, x is constant
            for row in range(y-ship_len + 1, y + 1):
                grid[x][row] = 1

    def set_battleships(self):
        """ Plots all of AutomaticPlayer's battleship. Should only be called once.
        Will plot the following ships:
        1. Battleship length: 5
        2. Battleship length: 4
        3. Battleship length: 3
        4. Battleship length: 2
        5. Battleship length: 1

        It updates the object variable battleship_set, which is a list of 5 elements.
        Each element represents the battleship \
        using the format:11
        (start_x, start_y, end_x, end_y, size)
        """
        battleship_length = 1
        while battleship_length < 6:
            h_or_v = random.randint(0, 1)  # If 0, the battleship will be horizontal. If 1, it will be vertical.
            validity = 0  # Obtaining a valid x y
            while validity == 0:
                x_head = random.randint(0, 9)
                y_head = random.randint(0, 9)
                if ((h_or_v == 0 and (x_head + battleship_length - 1 < 10)) or
                        (h_or_v == 1 and (y_head - battleship_length - 1 >= 0))):  # Ship is within board
                    validity = self.valid_location(self.placements, x_head, y_head, battleship_length, h_or_v)
                    if validity == 1:  # Adding this battleship into internal board and battleship_set array
                        self.update_internal_board(self.placements, x_head, y_head, battleship_length, h_or_v)
                        if h_or_v == 0:
                            self.battleship_set.append(
                                (x_head, y_head, x_head + battleship_length - 1, y_head, battleship_length))
                        else:
                            self.battleship_set.append(
                                (x_head, y_head, x_head, y_head - battleship_length + 1, battleship_length))
            battleship_length = battleship_length + 1
        return self.battleship_set


