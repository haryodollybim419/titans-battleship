import pygame
from AutomaticPlayer import*
from VisibleBoard import*
from PersonPlayer import*
from Stats import*
import time
import random

FPS = 30
HEIGHT = 1000
WIDTH = 500
P_SHIPS = []
BORDER_WIDTH = 235
BORDER_HEIGHT = 35
REQ_SHIP_SIZE = 40
MAX_SCORE = 5
MOUSE_POS_X = 430
MOUSE_POS_Y = 130
RESTRICT_X = 775
RESTRICT_Y = 475
MARGIN = 5
SIZE = 30


class Start(pygame.sprite.Sprite):
    """ Start(controller) utilizes all the\
    object classes of the game.
    NOTE: This follows the MVC architecture design protocols
    as this class also represents the view part and controller of MVC.
    """

    def __init__(self, auto, person, stats, vboard, vb_auto, vb_player, p_ships):
        """ Initializes the start class with .
        auto: represents the computers(ai) aspect of the game.
        person: represents the human player aspect of the game.
        stats: represents the status of the game.
        vboard: represents the visual board showned on the screen.
        vb_auto: represents the computers(ai) board.
        vb_player: represents the human player's bpoard.
        p_ships: a list of ships coordinates for the computer to guess.
        """
        super(Start, self).__init__()
        self.auto = auto
        self.stats = stats
        self.person = person
        self.vboard = vboard
        self.vb_auto = vb_auto
        self.vb_player = vb_player
        self.win = (False, "")
        self.player1_score = 0 #human player is player 1
        self.player2_score = 0 #computer is player 2
        self.turns = 0 #0 means the human player turn to play, 1 means its the computers turn.
        self.p_ships = p_ships # a list of ships
        self.guesses = 0
        

    def set_auto_ships(self):
        """ Set the ships  at valid
        coordinates for human player to guess.
        """
        ships = self.auto.set_battleships()
        for enemy_ships in ships:
                self.vb_auto.add_ship(enemy_ships[0], enemy_ships[1],\
                                     enemy_ships[2], enemy_ships[3], enemy_ships[4])

    def set_person_ships(self):
        """ Set the ships  at valid
        coordinates for computer player to guess.
        NOTE: This is based on the list of ships P_SHIPS
        the human player choosed.
        """
        ships = self.p_ships
        for person_ships in ships:
                self.vb_player.add_ship(person_ships[0], person_ships[1],\
                                     person_ships[2], person_ships[3], person_ships[4])
          
                
    def play_ai(self):
        """Let's the computer player
        to be able to guess the human player's ship
        at valid positions, ensuring the same coordinates
        is chosen only once.
        """
        pos = self.auto.guess_location()
        no_go = self.update(self.vb_player, pos[0], pos[1])
        if no_go == None:
            no_go = []
        if no_go != []:
            self.player2_score = self.player2_score + 1
        self.auto.avoid_plots(no_go)
        
    def update(self, obj, coord_x, coord_y):
        """updates the screen based on
        guesses made by the human player or the computer player

        obj: represents an object that can either be an human player
        or the computer player.
        coord_x: coordinate for the row
        coor_y: coordinate for the column

        returns moves made.
        """
        no_go = obj.viewable_move(coord_x, coord_y)
        return no_go
                
        
    def display_score(self):
        """Display the human player and computer player's score.
        """
        font = pygame.font.SysFont(""'couriernew'"", 19)
        font.set_bold(True)
        mess_1 = "Player score: {}".format(self.player1_score)
        mess_2 = "Computer score: {}".format(self.player2_score)
        txt1 = font.render(mess_1, True, (0, 128, 0))
        txt2 = font.render(mess_2, True, (0, 128, 0)) 
        self.vboard.blit(txt1, (150, 100))
        self.vboard.blit(txt2, (500, 100))

    def set_border(self):
        """Display a blue borderline around the
        human player's board and the computer player's board.
        """
        pygame.draw.rect(self.vboard, BLUE, pygame.Rect(10, 10, HEIGHT - BORDER_WIDTH, WIDTH - BORDER_HEIGHT), 3)    
        


    def display_stats(self):
        """Show the important information about both players:
        1) Number of ships
        2)Remaining ships
        3)Number of guesses
        4) Scores of both players when a ship is hit.
        """
        font = pygame.font.SysFont("agencyfb", 25)
        mess_1 = "Number of ships: "
        mess_2 = "Remaining ships: "
        mess_3 = "Numbers of guesses: {}".format(self.guesses)
        txt1 = font.render(mess_1, True, (0, 127, 0))
        txt2 = font.render(mess_2, True, (0, 127, 0))
        txt3 = font.render(mess_3, True, (0, 127, 0))
        play_score_msg1 = font.render("Player1: {}  Computer: {}".format(MAX_SCORE, MAX_SCORE), True, (0, 127, 0))
        play_score_msg2 = font.render("Player1: {}  Computer: {}".format(MAX_SCORE - self.player1_score, MAX_SCORE - self.player2_score), True, (0, 127, 0))
        self.vboard.blit(txt1, (800, 100))
        self.vboard.blit(txt2, (800, 200))
        self.vboard.blit(txt3, (800, 300))
        self.vboard.blit(play_score_msg1, (810, 130))
        self.vboard.blit(play_score_msg2, (810, 230))

    def quit(self):
        """To exit the game.
        """
        pygame.quit()
        sys.exit()

