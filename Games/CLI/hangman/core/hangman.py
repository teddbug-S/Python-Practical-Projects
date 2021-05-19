from random import choice
from os import system
from time import sleep
from colored import fg, attr


class HangMan:
    """
    A simple command-line word guessing game.
    """
    def __init__(self, /,
                 word_list: list,
                 remarks: list,
                 banner: str,
                 score_board: str,
                 lose_board: str,
                 win_board: str,
                 stages: list) -> None:
        self.words_list = word_list
        self.remarks = remarks
        self.banner = banner
        self.stages = stages
        self.score_board = score_board
        self.win_board = win_board
        self.lose_board = lose_board
        self.word = ""
        self.list_word = []
        self.word_length = 0
        self.hidden_word = []

    def refresh(self):
        system('clear')
        print(self.banner)

    def set_vars(self):
        self.word = choice(self.words_list).upper()
        self.word_length = len(self.word)
        self.hidden_word = ['_'] * self.word_length
        self.list_word = list(self.word)

    def get_remark(self):
        return choice(self.remarks)

    def score_table(self, score, tries):
        """ Returns a score table """
        table = self.score_board.format(score, tries)
        return table
    
    def win_table(self, score):
        """Returns win table """
        table = self.win_board.format(score)
        return table
    
    def lose_table(self, score):
        """Returns win table """
        table = self.lose_board.format(score)
        return table
    
    def get_man(self, tries):
        return self.stages[tries]

    @staticmethod
    def replace(seq, new, pos=0, old=None):
        if not pos and old:
            pos = seq.index(old)
        seq.pop(pos)
        seq.insert(pos, new)

    def game(self):
        self.set_vars()
        score, tries, guessed = 0, 6, []
        while tries: # stay alive while there's still a chance
            self.refresh() # refresh screen
            # get user input
            print(self.score_table(score, tries))
            print(f"%s{self.get_man(tries)}%s\n"%(fg('82'), attr('reset')))
            print(f"%s\t{''.join(self.hidden_word)}%s"%(fg('171'), attr('reset')))
            user_guess = input("%s\tGuess Word or Letter: %s"%(fg('82'), attr('reset'))).upper()
            # if guess is a letter
            if len(user_guess) == 1 and user_guess not in guessed:
                if user_guess in self.list_word:
                    # replace the hidden letter with it
                    self.replace(seq=self.hidden_word, new=user_guess, pos=self.list_word.index(user_guess))
                    self.replace(seq=self.list_word, new='', old=user_guess)
                    score += 1 # add a score of 1
                    if '_' not in self.hidden_word and ''.join(self.hidden_word) == self.word:
                        score += 10
                        tries = tries + 1 if tries < 6 else tries
                        self.set_vars()
                        print(f"\n\t%s{self.get_remark().capitalize():1}! You guessed the wOOrrd.%s"%(fg('26'), attr('reset')))
                        sleep(1.6)
                else:
                    # else add letter to guessed
                    print(f"%s\tWrong Guess! {user_guess} is not in the word.%s"%(fg('50'), attr('reset')))
                    guessed.append(user_guess)
                    tries -= 1 # reduce the chances
                    sleep(0.4)
            # else if it is a word guess
            elif len(user_guess) == self.word_length and user_guess not in guessed:
                if user_guess == self.word:
                    score += 10
                    self.set_vars()
                    tries = tries + 1 if tries < 6 else tries
                    print(f"\n\t%s{self.get_remark().capitalize():1}! You guessed the wOOrrd.%s"%(fg('26'), attr('reset')))
                    sleep(1.6)
                else:
                    print(f"%s\tWrong Guess! {user_guess} is not the word.%s"%(fg('light_cyan'), attr('reset')))
                    guessed.append(user_guess)
                    tries -= 1
                    sleep(0.4)
            elif user_guess in guessed:
                print(f"%s\tYou have already guessed {user_guess}%s"%(fg('light_cyan'), attr('reset')))
                sleep(0.4)
            else:
                print("%s\tInvalid Guess!%s"%(fg('27'), attr('reset')))
                sleep(0.5)
        else:
            if score > self.word_length:
                self.refresh()
                print(f"%s\t\t\t\tCongratulations!!!%s"%(fg('hot_pink_3a'), attr('reset')))
                print(f"%s{self.win_table(score)}%s"%(fg('gold_1'), attr('reset')))
                rint(f"\n\t%sWord: {self.word}%s"%(fg('87'), attr('reset')))
            else:
                self.refresh()
                print(f"%s{self.lose_table(score)}%s"%(fg('87'), attr('reset')))
                print(f"\n\t%sWord: {self.word}%s"%(fg('87'), attr('reset')))
            again = input("\tDo you wish to play again_Y/N?: ").lower()
            if again == 'y':
                self.game()
 
