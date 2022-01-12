def main():
    action = " "
    turn = True
    player = "X"
    x_player_selection = [ ]
    o_player_selection = [ ]
    options = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while action != False:
        action = int(input(f"{player}'s turn. Please select a number 1-9: "))
        if turn == True:
            player = "O"
            x_player_selection.append(action)
            turn = False
        elif turn == False:
            player = "X"
            o_player_selection.append(action)
            turn = True

        for selection in x_player_selection:
            print (f'X selection: {selection}')
            for option in options:
                if option == selection:
                    options[selection - 1] = "X"
                # option = "X"
        for selection in o_player_selection:
            print (f'O Selection: {selection}')
            for option in options:
                if option == selection:
                    options[selection - 1] = "O"
                # option = "O"
        match = (f'Match: \
            \n{options[0]}|{options[1]}|{options[2]} \
            \n-+-+- \
            \n{options[3]}|{options[4]}|{options[5]} \
            \n-+-+- \
            \n{options[6]}|{options[7]}|{options[8]}')
        yes = match_win(match, player, options, action)
        print (f'{yes}')
        action = yes

def match_win(match, player, options, action):
    winner_board = (f'Match: \
            \nX|X|X \
            \n-+-+- \
            \n{options[3]}|{options[4]}|{options[5]} \
            \n-+-+- \
            \n{options[6]}|{options[7]}|{options[8]}')
            
    if match == winner_board:
        print(f'Congratulations, {player} you win.')
        action = False
        print(f'{match}')
        return action
    else:
        action = True
        print(f'{match}')
        return action
        

if __name__ == "__main__":
    main()