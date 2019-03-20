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
MARGIN_ROW = 5
MARGIN_COL = 11
P_SHIPS = []

class Start(pygame.sprite.Sprite):
    #NOTE: vboard stands for visibleboard
    def __init__(self, auto, person, stats, vboard, vb_auto, vb_player, p_ships):
        super(Start, self).__init__()
        self.auto = auto
        self.stats = stats
        self.person = person
        self.vboard = vboard
        self.vb_auto = vb_auto
        self.vb_player = vb_player
        self.total_score = 0
        self.win = (False, "")
        self.player1_score = 0
        self.player2_score = 0 #computer is player 2
        self.turns = 0 #0 means the human player turn to play, 1 means the auto players turn.
        self.p_ships = p_ships # a list of ships
        self.guesses = 0
        

    def set_auto_ships(self):
        ships = self.auto.set_battleships()
        for enemy_ships in ships:
                self.vb_auto.add_ship(enemy_ships[0], enemy_ships[1],\
                                     enemy_ships[2], enemy_ships[3], enemy_ships[4])
                print("enemy ships: ",  enemy_ships)

    def set_person_ships(self):
        ships = self.p_ships
        for person_ships in ships:
                self.vb_player.add_ship(person_ships[0], person_ships[1],\
                                     person_ships[2], person_ships[3], person_ships[4])
                print("person ships: ",  person_ships)
          
                
    def play_ai(self):
        pos = self.auto.guess_location()
        no_go = self.update(self.vb_player, pos[0], pos[1])
        if no_go == None:
            no_go = []
        if no_go != []:
            self.player2_score = self.player2_score + 1
        self.auto.avoid_plots(no_go)
        print("auto: ", pos)
        #print("AUTO start: ", self.auto.selection_history)

    def update(self, obj, coord_x, coord_y):
        print("I was called on")
        print(coord_x, coord_y)
        no_go = obj.viewable_move(coord_x, coord_y)
        return no_go
        print("No go: ", no_go)
        
       
    def set_score(self, score, player):
        player.score.append(score)

    def set_winner(self, player_score, computer_score):
        winner = max(player_score, computer_score)
        self.win = (True, "Winner {} has won the game!".format(winner))
        
        
    def display_score(self):
        font = pygame.font.SysFont(""'couriernew'"", 19)
        font.set_bold(True)
        mess_1 = "Player score: {}".format(self.player1_score)
        mess_2 = "Computer score: {}".format(self.player2_score)
        txt1 = font.render(mess_1, True, (0, 128, 0))
        txt2 = font.render(mess_2, True, (0, 128, 0)) 
        self.vboard.blit(txt1, (150, 100))
        self.vboard.blit(txt2, (500, 100))

    def set_border(self):
        pygame.draw.rect(self.vboard, BLUE, pygame.Rect(10, 10, 1000 - 235, 500 - 35), 3)

    def indicate_winner(self):
        color = WHITE
        pygame.draw.rect(self.vboard,color,
                    pygame.Rect(200, 150, 400, 300))
        pygame.draw.rect(self.vboard, BLUE, pygame.Rect(200, 150,  400, 300), 3)
        font = pygame.font.SysFont("comicsansms", 35)
        mess_1 = "{}".format(self.win[1])
        txt1 = font.render(mess_1, True, (0, 128, 0))
        self.vboard.blit(txt1, (275, 280))
        
        


    def display_stats(self):
        font = pygame.font.SysFont("agencyfb", 25)
        #font.set_bold(True)
        mess_1 = "Number of ships: "
        mess_2 = "Remaining ships: "
        mess_3 = "Numbers of guesses: {}".format(self.guesses)
        #print("guesses: ", self.guesses)
        txt1 = font.render(mess_1, True, (0, 127, 0))
        txt2 = font.render(mess_2, True, (0, 127, 0))
        txt3 = font.render(mess_3, True, (0, 127, 0))
        play_score_msg1 = font.render("Player1: {}  Computer: {}".format(5, 5), True, (0, 127, 0))
        play_score_msg2 = font.render("Player1: {}  Computer: {}".format(5 - self.player1_score, 5 - self.player2_score), True, (0, 127, 0))
        self.vboard.blit(txt1, (800, 100))
        self.vboard.blit(txt2, (800, 200))
        self.vboard.blit(txt3, (800, 300))
        self.vboard.blit(play_score_msg1, (810, 130))
        self.vboard.blit(play_score_msg2, (810, 230))
        
        

    def quit(self):
        pygame.quit()
        sys.exit()

###################################################################### SPLASH SCREEN ###########
MARGIN_ROW = 40
MARGIN_COL = 11



