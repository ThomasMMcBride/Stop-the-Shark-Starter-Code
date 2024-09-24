import random

# Model: Saves current state of the hangman game
# Things worth saving:
    # Possible words in the game
    # Current word to guess
    # Letters guessed
    # Correct letter guesses
    # Incorrect letter guesses
# What should a model for the hangman game be able to do to itself?
    # Guess a letter
    # Provide information of its state
class Model:
    """
    Model constructor
    Args:
        possible_words: list of strings representing the possible words the player can guess
    """
    def __init__(self, possible_words):

        self.possible_words = possible_words

        self.word_to_guess = random.choice(self.possible_words)

        # This list will contain the word the player has guessed so far. Starts off as a list of blanks.
        self.word_so_far = ["_"] * len(self.word_to_guess) 

        # List of all of the incorrect letters the player has guessed. 
        # We use a set here to avoid duplicate inccorect letters.
        self.incorrect_letters = set()

        # The player will have 10 chances to guess wrong.
        self.lives = 10
    
    """
    Given a string 'letter', checks to see if the letter is within the word to guess and adds
    to the word so far if it is within the word to guess. Otherwise, it adds the letter to the set of
    incorrect letters and reduces the number of lives by 1.

    Args:
        letter : String representing a player's guessed letter (assumed to be already lowercase)
    Returns:
        nothing 
    """
    def guess_letter(self, letter):
        # (TODO) Implement guess_letter following the comments below.

        if letter in self.word_to_guess:
            for i, char in enumerate(self.word_to_guess):

                # If 'letter' is equal to 'char'...

                    # Set the element at the same index in 'self.word_so_far' to 'letter'. 
                    # Hint: You can set the element of a list using the following syntax...
                    # example_list[i] = new_element
                
                pass # <- Remove when done! 
            
        # Else
            #  _Add_ 'letter' to self.incorrect_letters

            #  Reduce self.lives by 1 
        raise NotImplementedError("Remove this when done.")
    
    """
    Determines if the Stop-the-Shark game is over (player has lost)
    Args:
        none
    Returns:
        True if the game is over, False if the game is not over
    """
    def game_over(self):
        # (TODO) Implement game_over.
        #
        # The game is over when both of the following occur:
        # (i) Player has run out of lives (self.lives == 0)
        # (ii) There are still "_"s in self.word_so_far ("_" in self.word_so_far)
        raise NotImplementedError("Remove this when done.")

    """
    Determines if the player has won the Stop-the-Shark game.
    Args:
        none
    Returns:
        True if the player has won, False if player has not won
    """
    def player_wins(self):
        # (TODO) Implement player_wins.
        #
        # The player wins when both of the following occur:
        # (i) Player has more than 0 lives (self.lives > 0)
        # (ii) There are no more "_"s in self.word_so_far (not "_" in self.word_so_far)
        raise NotImplementedError("Remove this when done.")

    

# View: Displays information about the game to the player, and receives input from the player
# Things worth showing:
    # Current attempts left
    # Guessed word so far
    # Incorrect guesses
    # Let the player know if they have lost or won
    # Let them know if they've input something invalid