#NOTE: this aspect of the file(Begin class) is mainly for the welcome screen of Start class.
class Begin:
    """ Begin represents the welcome screen,
    where the human player can hide ships from the computer player.
    """

    def __init__(self, player_board, user_board, person):
        """ Initializes the begin class with:
        player_board: represents the visual part from Start class.
        person: represents the human player from Start class.
        user_board: represents the visual board from Start class.
        """
        self.player_board = player_board
        self.user_board = user_board
        self.person = person
        self.required_ships = [5, 4, 3, 2, 1] #numbers of ships(5 ships) needed to play the game.
        self.num_set_ships = 0

    def show_required(self, color, index):
        """ Show the required ships needed for the human player
        to hide the ships.
        color: to highlight what ship as being used. In this case
        the color is red.
        index: the set of ships required.
        """
        x = 5
        for row in range(5):
            for column in range(x):
                if index == x:
                    pygame.draw.rect(self.player_board,
                                 color,
                                 pygame.Rect(800+(REQ_SHIP_SIZE * column), 200+(REQ_SHIP_SIZE * row), 30, 30))
                else:
                    pygame.draw.rect(self.player_board,
                                     WHITE,
                                     pygame.Rect(800+(REQ_SHIP_SIZE * column), 200+(REQ_SHIP_SIZE * row), 30, 30))
            x -= 1
            
    def set_player_ships(self, x_head, y_head, battleship_length):
        """ Set the player ships  at valid
        coordinates for the computer player to guess.
        x_head: column position
        y_head: row position
        battleship_length: length of ship. eg 5 if the ship is of length 5.
        """
        person = self.person.set_battleship(x_head, y_head, battleship_length)
        if(len(person) > 0):
            person_ships = person[-1]
            self.user_board.add_ship(person_ships[0], person_ships[1],\
                                         person_ships[2], person_ships[3], person_ships[4])
            P_SHIPS.append((person_ships[0], person_ships[1],\
                                         person_ships[2], person_ships[3], person_ships[4]))

    
    def display_info(self):
        """ Show what is required for the human player to do.
        """
        title = pygame.font.SysFont("ocraextended", 40)
        font = pygame.font.SysFont("'couriernew'", 19)
        font.set_bold(True)
        main_title = title.render("Battle of the Titans", True, (0, 128, 0))
        self.player_board.blit(main_title, (145, 40))
        txt1 = font.render("1. Set Battleship locations", True, (0, 128, 0))
        txt2 = font.render("2. Press any key to start game", True, (0, 128, 0))
        self.player_board.blit(txt1, (50, 150))
        self.player_board.blit(txt2, (50, 250))
        font = pygame.font.SysFont("couriernew", 17)
        mess_1 = "Required ships: "
        font.set_bold(True)
        txt1 = font.render(mess_1, True, (0, 127, 0))
        self.player_board.blit(txt1, (800, 150))
        
        

    def update(self, human_player, coord_x, coord_y):
        """
        updates the screen based on
        guesses made by the human player only.

        human_player: represents the human player object.
        coord_x: coordinate for the row
        coor_y: coordinate for the column
        """
        human_player.viewable_move(coord_x, coord_y)

    def set_border(self):
        """Display a blue borderline around the
        human player's board alone.
        """
        pygame.draw.rect(self.player_board, BLUE, pygame.Rect(10, 10, HEIGHT - BORDER_WIDTH, WIDTH - BORDER_HEIGHT), 3)

    
