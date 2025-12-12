#include <iostream>
using namespace std;
#include <string>
#include <time.h> // for time()

const int MAX_TRIES = 6;
const string WORDS[] = {"HELLO", "WORLD", "HANGMAN", "COMPUTER", "PROGRAM"};

int main() {
    srand(time(NULL));

    int winCount = 0;
    int loseCount = 0;
    char playAgain = 'y';

    while (playAgain == 'y' || playAgain == 'Y') {
        string word = WORDS[rand() % (sizeof(WORDS) / sizeof(WORDS[0]))];
        string hiddenWord(word.length(), '-');
        string guessedLetters;
        int tries = 0;
        char guess;

        cout << "Welcome to Hangman!" <<endl;

        while (tries < MAX_TRIES && hiddenWord != word) {
            cout << "Word: " << hiddenWord << endl;
            cout << "Guessed Letters: " << guessedLetters << endl;
            cout << "Tries Remaining: " << MAX_TRIES - tries <<endl;
            cout << "Enter your guess: ";
            cin >> guess;

            if (guessedLetters.find(guess) != std::string::npos) {
                cout << "You already guessed that letter. Try again." <<endl;
                continue;
            }
            
            guessedLetters += guess;

            if (word.find(guess) != string::npos) {
                for (int i = 0; i < word.length(); i++) {
                    if (word[i] == guess) {
                        hiddenWord[i] = guess;
                    }
                }
                cout << "Correct guess!" << endl;
            } else {
                tries++;
                cout << "Incorrect guess!" << endl;
            }

            cout << std::endl;
        }

        if (hiddenWord == word) {
            cout << "Congratulations! You guessed the word: " << word <<endl;
            winCount++;
        } else {
            cout << "Sorry, you ran out of tries. The word was: " << word <<endl;
            loseCount++;
        } 

        cout << "Wins: " << winCount << " Losses: " << loseCount << endl;
        cout << "Do you want to play again? (y/n): ";
        cin >> playAgain;
        cout << std::endl;
    }

    cout << "Thank you for playing Hangman!" << endl;

    return 0;
}
