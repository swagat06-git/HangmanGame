import random
import os

class HangmanGame:
    def __init__(self):
        self.word_categories = {
            'animals': ['elephant', 'giraffe', 'penguin', 'dolphin', 'kangaroo', 'zebra', 'tiger', 'cheetah'],
            'fruits': ['apple', 'banana', 'orange', 'strawberry', 'watermelon', 'pineapple', 'mango', 'blueberry'],
            'countries': ['france', 'brazil', 'japan', 'canada', 'australia', 'germany', 'mexico', 'italy'],
            'sports': ['football', 'basketball', 'tennis', 'swimming', 'cricket', 'volleyball', 'hockey', 'baseball'],
            'colors': ['purple', 'yellow', 'orange', 'silver', 'crimson', 'turquoise', 'magenta', 'emerald']
        }        
        self.hangman_stages = [
            """
               ------
               |    |
               |
               |
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |    |
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   /
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |
            --------
            """
        ]        
        self.max_wrong = len(self.hangman_stages) - 1
        self.reset_game()    
    def reset_game(self):
        """Reset the game state"""
        category = random.choice(list(self.word_categories.keys()))
        self.word = random.choice(self.word_categories[category])
        self.category = category
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.game_over = False
        self.won = False    
    def get_display_word(self):
        """Return the word with unguessed letters as underscores"""
        return ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])    
    def display(self):
        """Display the current game state"""
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\n" + "="*50)
        print(f"{'HANGMAN GAME':^50}")
        print("="*50)
        print(f"\nCategory: {self.category.upper()}")
        print(self.hangman_stages[self.wrong_guesses])
        print(f"\nWord: {self.get_display_word()}")
        print(f"\nWrong guesses remaining: {self.max_wrong - self.wrong_guesses}")        
        if self.guessed_letters:
            sorted_guesses = sorted(list(self.guessed_letters))
            correct = [l for l in sorted_guesses if l in self.word]
            wrong = [l for l in sorted_guesses if l not in self.word]            
            if correct:
                print(f"Correct letters: {', '.join(correct).upper()}")
            if wrong:
                print(f"Wrong letters: {', '.join(wrong).upper()}")    
    def make_guess(self, letter):
        """Process a letter guess"""
        letter = letter.lower()        
        if not letter.isalpha() or len(letter) != 1:
            return "Please enter a single letter!"        
        if letter in self.guessed_letters:
            return "You already guessed that letter!"        
        self.guessed_letters.add(letter)        
        if letter in self.word:
            # Check if word is complete
            if all(l in self.guessed_letters for l in self.word):
                self.won = True
                self.game_over = True
            return "Good guess!"
        else:
            self.wrong_guesses += 1
            if self.wrong_guesses >= self.max_wrong:
                self.game_over = True
            return "Wrong guess!"    
    def play(self):
        """Main game loop"""
        while not self.game_over:
            self.display()
            guess = input("\n\nEnter a letter (or 'quit' to exit): ").strip()            
            if guess.lower() == 'quit':
                print("\nThanks for playing!")
                return False            
            message = self.make_guess(guess)            
            if message != "Good guess!" and message != "Wrong guess!":
                print(f"\n{message}")
                input("Press Enter to continue...")     
        # Game over - show final state
        self.display()        
        if self.won:
            print("\n" + "="*50)
            print(f"{'🎉 CONGRATULATIONS! YOU WON! 🎉':^50}")
            print("="*50)
            print(f"\nThe word was: {self.word.upper()}")
        else:
            print("\n" + "="*50)
            print(f"{'💀 GAME OVER! YOU LOST! 💀':^50}")
            print("="*50)
            print(f"\nThe word was: {self.word.upper()}")        
        return True
def main():
    """Main function to run the game"""
    print("\n" + "="*50)
    print(f"{'WELCOME TO HANGMAN!':^50}")
    print("="*50)
    print("\nGuess the word one letter at a time.")
    print("You have 6 wrong guesses before you lose!")
    input("\nPress Enter to start...")   
    while True:
        game = HangmanGame()
        finished = game.play()
        if not finished:
            break
        play_again = input("\n\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing Hangman! Goodbye!")
            break
if __name__ == "__main__":
    main()