def main():      
    pygame.init()
    DISPLAY=pygame.display.set_mode((1000,500),0,32)
    DISPLAY.fill(BLACK)
    pygame.display.set_caption("BattleShip--1.0")
    user_board = VisibleUserBoard(DISPLAY)
    person = PersonPlayer()

    begin = Begin(DISPLAY, user_board, person)
    begin.display_info()
    begin.set_border()
    begin.show_required(WHITE, 0)

    begin.num_set_ships = 0 #numbers of battleship bricks can not be more than 15
    def mouse_event(event, start, size):
        """handle mouse events and ensures mouse clicks
        only works on the grid coordinates.
        start: The object or present screen.
        size: Size of a single brick coordinate.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if MOUSE_POS_X <= mouse_pos[0] <= RESTRICT_X and MOUSE_POS_Y <= mouse_pos[1] <= RESTRICT_Y:
                col = mouse_pos[0] - MOUSE_POS_X
                rw = mouse_pos[1] - MOUSE_POS_Y
                column = col // (size + MARGIN)
                row = rw // (size + MARGIN)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('jump.wav'))
                if len(begin.required_ships) > 0:
                    begin.set_player_ships(column, row, begin.required_ships[0])
                    popped_val = begin.required_ships.pop(0)
                    begin.show_required(RED, popped_val)
                    begin.num_set_ships += 1
            else:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('Buzzer.wav'))
                
    pygame.mixer.music.load('look.wav')
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and begin.num_set_ships >= 5:
                run = False
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('look.wav')
                pygame.mixer.music.play()
            n_event = mouse_event(event, begin, 30) #called the mouse event function
        pygame.display.update()
    
    

if __name__ == '__main__':
    def mouse_event(mouse_pos, start):
        """handle mouse events and ensures mouse clicks
        only works on the grid coordinates.
        start: The object or present screen.
        """
        if REQ_SHIP_SIZE <= mouse_pos[0] <= (RESTRICT_X - 390) and MOUSE_POS_Y <= mouse_pos[1] <= RESTRICT_Y:
            col = mouse_pos[0] - REQ_SHIP_SIZE
            rw = mouse_pos[1] - MOUSE_POS_Y
            column = col // (SIZE + MARGIN)
            row = rw // (SIZE + MARGIN)
            no_go = start.update(start.vb_auto, column, row)
            if no_go != None and no_go != []:
                start.player1_score = start.player1_score + 1
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('jump.wav'))
            start.guesses += 1
            start.turns = 1
            
    stats = Stats()
    auto = AutomaticPlayer()
    person = PersonPlayer()
    main()
    
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    DISPLAY=pygame.display
    main_board = DISPLAY.set_mode((HEIGHT, WIDTH),0,32)
    main_board.fill(BLACK)
    DISPLAY.set_caption("BattleShip--1.0")
    user_board = VisibleUserBoard(main_board)
    enemy_board = VisibleEnemyBoard(main_board)
    
    start = Start(auto, person, stats, main_board, enemy_board, user_board, P_SHIPS);
    start.set_auto_ships()
    start.set_border()
    start.set_person_ships()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('look.wav'))
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    win = 0 #end game if equal to 1

    running = True
    while running:
        #events handler
        for event in pygame.event.get():
            start.display_score()
            start.display_stats()
            if event.type==QUIT:
                start.quit()
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('look.wav')
                pygame.mixer.music.play()
            if win == 0:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if start.turns == 0:
                        m_event = mouse_event(mouse_pos, start)
                        if start.vb_auto.all_ships_sunk():
                            pygame.draw.rect(start.vboard,BLACK,
                            pygame.Rect(315, 80, 40, 40))

                            pygame.draw.rect(start.vboard,BLACK,
                            pygame.Rect(680, 80, 40, 40))

                            pygame.draw.rect(start.vboard, BLACK,
                            pygame.Rect(800, 230, 300, 30))
                        

                            start.display_score()
                            start.display_stats()
                            title = pygame.font.SysFont("'couriernew'", 40)
                            title.set_bold(True)
                            main_title = title.render("Player wins!", True, (0, 128, 0))
                            main_board.blit(main_title, (210, 40))
                            start.display_score()
                            start.display_stats()
                            win = 1
                        pygame.draw.rect(start.vboard,BLACK,
                        pygame.Rect(960, 300, 40, 40))
                        
                    else:
                        start.play_ai()
                        if start.vb_player.all_ships_sunk():
                            pygame.draw.rect(start.vboard,BLACK,
                            pygame.Rect(315, 80, 40, 40))

                            pygame.draw.rect(start.vboard,BLACK,
                            pygame.Rect(680, 80, 40, 40))

                            pygame.draw.rect(start.vboard, BLACK,
                            pygame.Rect(800, 230, 300, 30))
                        
                            start.display_score()
                            start.display_stats()
                            title = pygame.font.SysFont("'couriernew'", 40)
                            title.set_bold(True)
                            main_title = title.render("Computer wins!", True, (0, 128, 0))
                            main_board.blit(main_title, (175, 40))
                            start.display_score()
                            start.display_stats()
                            win = 1
                        pygame.draw.rect(start.vboard,BLACK,
                            pygame.Rect(960, 300, 40, 40))
                        start.turns = 0

                    if (win == 0):
                        pygame.draw.rect(start.vboard,BLACK,
                        pygame.Rect(315, 80, 40, 40))

                        pygame.draw.rect(start.vboard,BLACK,
                        pygame.Rect(680, 80, 40, 40))

                        pygame.draw.rect(start.vboard, BLACK,
                            pygame.Rect(800, 230, 300, 30))
                
        pygame.display.flip()
        clock.tick(FPS) #set limit of fps to 30 frame/sec
        
            
