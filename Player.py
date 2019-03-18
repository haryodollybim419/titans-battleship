import random


class Player:
    """Represents any player that can play the game."""
    def __init__(self):
        """ Initializes the Player class.
        """
        self.score = []  # Keeps track of the battleships that have been hit.
        self.placements = [[], [], [], [], [], [], [], [], [], []]  # [x][y] Computer's battleship in grid format
        for i in range(10):
            for j in range(10):
                self.placements[i].append(0)
        self.battleship_set = []  # Computer's battleship in (start_x, start_y, end_x, end_y, length) format
        self.selection_history = []  # Keeps track of computer's selection to prevent repeats.

    def get_total_score(self):
        """" Sums up the total score obtained by the Player.
        Input variables:
            self: The Player object
        Returns:
            total(integer): Summation of score """
        total = 0
        for ship_length in range(len(self.score)):
            total += ship_length

        return total

    def avoid_plots(self, plot_list):
        """ Adds plot to the player's selection history to prevent guessing in invalid locations.
        This function is called when a battleship has been hit. The plot_list will consist of the
        remaining plots of the battleship.
        Input variables:
            plot_list: A list of tuples in format (x,y) which represent plots that must be avoided.
        Returns:
            None"""
        for plot in plot_list:
            self.selection_history.append(plot)

    def valid_location(self, grid, x, y, ship_len, ship_orientation):
        """ Determines whether ship with length ship_len and orientation ship_orientation can be placed in grid at x,y.
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

