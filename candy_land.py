def create_board():
    '''
    This function creates a list of positions/spots for the candy land game.
    '''
    board = [] # Initialize a list for board
    colors = ('R', 'P', 'Y', 'B', 'O', 'G') * 23 # Calculated from 134 possible positions total in board
    special_spots = ('CC', 'IC', 'JO', 'GP', 'LP', 'PS', 'BB', 'MC')
    wild_spots = ('LI', 'BS60', 'BS41')



    for i in range(134):
        # Hard coded special/wild spots depending on index
        if i == 9:
            board.append(special_spots[0])
        elif i == 4:
            board.append(wild_spots[1])
        elif i == 20:
            board.append(special_spots[1])
        elif i == 29:
            board.append(wild_spots[2])
        elif i == 42:
            board.append(special_spots[2])
        elif i == 45:
            board.append(colors[i]+wild_spots[0])
        elif i == 69:
            board.append(special_spots[3])
        elif i == 76:
            board.append(colors[i]+wild_spots[0])
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
            board.append(colors[i])
    return board

def main():
    print(create_board())
    print(len(create_board()))

if __name__ == "__main__":
    main()
    