import candy_land_card

loose_turn_arr = []

def create_board():
    '''
    This function creates a list of positions/spots for the candy land game.
    '''
    board = ['START'] # Initialize a list for board
    colors = ('R', 'P', 'Y', 'B', 'O', 'G') * 23 # Calculated from 134 possible positions total in board
    special_spots = ('CC', 'IC', 'JO', 'GP', 'LP', 'PS', 'BB', 'MC')
    wild_spots = ('LI', 'BS60', 'BS41')
    



    for i in range(134):
        # Hard coded special/wild spots depending on index
        index_offset = i-1
        if i == 0:
            continue
        elif i == 9:
            board.append(special_spots[0])
        elif i == 4:
            board.append(colors[index_offset]+wild_spots[1])
        elif i == 20:
            board.append(special_spots[1])
        elif i == 29:
            board.append(colors[index_offset]+wild_spots[2])
        elif i == 42:
            board.append(special_spots[2])
        elif i == 45:
            board.append(colors[index_offset]+wild_spots[0])
        elif i == 69:
            board.append(special_spots[3])
        elif i == 76:
            board.append(colors[index_offset]+wild_spots[0])
        elif i == 92:
            board.append(special_spots[4])
        elif i == 102:
            board.append(special_spots[5])
        elif i == 117:
            board.append(special_spots[6])
        elif i == 133:
            board.append(special_spots[7])
        else:
            # Otherwise append normally based on the index given, matching the color in list
            board.append(colors[index_offset])
    return board

def loose_turn(player_color):
    loose_turn_arr.append(player_color)

def take_turn(player, board, deck):
    
    player_color, player_location = player # Unpack the player list passed into this function

    card_type, card_color, card_name = candy_land_card.draw(deck) # Draw a card from the deck passed into this function using the candy_land_card module and unpack it

    print("Player", player_color, "drew a", card_name, "card.")

    # Checks if any current player calling this function has loose turn status
    if len(loose_turn_arr) > 0:
        for i in range(len(loose_turn_arr)):
            if loose_turn_arr[i] == player_color:
                loose_turn_arr.pop(i)
                return

    # Checks if the card type is single or double, then loops through available color match of given amount of move
    if card_type == 1:
        for i in range(player_location, len(board)):
            if board[i][0] == card_color:
                player_location = i
                break
        else:
            player_location = 134 # If no color matches after iterating over possible matches, then assume that player wins (MC)
    elif card_type == 2:
        count = 0 # Initialize counter for double move
        for i in range(player_location, len(board)):
            if board[i][0] == card_color and count == 1:
                player_location = i
                break
            elif board[i][0] == card_color:
                count += 1
        else:
            player_location = 134 # If no color matches after iterating over possible matches, then assume that player wins (MC)
    else:
        player_location = card_type # Otherwise change player's location to special card's location

    # If board location contains 'BS..', it will automatically go ahead skip them to new index or 'LI', will loose turn too
    if board[player_location][1:] == 'BS60':
        player_location = 60
        print("Player", player_color, "took a shortcut!")
    elif board[player_location][1:] == 'BS41':
        player_location = 41
        print("Player", player_color, "took a shortcut!")
    elif board[player_location][1:] == 'LI':
        loose_turn(player_color)

    player[1] = player_location

    return player[1] # Lastly return the player's index with the updated value

def play_game(num_players):

    board = create_board()
    deck = candy_land_card.shuffle(candy_land_card.make_deck())

    if num_players > 6 or num_players < 0:
        print("Invalid num of players")
        return
    
    colors = ('R', 'P', 'Y', 'B', 'O', 'G')
    players = []
    
    for i in range(num_players):
        create_player = [colors[i], 0]
        players.append(create_player)

    current_player_index = 0

    while current_player_index >= 0:
        
        # Reset current player to 0 if it has reached to to end of number of players
        if current_player_index >= (len(players)-1):
            current_player_index = 0

        current_player = players[current_player_index]

        player_result = take_turn(current_player, board, deck)

        if player_result == 134:
            print("Player", players[current_player_index], "has won the game!")
            return
        else:
            print("Player", players[current_player_index], "has landed on", board[current_player[1]][0])
            current_player_index += 1



def main():
    play_game(2)

if __name__ == "__main__":
    main()
    