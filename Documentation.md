## Directory Structure

1. `AutomaticPlayer` contains the code for the computer that will verse the player (inherits from `Player`).
2. `Board` contains the back-end portion of the code for the game boards.
3. `Controller` contains the code to start, run and end the game.
4. `PersonPlayer` contains the code for the user playing the game (inherits from `Player`)
5. `Player` contains code for any player.
6. `Stats` contains code for the display that shows the statistics of the game.
7. `VisibleBoard` contains the code for the GUI of both game boards.

## Examples of how to extend the game

1. Currently, our game only allows the player to play against computer. One way to extend our game would be to make the game multiplayer. This would allow two human players to verse against each other. 
2. Our game allows the user to win even if they hit only one square containing the battleship. The game could be made more challenging by only allowing users to win only if they hit all the squares containing the ship. 
3. Additional features such as a 'quit' button or 'reset' button could be added to allow player to exit or restart the game.

## Major Classes and Functions

1. **`Board class:`**

   A board is a standard 10\*10 grid where each square can have status 'neutral', 'hit', 'miss' or 'ship'. Every position on the board starts as ‘neutral’.

   1. Attributes:
      1. `status` – A 10*10 multidimensional array representing each coordinate of the grid. Each coordinate can have one of the following statuses: ‘neutral’, ‘hit’, ‘miss’ or ‘ship’.
      2. `ships` – A list of ships (represented as an array of coordinates) that are currently on the Board.
      3. `number_of_ships` – An integer representing the total number of ships that have been placed on the Board.
      4. `all_ships_sunk` – Returns True if all ships have been sunk and returns False otherwise.
   2. Functions:
      1. `move(self, x, y)` – If a ship is at the location (x, y) then that the status of every position occupied by that ship is set to ‘hit’ and that ship is removed from the list of ships currently on the board.
      2. `board_add_ship (self, start_x, start_y, end_x, end_y, size)` – If the coordinates are valid then the status of all positions mentioned is changed to ’Ship’ and a list with those coordinates is appended to ships.

2. **`Rectangle:`**

   A Rectangle is an object with a width, height, x-coordinate and y-coordinate. All attributes are provided at time of instantiation.

3. **`VisibleBoard:`**

   A VisibleBoard is a standard 10\*10 grid of Rectangles where the status of each Rectangle is represented as a colour (eg. red for hit and blue for miss). It is the GUI representation of the class Board.

   1. Attributes:
      1. `rectangles` – A list containing all the Rectangles which make up the grid.
      2. `display` – The display on which the Rectangles will be drawn.
   2. Functions:
      1. `__init__` - The x and y coordinate of the upper left corner. Based on these coordinates – a 10 * 10 grid of rectangles is formed where each Rectangle has dimensions 30 * 30.
      2. `viewable_move(x, y)` – If there is a ship at this coordinate, then all coordinates of this ship will turn red. Otherwise, the rectangle turns blue.
      3. `hit (x, y)` – The rectangle at the coordinates (x, y) turns red.
      4. `miss(x, y)` – The rectangle at the coordinates (x, y) turns blue.
      5. `add_ship(self, startx, starty, endx, endy, size, colour)` – Turns  the colour of the appropriate positions to “colour” and changes the status of each of those positions to  ‘Ship’.

4. **`VisibleEnemyBoard (inherits from class VisibleBoard):`**

   A `VisibleEnemyBoard` is a `VisibleBoard` where ships are represented as white Rectangles to ensure that the User cannot see them.

   1. Functions:
      1. `__init__ `-  Draws all rectangles of the board onto display.
      2. `add_ship(self, startx, starty, endx, endy, size)` – Adds a ship to the board. The ship is represented as white Rectangles.

5. **`VisibleUserBoard (inherits from class VisibleBoard) :`**

   A `VisibleUserBoard` is a `VisibleBoard` where ships are represented as grey Rectangles so that the user can see where they have hidden their ships.

   1. Functions: 
      1. `__init__ `- Draws all rectangles of the board onto display.
      2. `add_ship(self, startx, starty, endx, endy, size) `– Adds a ship to the board. The ship is represented as grey Rectangles.

