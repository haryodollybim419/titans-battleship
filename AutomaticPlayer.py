import random
from Player import Player

class AutomaticPlayer(Player):
    """ AutomaticPlayer represents the computer that an actual \
    user will play against.
    """

    def __init__(self):
        """ Initializes the AutomaticPlayer class.
        """
        super().__init__()

    def guess_location(self):
        """ Represents the Player's guesses.
         Guesses will not repeat.
         Returns:
             (x,y) coordinate of guess."""
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if (x, y) not in self.selection_history:
                self.selection_history.append((x, y))
                return (x, y)

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
        using the format:
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