class Begin:
    def __init__(self, player_board, user_board, person):
        self.player_board = player_board
        self.user_board = user_board
        self.person = person
        self.required_ships = [5, 4, 3, 2, 1]
        self.num_set_ships = 0

    def show_required(self, color, index):
        x = 5
        for row in range(5):
            for column in range(x):
                if index == x:
                    pygame.draw.rect(self.player_board,
                                 color,
                                 pygame.Rect(800+(40 *column), 200+(40*row), 30, 30))
                else:
                    pygame.draw.rect(self.player_board,
                                     WHITE,
                                     pygame.Rect(800+(40 *column), 200+(40*row), 30, 30))
            x -= 1
    def set_player_ships(self, x_head, y_head, battleship_length):
        person = self.person.set_battleship(x_head, y_head, battleship_length)
        person_ships = person[-1]
        #for person_ships in ships:
        self.user_board.add_ship(person_ships[0], person_ships[1],\
                                     person_ships[2], person_ships[3], person_ships[4])
        P_SHIPS.append((person_ships[0], person_ships[1],\
                                     person_ships[2], person_ships[3], person_ships[4]))
        print("person ships: ",  person_ships)

    
    def display_score(self):
        title = pygame.font.SysFont("ocraextended", 40)
        #title.set_bold(True)
        font = pygame.font.SysFont("'couriernew'", 19)
        font.set_bold(True)
        main_title = title.render("Battle of the Titans", True, (0, 128, 0))
        self.player_board.blit(main_title, (145, 40))
        txt1 = font.render("1. Set Battleship locations", True, (0, 128, 0))
        txt2 = font.render("2. Press any key to start game", True, (0, 128, 0))
        #txt3 = font.render("3. Set Battleships by selecting preferred location", True, (0, 128, 0))
        self.player_board.blit(txt1, (50, 150))
        self.player_board.blit(txt2, (50, 250))
        #self.player_board.blit(txt3, (10, 300))
        font = pygame.font.SysFont("couriernew", 17)
        mess_1 = "Required ships: "
        font.set_bold(True)
        txt1 = font.render(mess_1, True, (0, 127, 0))
        self.player_board.blit(txt1, (800, 150))
        
        

    def update(self, obj, coord_x, coord_y):
        obj.viewable_move(coord_x, coord_y)

    def set_border(self):
        pygame.draw.rect(self.player_board, BLUE, pygame.Rect(10, 10, 1000 - 235, 500 - 35), 3)

    
def main():
            
    pygame.init()

    DISPLAY=pygame.display.set_mode((1000,500),0,32)
    DISPLAY.fill(BLACK)
    pygame.display.set_caption("BattleShip--1.0")
    user_board = VisibleUserBoard(DISPLAY)
    person = PersonPlayer()

    #user_board.add_ship(3, 4, 3, 5, 2)


    #print(user_board.all_ships_sunk())
    begin = Begin(DISPLAY, user_board, person)
    begin.display_score()
    begin.set_border()
    begin.show_required(WHITE, 0)

    begin.num_set_ships = 0 #number of battleship bricks should not be more than 15
    #begin.set_player_ships(2, , battleship_length)
    def mouse_event(event, start, size):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if 430 <= mouse_pos[0] <= 775 and 130 <= mouse_pos[1] <= 475:
                print(mouse_pos)
                col = mouse_pos[0] - 430
                rw = mouse_pos[1] - 130
                column = col // (size + 5)
                row = rw // (size + 5)
                #if (0 <= row <= 9) and (0 <= column <= 9):
                #if (row, column) not in val:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('jump.wav'))
                
                    
                if len(begin.required_ships) > 0:
                    begin.set_player_ships(column, row, begin.required_ships[0])
                    popped_val = begin.required_ships.pop(0)
                    begin.show_required(RED, popped_val)
                    begin.num_set_ships += 1
                        
                    print("Click ", mouse_pos, "Grid coordinates: ", row, column)
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
            n_event = mouse_event(event, begin, 30)
            if  n_event is not None:
                print(n_event)
        pygame.display.update()
    
    



######################################################################
if __name__ == '__main__':
    SIZE = 30
    def mouse_event(mouse_pos, start):
        if 40 <= mouse_pos[0] <= 385 and 130 <= mouse_pos[1] <= 475:
            col = mouse_pos[0] - 40
            rw = mouse_pos[1] - 130
            column = col // (SIZE + 5)
            row = rw // (SIZE + 5)
            #if (row, column) in lst_clicked:
            no_go = start.update(start.vb_auto, column, row)
            if no_go != None and no_go != []:
                start.player1_score = start.player1_score + 1
            print("Click ", mouse_pos, "Grid coordinates: ", column, row)
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('jump.wav'))
            #pygame.draw.rect(start.vboard,BLACK,
            #pygame.Rect(800, 300, 400, 300))
            start.guesses += 1
            #print("Click ", mouse_pos, "Grid coordinates: ", column, row)
            start.turns = 1
                #else:
                #pygame.mixer.Channel(1).play(pygame.mixer.Sound('Buzzer.wav'))
            
            
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
    
        
    #start class
    start = Start(auto, person, stats, main_board, enemy_board, user_board, P_SHIPS);
    start.set_auto_ships()
    start.set_border()
    start.set_person_ships()
    pygame.mixer.Channel(0).play(pygame.mixer.Sound('look.wav'))
    
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
    pygame.mixer.music.play()
    win = 0


    running = True
    while running:
        
        for event in pygame.event.get():
            #pygame.draw.rect(start.vboard,BLACK,
            #            pygame.Rect(800, 100, 400, 500))
            start.display_score()
            start.display_stats()
            #pygame.display.flip() #update the game when it draws
            if event.type==QUIT:
                start.quit()
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('look.wav')
                pygame.mixer.music.play()
                #start.set_player_ships()
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
                        win = 1
                        main_board.blit(main_title, (210, 40))
                        start.display_score()
                        start.display_stats()
                        running = False
                    pygame.draw.rect(start.vboard,BLACK,
                        pygame.Rect(960, 300, 40, 40))
                    
                    
                    
                else:
                    #m_event = mouse_event(mouse_pos, start)
                    #pygame.time.delay(300) #set time for the ai
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
                        win = 1
                        main_board.blit(main_title, (175, 40))
                        start.display_score()
                        start.display_stats()
                        running = False
                    #start.guesses += 1
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
        #pygame.display.update()
        
            
