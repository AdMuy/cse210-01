'''
Tic-Tac-Toe
W02 Prove: Developer - Solo Code Submission
Author: Adam Muy
'''

def main():
    action = " "
    turn = True
    player = "X"
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while not (match_win(options)):
        # Request the selection from the user.
        action = int(input(f"{player}'s turn. Please select a number 1-9: "))
        # Calls the match_options funtion to record the selected number by the current player.
        # It passes the match_options result through the start_game function to print the game. 
        start_game(match_options(player, action, options))
        # It calles the match_win function to confirm if it's True to stop the loop and 
        # get the current player who won, instead of passing the turn to the other player
        # and get the incorrect one on the congratulations message.
        if match_win(options) == True:
            break
        # It calls the turns fuction to determine the next player.
        whose_turn = turns(turn)
        player = whose_turn[0]
        turn = whose_turn[1]
    # It displays a congratulations message when the match is over.
    print(f'Congratulations {player} you win!')

def turns(turn):
    """Decides whose turns is it based on the last player's movement. 

    Parameters
        turn: a variable stating who made the last movement. 
    Return: the next player to make a move.
    """
    if turn == False:
            player = "X"
            turn = True
    elif turn == True:
            player = "O"
            turn = False
    return player, turn

def start_game(options):
    """Print the game, and replace the numbers with the player's name. 

    Parameters
        options: the list of movements made by the players.
    """
    print()
    print(f"{options[0]}|{options[1]}|{options[2]}")
    print('-+-+-')
    print(f"{options[3]}|{options[4]}|{options[5]}")
    print('-+-+-')
    print(f"{options[6]}|{options[7]}|{options[8]}")
    print()

def match_options(player_turn, selection, options):
    """Changes the number in the options list to the player's name. 

    Parameters
        player_turn: the of the current player. 
        selection: the number selected to be replaced.
        options: the list of movements made by the players. 
    """
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

def match_win(game):
    """Decides who won the game. 

    Parameters
        game: the current game. 
    """
    return (game[0] == game[1] == game[2] or
            game[3] == game[4] == game[5] or
            game[6] == game[7] == game[8] or
            game[0] == game[3] == game[6] or
            game[1] == game[4] == game[7] or
            game[2] == game[5] == game[8] or
            game[0] == game[4] == game[8] or
            game[2] == game[4] == game[6])

if __name__ == "__main__":
    main()