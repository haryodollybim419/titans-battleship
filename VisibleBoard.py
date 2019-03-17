import pygame, sys
from pygame.locals import *
import Board

#Colours
WHITE=(255,255,255)
BLUE=(0,0,255)
RED=(255,0,0)
BLACK=(0,0,0)
GREY=(128,128,128)

'''
A Rectangle is an object with a width, height, x-coordinate and y-coordinate.
'''
class Rectangle:

    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


'''
A VisibleBoard is a standard 10*10 grid of Rectangles where the status of
each Rectangle is as a colour (eg. red for hit and blue for miss).
'''
class VisibleBoard(Board.Board):
    def __init__(self, startx, starty, display):
        Board.Board.__init__(self)
        self.rectangles = [[],[],[],[],[],[],[],[],[],[]]

        for i in range(10):
            for j in range(10):
                new_rect = Rectangle(startx + 35 * i,starty + 35 * j,30,30)
                self.rectangles[i].append(new_rect)
        self.display = display


    def viewable_move(self, x, y):
        move_return, ans = self.move(x, y)

        if (move_return, ans) == (None, []):
            return
        elif (move_return, ans) == (Board.MISS, []):
                self.miss(x, y)
        else:
            for (xc, yc) in ans:
               self.hit(xc, yc)


    def hit(self, x, y):
        if (0 <= x <= 9) and (0 <= y <= 9):
            rect = self.rectangles[x][y]
            pygame.draw.rect(self.display, RED, (rect.x, rect.y, rect.width, rect.height))


    def miss(self, x, y):
        if (0 <= x <= 9) and (0 <= y <= 9):
            rect = self.rectangles[x][y]
            pygame.draw.rect(self.display, BLUE, (rect.x, rect.y, rect.width, rect.height))


    def add_ship(self, startx, starty, endx, endy, size, colour):
        check = self.board_add_ship(startx, starty, endx, endy, size)
        if check != None:
            starting_point_x, ending_point_x, starting_point_y, ending_point_y = check
            for x in range(starting_point_x, ending_point_x + 1):
                for y in range(starting_point_y, ending_point_y + 1):
                    rect = self.rectangles[x][y]
                    pygame.draw.rect(self.display, colour, (rect.x, rect.y, rect.width, rect.height))


'''
A VisibleEnemyBoard is a VisibleBoard where ships are represented as white Rectangles.
'''
class VisibleEnemyBoard(VisibleBoard):

    def __init__(self, display):
        VisibleBoard.__init__(self, 40, 130, display)
        for row in self.rectangles:
            for rect in row:
                pygame.draw.rect(self.display, WHITE, (rect.x, rect.y, rect.width, rect.height))

    def add_ship(self, startx, starty, endx, endy, size):
        VisibleBoard.add_ship(self, startx, starty, endx, endy, size, WHITE)


'''
A VisibleUserBoard is a VisibleBoard where ships are represented as grey Rectangles.
'''
class VisibleUserBoard(VisibleBoard):

    def __init__(self, display):
        VisibleBoard.__init__(self, 430, 130, display)
        for row in self.rectangles:
            for rect in row:
                pygame.draw.rect(self.display, WHITE, (rect.x, rect.y, rect.width, rect.height))

    def add_ship(self, startx, starty, endx, endy, size):
        VisibleBoard.add_ship(self, startx, starty, endx, endy, size, GREY)
