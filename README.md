# Rock-Paper-Scissors
**STUDENT PROJECT:** Terminal based rock paper scissors text game for the purpose of practicing with Python classes.

- Run `rps_colored.py` for the version of the text game with prettier, **colored** terminal **outputs**.
- Run `rockpaperscissors.py` for a **simpler, normal outputs** game version if there's any issues running the other file due to the module used.

## How to Play

**Note:** All input is *case-insensitive*.

### Entering Rounds:

Upon running the file, you will be asked to enter a number of **game rows**. Enter any number you like to begin the game.

![Entering rounds](https://i.imgur.com/oy2q44Q.png)

- The code accounts for accidentally giving a non-numerical input, in which case you will be prompted to answer again. 

### Playing in a Round:

Once you enter a number, the game starts. You will be assigned to `Player One` by default, and then prompted to enter your **move** (rock, paper, or scissors).

The computer opponent plays at random, and after each round, either a winner or a tie is declared along with each player's score so far.

![Playing in a round](https://i.imgur.com/ATMXcA0.png)

- The code accounts for accidentally giving an answer that doesn't match any one of three moves. 

### Quitting Mid-Game:

After the game has started, you can also **quit** at any time by entering `quit` instead of a move. 

Player scores will be announced before the program quits.

![Quitting the game](https://i.imgur.com/Js9SKoC.png)

- Note that you will not be asked for a confirmation about quitting, the program will exit immediately.

### Game Over:

Once the final round is complete, the final scores and winner will be announced. You will then be asked for a new game. Type `y`/`yes` or `n`/`no` accordingly.

![Game over](https://i.imgur.com/129bmNn.png)

- The code accounts for accidentally giving an answer that doesn't match expected results by asking for an input again.

## Student Project

This is an optional student project on Python classes from Udacity's *Intro to Programming* Nanodegree Program.

### Requirements:

To do this project, I was given certain requirements to fulfill. This is why, if you look at my code, you will notice a number of classes that are not used when the program is run.

These classes were meant to be made for practice and to test my understanding on the subject, so they are not left in the code by mistake. Feel free to ignore them.

### Given Code Snippets:

For this project, I was given the following code to build and expand on:

```python
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
```

Everything else/different is my own work (save for the recommendation I was given to add a try except block in case the `colorama` module is not installed on user's computer).
