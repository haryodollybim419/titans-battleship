
from Player import Player
from Board import Board

"""The class Stats is used to display the stats of the game. It displays total number of
battleships, total number of remaining battleships in the game and the score of the player.
"""
class Stats():
    def __init__(self):
        """Initializes the Stats class.
        """
        self.score = 0
        self.number_of_ships = 0
        self.remaining_ships = 0

    def score(self):
        """Sets the score to the score of the player
        """
        self.score = Player.get_total_score()
        return self.score

    def number_of_ships(self):
        """Sets number_of_ships to the total number of ships in the game that the
        player has to guess
        """
        self.number_of_ships = Board.number_of_ships
        return self.number_of_ships

    def remaining_ships(self):
        """Sets the remaining_ships to the total number of ships remaining in the game
        for the player to guess
        """
        self.remaining_ships = Board.number_of_ships
        if Board.all_ships_sunk():
            self.remaining_ships = self.remaining_ships - 1
        return self.remaining_ships

    ##def display_all_stats(self): #copy in controller class 
        ##pygame.font.init() call this in start
        ##text = pygame.font.SysFont(pygame.font.get_default_font(),30)
        ##text_for_score = text.render("Total Score: " + self.score, False, (0,0,0))
        ##text_for_total_ships = text.render("Total number of ships: " + self.number_of_ships, False, (0,0,0))
        ##text_for_remaining_ships = text.render("Total number of remaining ships: " + self.remaining_ships, False, (0,0,0))
        ###screen.blit(text_for_score, position) #instead of screen, it will be the variable name we used to set the display mode
        ###screen.blit(text_for_total_ships, position)
        ###screen.blit(text_for_remaining_ships, position)
        
        
        

    

    
        
        
