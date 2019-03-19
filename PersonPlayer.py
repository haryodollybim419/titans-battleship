from Player import Player

class PersonPlayer(Player):
    """ PersonPlayer represents the human that ComputerPlayer will play against.
    """

    def __init__(self):
        """ Initializes the PersonPlayer class.
        """
        super().__init__()

    def set_battleship(self, x_head, y_head, battleship_length):
        """ Plots one of PersonPlayer's battleship with size: length starting at coordinate (x_head, y_head).

        Adds a list of 5 elements to the placements list. Each element represents the battleship using the format:
        (start_x, start_y, end_x, end_y, size)

        """
        validity = 0
        h_or_v = -1 #-1 represents the battleships orientation being undecided
        if ((x_head + battleship_length - 1 < 10)):
            h_or_v = 0 #0 represents the battleships orientation being horizontal
            validity = self.valid_location(self.placements, x_head, y_head, battleship_length, h_or_v)
        elif ((y_head - battleship_length - 1 >= 0)):  # Ship is within board
            h_or_v = 1 #1 represents the battleships orientation being vertical
            validity = self.valid_location(self.placements, x_head, y_head, battleship_length, h_or_v)
            
        if validity == 1:  # Adding this battleship into internal board and battleship_set array
            self.update_internal_board(self.placements, x_head, y_head, battleship_length, h_or_v)
            if h_or_v == 0:
                self.battleship_set.append(
                    (x_head, y_head, x_head + battleship_length - 1, y_head, battleship_length))
            else:
                self.battleship_set.append(
                    (x_head, y_head, x_head, y_head - battleship_length + 1, battleship_length))

        return self.battleship_set
