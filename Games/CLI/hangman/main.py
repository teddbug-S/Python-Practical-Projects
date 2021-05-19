# Imports the HangMan class, passes all necessary parameters and launches the game.

from core.hangman import HangMan

from resources.hangman_comps import word_list, stages, remarks, banner, score_board, win_board, lose_board


hangman = HangMan(
    word_list=word_list,
    remarks=remarks,
    banner=banner,
    stages=stages,
    score_board=score_board,
    win_board=win_board,
    lose_board=lose_board
)
hangman.game()
