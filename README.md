# titans-battleship
# Battle of the Titans
'Battle of the Titans' is an open-source version of the popular game 'Battleship' coded in Python.

## Game Description
Battleship is a 2 player guessing game in which players take turns trying to guess the location of their opponent’s battleship.  
At the beginning, each player plots 5 battleships that can either have a horizontal or vertical orientation and will be of lengths 
1, 2, 3, 4 and 5. The plots selected by the player will be hidden from their opponent. 
The objective of the game is to correctly guess the locations of your opponent’s battleship before they guess the location of your battleships.

In this version of Battleship, the user will be playing against a computer. The computer will automatically decide where 
to plot its battleships. The computer will also randomly guess the locations of the user’s battleship.
Whoever guesses the location of all of their opponent's battleships first, wins the game. 
Once either all of the computer’s or the user’s battleship plots have been correctly guessed, the game will end.


## Installation

### For Windows:
  - Download the prebuilt zip file and unzip it.
  - Run controller.py.

### For Ubuntu:
  - Install pygame: ```$ sudo apt-get install python-pygame```.
  - Clone the repo:  ``` $ git clone https://github.com/haryodollybim419/titans-battleship.git```.
  - Run controller.py: ```$ python controller.py```.
  
### For Mac:
  - Install pygame: ```$ pip3 install hg+http://bitbucket.org/pygame/pygame```.
  - Clone the repo: ```$ git clone https://github.com/haryodollybim419/titans-battleship.git```.
  - Run the controller.py: ```$ python controller.py```.
 

## How to Play


## Screenshots 
  1. Title Screen 
  <br /> Set 5 battleships of sizes 1, 2, 3, 4 and 5 squares horizontally as shown under required ships for the opponent to guess.
  <br /> Press any key to start the game. 
  <p align="left">
  <img width="650" height="400" src="https://user-images.githubusercontent.com/47309090/54718306-97467000-4b30-11e9-8410-205aa249df90.png">
</p>

  2. Ship Placement
<p align="left">
<img width="650" height="400" src="https://user-images.githubusercontent.com/47309090/54720132-07ef8b80-4b35-11e9-9401-3ae9f1534678.png">
</p>

  3. Start
  <br /> Click on any square of the board to guess the location of the battleships set by the opponent. 
  <p align="left">
<img width="650" height="400" src="https://user-images.githubusercontent.com/47309090/54719516-80ede380-4b33-11e9-9509-cf13ef573ced.png">
</p>

 4. Midgame
 <br /> The squares containing the battelship are turned red if you successfully hit any one square containing the battleship. 
 <br /> The squares are turned blue if you fail to hit a battleship. 
 <br /> The 'Number of ships' indicate the total number of battleships in the game. 
 <br /> The 'Remaning ships' indicate the remaining number of battleships in the game. 
 <br /> The 'Number of guesses' keep track of user's turns. 
  <p align="left">
<img width="650" height="400" src="https://user-images.githubusercontent.com/47309090/54719654-cdd1ba00-4b33-11e9-81a8-926d82039aee.png">
</p>

 5. End 
 <br /> Whoever guesses all the locations of the battleships first, wins the game! 
  <p align="left">
<img width="650" height="400" src="https://user-images.githubusercontent.com/47309090/54719676-dcb86c80-4b33-11e9-917e-7ce4ccf57d4c.png">
</p>
  

## License
This game was built by:
  - Michelle Sueyie Lim (@mich-sue9) 
  - Mohammed Samoel Ali (@MoSamAli)
  - Navya Gupta (@NavyaGupta)
  - Syeda Rida Zehra (@RidaZ313) 
  - Temidola Dollybim (@haryodollybim419) 
  
  The game was built under the GNU Lesser General Public License.
  A copy of the license can be found at https://github.com/haryodollybim419/titans-battleship/blob/master/LICENSE.txt.