class View:
    """
    Displays a welcome message to the player in the console
    Args:
        none
    Returns:
        none
    """
    @staticmethod
    def display_welcome():
        # (TODO) print() a warm welcome to the console!
        raise NotImplementedError("Remove this when done.")
    
    """
    Notifies the player that they have lost the game
    Args:
        none
    Returns:
        none
    """
    @staticmethod
    def display_game_over():
        # (TODO) print() a message letting the player know they've lost the game.
        raise NotImplementedError("Remove this when done.")

    """
    Notifies the player that they have won the game
    Args:
        none
    Returns:
        none
    """
    @staticmethod
    def display_game_won():
        # (TODO) print() a message letting the player know they've won the game.
        raise NotImplementedError("Remove this when done.")
    
    """
    Prints the given text to the console
    Args:
        text : A string representing the text to be print to the console
    Returns:
        none
    """
    @staticmethod
    def display_text(text):
        # (TODO) print() the given 'text' to the console, followed by a newline '\n'.
        raise NotImplementedError("Remove this when done.")
    
    """
    Asks the user for a new letter guess using input() and returns the guess
    Args:
        none
    Returns:
        A string, representing the letter that the player guessed
    """
    @staticmethod
    def get_next_guess():
        # (TODO) Using Python's built-in input(), ask the player for their next guess, and return the guess
        raise NotImplementedError("Remove this when done.")
    
    """
    Notifies that the player has input an invalid value, asks for them to only input letters
    Args:
        none
    Returns:
        none
    """
    @staticmethod
    def display_try_again():
        # (TODO) print() a message asking the player to provide only letters as input.
        raise NotImplementedError("Remove this when done.")

    """
    Prints whitespace to the console
    Args:
        none
    Returns:
        none
    """
    @staticmethod
    def print_space():
        print("\n\n\n\n")

    """
    Given an index, prints the image corresponding to that index to the console
    Args:
        stage : A number representing an index
    Returns:
        none
    """
    @staticmethod
    def show_man(stage):
        # (TODO) Given a 'stage' representing an index for the list of string images below, print() the 
        # image at that index
        stages = [
        """

                 _______
               /         \\
              |           |
              |___________|
                 \ ||| / 
                  \|||/ 
                   \o/
                    |
                   / \\

             
        |-
        |  \\_
    ____|_____\\____________
        """,
        """

                 _______
               /         \\
              |           |
              |___________|
                 \ ||| / 
                  \| |/ 
                   \o/
                    |
                   / \\

                
        |-
        |  \\_
    ____|_____\\____________
        """,
        """

                 _______
               /         \\
              |           |
              |___________|
                 \ ||| / 
                   \|/ 
                   \o/
                    |
                   / \\

                     
        |-
        |  \\_
    ____|_____\\____________
        """,
        """

                 _______
               /         \\
              |           |
              |___________|
                 \ ||| / 
                   | |
                   \o/
                    |
                   / \\

                     
        |-
        |  \\_
    ____|_____\\____________
        """,
        """

                 _______
               /         \\
              |           |
              |___________|
                 \ | | / 
                   | |
                   \o/
                    |
                   / \\

                     
        |-
        |  \\_
    ____|_____\\____________
        """,
        """

                 _______
               /         \\
              |           |
              |___________|
                 \ | | / 
                    |
                   \o/
                    |
                   / \\

                      
        |-
        |  \\_
    ____|_____\\____________
        """,
        """

                 _______
               /         \\
              |           |
              |___________|
                 \ | | / 
                   \o/
                    |
                   / \\

                  
        |-
        |  \\_
    ____|_____\\____________
        """,
        """

                 _______
               /         \\
              |           |
              |___________|
                  | | |    
                   \o/
                    |
                   / \\

           
        |-
        |  \\_
    ____|_____\\____________
        """,
        """
        
                 _______
               /         \\
              |           |
              |___________|
                   | |     
                   \o/
                    |
                   / \\

              
        |-
        |  \\_
    ____|_____\\____________
        """,
        """

                 _______
               /         \\
              |           |
              |___________|
                  |    
                   \o/
                    |
                   / \\

               
        |-
        |  \\_
    ____|_____\\____________
        """,
        """ 









       mmm food...       
        |-
        |  \\_      uh oh...
    ____|_____\\_____\o/____
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                 \ ||| / 
                  \|||/ 
                   \o/
                    |
                   / \\

    whatever...    
          -|
       _/  |
     /_____|__________________
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                 \ ||| / 
                  \| |/ 
                   \o/
                    |
                   / \\

    whatever...    
          -|
       _/  |
     /_____|__________________
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                 \ ||| / 
                   \|/ 
                   \o/
                    |
                   / \\

    whatever...    
          -|
       _/  |
     /_____|__________________
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                 \ ||| / 
                   | |
                   \o/
                    |
                   / \\

    whatever...    
          -|
       _/  |
     /_____|__________________
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                 \ | | / 
                   | |
                   \o/
                    |
                   / \\

   whatever...    
          -|
       _/  |
     /_____|__________________
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                 \ | | / 
                    |
                   \o/
                    |
                   / \\

   whatever...    
          -|
       _/  |
     /_____|__________________
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                 \ | | / 
                   \o/
                    |
                   / \\

   whatever...    
          -|
       _/  |
     /_____|__________________
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                  | | |    
                   \o/
                    |
                   / \\

   whatever...    
          -|
       _/  |
     /_____|__________________
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                   | |     
                   \o/
                    |
                   / \\

   whatever...    
          -|
       _/  |
     /_____|__________________
        """,
        """
                  phew!
                 _______
               /         \\
              |           |
              |___________|
                   |    
                   \o/
                    |
                   / \\

   whatever...    
          -|
       _/  |
     /_____|__________________
        """]

        raise NotImplementedError("Remove this when done.")



# Controller: Manipulate the view and controller and keep the game running until the game is over

# This is done for you! Assuming your Model and View implementations are correct, you should have a 
# fully working command-line application!
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def go(self):
        self.view.display_welcome()

        while not self.model.game_over() and not self.model.player_wins():
            self.view.show_man(10 - self.model.lives)
            self.view.display_text(f"Word guessed so far: {' '.join(self.model.word_so_far)}")
            self.view.display_text(f"Incorrect guesses: {', '.join(self.model.incorrect_letters)}")
            self.view.display_text(f"Number of lives left: {self.model.lives}")
            guess = self.view.get_next_guess()

            if len(guess) != 1 or not guess.isalpha():
                self.view.print_space()
                self.view.display_try_again()
                continue

            self.model.guess_letter(guess.lower())
        
        if self.model.game_over():
            self.view.show_man(10)
            self.view.display_game_over()
        elif self.model.player_wins():
            self.view.show_man(21 - self.model.lives)
            self.view.display_text(f"Number of lives lost: {10 - self.model.lives}")
            self.view.display_text(f"Word: {''.join(self.model.word_to_guess)}")
            self.view.display_game_won()


if __name__ == "__main__":
    with open("words.txt") as word_file:
        words = word_file.readlines() 
        words = [word.strip() for word in words]
    model = Model(words)
    view = View()
    controller = Controller(model, view)
    
    controller.go()