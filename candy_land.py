import candy_land_card

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

def take_turn(player, board, deck):
    
    player_color, player_location = player # Unpack the player tuple passed into this function

    card_type, card_color, card_name = candy_land_card.draw(deck) # Draw a card from the deck passed into this function using the candy_land_card module and unpack it

    print("Card type:", card_type, "Card color:", card_color)

    if card_type == 1:
        for i in range(player_location, len(board)):
            # print(board[i][0])
            if board[i][0] == card_color:
                player_location = i
                break
        else:
            player_location = 134 # If no color matches after iterating over possible matches, then assume that player wins (MC)
    elif card_type == 2:
        count = 0 # Initialize counter
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

    # If board location contains 'BS..', it will automatically go ahead skip them to new index

    if board[player_location][1:] == 'BS60':
        player_location = 60
    elif board[player_location][1:] == 'BS41':
        player_location = 41
    
    print(player_location)

    return player_location # Lastly return the player tuple with the updated value



def main():
    board = create_board()
    shuffled_deck = candy_land_card.shuffle(candy_land_card.make_deck())
    print(take_turn(['B', 0], board, shuffled_deck))

if __name__ == "__main__":
    main()
    