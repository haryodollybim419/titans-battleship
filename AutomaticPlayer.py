import random


class AutomaticPlayer:
    """ AutomaticPlayer represents the computer that an actual \
    user will play against.
    """

    def __init__(self):
        """ Initializes the AutomaticPlayer class.
        """
        self.score = []  # Keeps track of the battleships that have been hit.
        self.placements = []  # Log of all the computer's battleship
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

    def set_battleships(self):
        """ Plots all of AutomaticPlayer's battleship.
        Will plot the following ships:
        1. Battleship length: 5
        2. Battleship length: 4
        3. Battleship length: 3
        4. Battleship length: 2
        5. Battleship length: 1

        Returns list of 5 elements. Each element represents the battleship \
        using the format:
        (start_x, start_y, end_x, end_y, size)

        Note that this is hard coded for now.
        """
        self.placements.append((5, 5, 5, 5, 1))  # Ship of size 1 at plot (5,5)
        self.placements.append((9, 9, 9, 5, 5))  # Ship of size 5 at plot (9,9) to (9,5)- vertical.
        self.placements.append((0, 9, 3, 9, 4))  # Ship of size 4 at plot (0,9) to (3,9) - Horizontal
        self.placements.append((0, 2, 0, 0, 3))  # Ship of size 3 at plot (0,2) to (0,0) - Vertical
        self.placements.append((8, 0, 9, 0, 2))  # Ship of size 2 at plot (8,0) to (9,0) - horizontal