6. **`Player:`**

   Represents any player that can play the game.

   1. Attributes: `score, placements, battleship_set, selection_history`
   2. Functions: 
      1. `__init__(self)` -  Initializes the class Player.
      2. `get_total_score(self)` - Sums up the total score obtained by the Player.
      3. `avoid_plots(self, plot_list)` - Adds a list of plots to the player's selection history to prevent guessing in invalid locations.
      4. `valid_location(self, grid, x, y, ship_len, ship_orientation)` - Determines whether ship with length ship_len and orientation ship_orientation can be placed in grid at x,y.
      5. `update_internal_board(self, grid, x, y, ship_len, ship_orientation)` - Once we determine that the location is valid, we will update grid to contain newly placed battleship.

7. **`AutomaticPlayer:`**

   Inherits from the class `Player`.  It represents the computer that an actual user will play against.

   1. Attributes: `Inherited from class Player`
   2. Functions:
      1.  `__init__(self)` - Initializes the class AutomaticPlayer.
      2. `set_battleships(self)` - Plots all of Automatic Player's battleship. Should only be called once.
      3. `Guess_location(self)` - Represents the Player’s guesses. Guesses will not repeat. 

8. **`PersonPlayer:`**

   Inherits from the class `Player`. It represents the PersonPlayer represents the human that `AutomaticPlayer` will play against.

   1. Attributes: Inherited from class `Player`
   2. Functions: 
      1. `__init__(self)` - Initializes the class PersonPlayer.
      2. `set_battleship(self)` - Plots one of PersonPlayer's battleship. Should be called at least five times.

9. **`Stats:`**

   The class `Stats` displays the statistics of the game. It displays player’s total score, the total number of battleships and total number of battleships remaining for the player to guess on the board of the game. 

   1. Attributes: Inherited from classes `Player` and `Board`
   2. Functions: 
      1. `__init__(self)` - Initializes the class.
      2. `score(self)` - Returns the total score of the player. 
      3. `number_of_ships(self)` - Returns total number of battleships in the game for the player to guess.
      4. `remaining_ships(self)` - Returns the total number of battleships remaining for the player to guess.

10. **`Start(controller):`**

    The class `Start` (controller) uses all the object classes of the game. This is the controller aspect of the game.

    1. Attributes: `auto, person, stats, vboard, vb_auto, vb_player, p_ships, win, player1_ score, player2_score, turns, guesses`.
    2. Functions: 
       1. `__init__(self, auto, person, stats, vboard, vb_auto, vb_player, p_ships) `- Initializes the class Start with other classes.
       2. `set_auto_ships(self)` - Sets the valid ships coordinates for the computer player.
       3. `set_person_ships(self)` - Sets the valid ships coordinates for the human player based on choice made by the human player.
       4. `play_ai(self)` - Invokes the automatic player to guess a location.
       5. `update(self, obj, coord_x, coord_y)` - Updates the board(obj)  based on the column and row coordinate given by coord_x and coord_y respectively. 
       6. `display_score(self)` - Displays the score of both players on the screen.
       7. `set_border(self) `- Creates a border around the board.
       8. `display_stats(self)` - Display the status of both players i.e remaining ships, number of ships.
       9. `quit(self)` - Ends the game.

11. **`Begin:`**

    The class `Begin` works with class `Start` to ensure that a splash screen is set at the beginning of the game so that the human player can hide ships for the computer player to guess from.

    1. Attributes: `player_board, user_board, person, required_ships, num_set_ships`

    2. Functions: 

       1. `__init__(self, player_board, user_board, person)` - Initializes the class Begin for only the human player.

       2. `show_required(self, color, index)` - Lets the human player know what types of ship are left to hide for the computer player to guess.

       3. `set_player_ships(self, x_head, y_head, battleship_length)` - Sets the ships at the prefered locations of the human player.

       4. `display_info(self)` - Displays the instructions for the human player.

       5. `main()` - Executes the Begin class.
         
 
