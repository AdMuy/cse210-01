def main():
    action = " "
    turn = True
    player = "X"
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while not (match_win(options)):
        action = int(input(f"{player}'s turn. Please select a number 1-9: "))
        main_options = match_options(player, action, options)
        start_game(main_options)
        # It calles the match_win function to confirm if it's True to stop the loop and 
        # get the current player who won, instead of passing the turn to the other player
        # and get the incorrect one on the congratulations message.
        if match_win(options) == True:
            break
        # It calls the turns fuction to determine the next player.
        who_turn = turns(turn)
        player = who_turn[0]
        turn = who_turn[1]
    if match_win(options) == True:
        print(f'Congratulations {player} you win!')
    print (f'{match_win(options)}')

def turns(turn):
    if turn == False:
            player = "X"
            turn = True
    elif turn == True:
            player = "O"
            turn = False
    return player, turn

def start_game(options):
    print()
    print(f"{options[0]}|{options[1]}|{options[2]}")
    print('-+-+-')
    print(f"{options[3]}|{options[4]}|{options[5]}")
    print('-+-+-')
    print(f"{options[6]}|{options[7]}|{options[8]}")
    print()

def match_options(player_turn, selection, options):
    if player_turn == "X":
        print (f'X selection: {selection}')
        for option in options:
            if option == selection:
                options[selection - 1] = "X"
                return options
    if player_turn == "O":
        print (f'O Selection: {selection}')
        for option in options:
            if option == selection:
                options[selection - 1] = "O"
                return options

def match_win(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
        




if __name__ == "__main__":
    main()