#  IMPORTS:
import sys
import random
import subprocess
try:
    import colorama
except Exception as e:
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "colorama"]
    )
from colorama import Fore
from colorama import Style

# VARIABLES:
moves = ['rock', 'paper', 'scissors']


# Function that Colors Strings in Terminal:
def colored(string, color):
    colors = {
        "red": Fore.RED,
        "blue": Fore.BLUE,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "purple": Fore.MAGENTA
        }
    print(f"{colors[color]}{string}{Style.RESET_ALL}")


# CLASSES:
# Parent Class - Non-Random Player:
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Player Sub Class - Randomly Plays a Move:
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Player Sub Class - Asks Human Player for a Move:
class HumanPlayer(Player):
    def move(self):
        """Human Player move:
        Asks player for input, converts it to lower case and validates it
        """
        human_move = input("Rock, paper, scissors? > ").lower()
        # Checks for Valid Input:
        if human_move not in moves and human_move != "quit":
            colored("Oops! Seems like you misspelled something."
                    " Try again!", "red")
            return self.move()
        return human_move


# Player Sub Class - Uses Opponent's Last Move:
class ReflectPlayer(Player):
    def __init__(self):
        self.last_moves = {  # Saves last own & opponent's move
            "my_move": "",
            "their_move": ""
            }

    def move(self):
        """Reflects last opponent move.
        Uses last opponent move, unless there isn't one,
        in which case it returns a random move."""
        their_move = self.last_moves["their_move"]
        return (their_move == "" and random.choice(moves) or their_move)

    # Saves Own & Opponents Latest Move to Instance Variable:
    def learn(self, my_move, their_move):
        last_moves = self.last_moves
        last_moves["my_move"] = my_move
        last_moves["their_move"] = their_move


# ReflectPlayer Sub Class - Uses its Own Last Move:
class CyclePlayer(ReflectPlayer):  # Inherits already defined functions
    """Inherits __init__ & learn from ReflectPlayer
    since it requiressimilar methods."""
    def move(self):
        """Cycles through moves.
        Uses the next in the moves list move each time,
        starting from the first one when list is exhausted."""
        my_move = self.last_moves["my_move"]
        return (my_move != "" and moves[(moves.index(my_move)+1) % 3] or
                random.choice(moves))


# Determines if One Move Beats Another:
def beats(one, two):
    """Determines winning move.
    Output: Returns True if one beats two."""
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Contains All Main, Game Methods:
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1  # Player One
        self.p2 = p2  # Player Two
        self.scores = {"p1": 0, "p2": 0}  # Gathers player scores

    def keep_score(self, move1, move2):
        """- Keeps track of each player's score,
        updating self.scores with the new sum for each player.
        - Declares which player wins each round.
        - Prints each player's total score after each round.
        """
        scores = self.scores  # Player scores
        # Converts Win/Loss to 0/1 & Saves it to List:
        score1 = int(beats(move1, move2))
        score2 = int(beats(move2, move1))
        scores["p1"] += score1
        scores["p2"] += score2
        # Declares Which Player Won the Round, or a Tie:
        if score1 != score2:
            round_winner = (score1 > score2 and "ONE" or "TWO")
            colored(
                f"** PLAYER {round_winner} WINS THE ROUND **",
                "green" if round_winner == "ONE" else "blue"
                )
        else:
            colored("** THIS ROUND IS A TIE **", "yellow")
        # Prints Total of Each Player's Scores:
        colored(f"Player One Score: {scores['p1']}", "green")
        colored(f"Player Two Score: {scores['p2']}\n", "blue")

    def play_round(self):
        """Saves player moves and checks if user typed "quit".
        If they did, it calls game_over() with param set to True.
        If not, prints the move each player chose and calls learn()."""
        move1 = self.p1.move()
        move2 = self.p2.move()
        # Checks if User Wants to Quit Game:
        if move1 == "quit" or move2 == "quit":
            self.game_over(True)
        colored(f"Player One: {move1.upper()}", "green")
        colored(f"Player Two: {move2.upper()}", "blue")
        self.keep_score(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def game_over(self, user_quit=""):
        """Is activated when game ends,
        either naturally or due to player typing "quit".
        Parameter:
        :user_quit: Boolean parameter, True is passed when player
        sends "quit" instead of a move, otherwise defaults to False.
        Functionality:
        Prints final scores and declares the winner (or a tie)
        of all game rounds using self.scores.
        It also prints by how many points the winner won.
        If game concluded naturally, it asks user if they want
        to restart the game, in which case self.score is reset.
        If player quit via typing "quit", game ends without asking.
        """
        scores = self.scores
        game_winner = (scores["p1"] > scores["p2"] and "One" or "Two")
        score_list = list(scores.values())
        score_difference = max(score_list) - min(score_list)
        print(user_quit and "\nYou quit the game." or "Game over!")
        print(f"\nFINAL SCORES:")
        colored(f"Player One Total Score: {scores['p1']}", "green")
        colored(f"Player Two Total Score: {scores['p2']}", "blue")
        print(f"\n\nRESULTS:")
        if scores["p1"] != scores["p2"]:
            colored(f"** Player {game_winner} Wins the Game"
                    f" by {score_difference}"
                    f" Point{score_difference > 1 and 's' or ''}! **\n",
                    "green" if game_winner == "One" else "blue")
        else:
            colored(f"** TIE: Both Players Scored the Same! **", "yellow")

        # Asks User if they Want to Restart the Game:
        def restart_game():
            """Asks user if they want to restart the game.
            If yes, resets self.score.
            If not, thanks player and exits.
            It also checks for valid input."""
            restart = input("Would you like to play again?\n(y/n):")
            if restart.lower() == "y" or restart.lower() == "yes":
                print("\nStarting New Game!\n")
                self.scores = {"p1": 0, "p2": 0}  # Restarts scores
                self.play_game()  # Restarts game
            elif restart.lower() == "n" or restart.lower() == "no":
                print("\nThank you for playing!")
            else:  # Checks for valid input:
                colored(f"Oops! Seems like you misspelled something."
                        f"\nMake sure your response is: y, yes, n or no.",
                        "red")
                return restart_game()

        # If Player Typed "quit", Game Ends Without Restart Option:
        if not user_quit:
            restart_game()
        exit()

    def play_game(self):
        """Asks user for how many rounds they want to play.
        Validates input, and asks again if invalid."""
        try:  # Asks user how many rounds they want to play:
            game_rounds = int(input(
                "Please enter the desired number of rounds to play: "
                ))
        except ValueError:  # Ensures input value is correct
            colored("Sorry, I didn't quite catch that.\nPlease try again,"
                    " and make sure you enter a valid number.\n", "red")
            return self.play_game()
        # Game Starts:
        print("\nGame start!\n")
        for round in range(game_rounds):
            colored(f"ROUND {round}:", "purple")
            self.play_round()
        self.game_over()  # Game concludes naturally.


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
