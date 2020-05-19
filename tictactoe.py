import random


def draw_board(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0).
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item and the
    # computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    # The first element in the list is the player's letter; the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    # Randomly choose which player goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def make_move(board, letter, move_p):
    board[move_p] = letter


def is_winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # Across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # Across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # Across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # Down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # Down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # Down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # Diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # Diagonal


def get_board_copy(board):
    # Make a copy of the board list and return it.
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, move_p):
    # Return True if the passed move is free on the passed board.
    return board[move_p] == ' '


# Let the player enter their move.
def get_player_move(board):
    move_v = ' '
    while move_v not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move_v)):
        print('What is your next move? (1-9)')
        move_v = input()
        return int(move_v)


def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_space_free(board, i):
            possible_moves.append(i)
    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # Check if the computer could win on their next
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, computer_letter, i)
        if is_winner(board_copy, computer_letter):
            return i
    # Check if the player could win on their next
    for i in range(1, 10):
        board_copy = get_board_copy(board)
        if is_space_free(board_copy, i):
            make_move(board_copy, player_letter, i)
        if is_winner(board_copy, player_letter):
            return i
    # Try to take one of the corners, if they are
    move_v = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move_v is not None:
        return move_v
    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5
    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise, return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


def main():
    print('Welcome to Tic-Tac-Toe!')
    while True:
        # Reset the board.
        theBoard = [' '] * 10
        playerLetter, computerLetter = input_player_letter()
        turn = who_goes_first()
        print('The ' + turn + ' will go first.')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player':
                # Player's turn
                draw_board(theBoard)
                move = get_player_move(theBoard)
                make_move(theBoard, playerLetter, move)
                if is_winner(theBoard, playerLetter):
                    draw_board(theBoard)
                    print('Hooray! You have won the game!')
                    gameIsPlaying = False
                else:
                    if is_board_full(theBoard):
                        draw_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                # Computer's turn
                move = get_computer_move(theBoard, computerLetter)
                make_move(theBoard, computerLetter, move)
                if is_winner(theBoard, computerLetter):
                    draw_board(theBoard)
                    print('The computer has beaten you! You lose.')
                    gameIsPlaying = False
                else:
                    if is_board_full(theBoard):
                        draw_board(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break


def test_call_board():
    draw_board([' ', ' ', ' ', ' ', 'X', 'O', 'X ', 'X', 'O', 'O'])


if __name__ == "__main__":
    # test_call_board()
    main()
