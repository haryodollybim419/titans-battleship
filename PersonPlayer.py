import pygame
from pygame.locals import *

class PersonPlayer:
    """ PersonPlayer represents the human that ComputerPlayer will play against.
    """

    def __init__(self):
        """ Initializes the PersonPlayer class.
        """
        self.score = []  # Keeps track of the battleships that have been hit.
        self.placements = []  # Log of all the person's battleship
        self.selection_history = []  # Keeps track of person's selection to prevent repeats.

    def get_total_score(self):
        """" Sums up the total score obtained by the PersonPlayer.
        Input variables:
            self: The PersonPlayer object
        Returns:
            total(integer): Summation of score """
        total = 0
        for ship_length in range(len(self.score)):
            total += ship_length
        return total

    def is_finished_game(self, event_type):
        """ Given the event_type, returns whether or not the PersonPlayer's click represented an exit from the game.
         Returns:
             True or False depending on the event_type"""
        return (event_type == QUIT) or (event_type == KEYDOWN and event_key == K_ESCAPE)

    def get_user_click(self):
        """ Represents the PersonPlayer's click.
         Guesses will not repeat.
         Returns:
             (x,y) coordinate of guess."""
        pygame.init()
        running = True
        coordinates=(-1,-1)
        clicks=5
        while running:
            for event in pygame.event.get():
                if self.is_finished_game(event.type):
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    coordinates = pygame.mouse.get_pos()
                    self.set_battleship(clicks)
                    clicks = clicks - 1
                if clicks == 0:
                    running = False
        if coordinates==(-1,-1):
            print("Invalid box selected, please try again")
        return coordinates

    def set_location(self):
        """ Represents the PersonPlayer's guesses.
         Guesses will not repeat.
         Returns:
             (x,y) coordinate of guess."""
        coordinates=self.get_user_click()
        if coordinates == (-1,-1):
            return coordinates
        if coordinates not in self.selection_history:
            self.selection_history.append((x, y))
            return (x, y)

    def set_battleship(self, length):
        """ Plots one of PersonPlayer's battleship with size: length.

        Adds a list of 5 elements to the placements list. Each element represents the battleship \
        using the format:
        (start_x, start_y, end_x, end_y, size)

        """
        start_x=self.set_location[0]
        start_y=self.set_location[1]
        end_x=self.set_location[0]+size-1
        end_y=self.set_location[1]+size-1
        self.placements.append((start_x, start_y, end_x, end_y, length))  # Ship of size length at plot (start_x, start_y) to (end_x, end_y) (vertical).

