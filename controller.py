import pygame
from AutomaticPlayer import*
from Board import*
from Ship import*
from PersonPlayer import*
import time
import random


class Start(pygame.sprite.Sprite):
    def __init__(self, ship, board, auto, player):
        super(Start, self).__init__()
        self.ship = ship
        self.ship_stats =''
        self.auto = auto
        self.player = player
        self.total = self.auto.get_total_score()
        self.message = ''
        self.win = False
        self.board = board
        #space left for the splash screen info

    def set_splash_message(self, message):
        self.message = message

    def hide_ship(self):
        """
        hide ships automatically, randomly on the grid
        """
        self.message = message
        self.ship.set_battleships()
        

    def update(self, coords, size):
        """
        update the coordinates of the board
        giving the coords, and size of the board
        the coords that is coordinates are in a list
        of 4 elements:
            example: [2, 3, 4, 5] representing where the ship
            will be placed.
        """
        self.board.board_add_ship(coords[0], coords[1],\
                                  coords[2], coords[4], size)
        self.ship_stats.change_status()

    def quit_game(self):
        """
        end the game when the user quits the game
        """
        #will work more on this later
        self.win = True

    def end_game(self, event_type):
        self.player.is_finished_game(event_type)
        
        
        
        
        
#start the game
if __name__ == '__main__':
    ship = Ship()
    board = Board()
    auto = AutomaticPlayer()
    player = PersonPlayer()
    controller = Start(ship, board, auto, player)
    run = True
    while run:
        if controller.win:
            run = False
        #space left for running events
        time.sleep(4) #runs for 4 seconds
        run = False
        
        
        
        



