import random

def make_deck():
    '''
    This function creates and returns a deck of cards containing all of the cards
    '''

    card_colors = ('R', 'P', 'Y', 'B', 'O', 'G') # Designates all available colors
    
    deck = [] # Initialize card deck
    
    # Create 6 times every loop is done given a color range (single move cards)
    for _ in range(6):
        # Create single move cards
        for color in card_colors:
            create_card = (1, color, "S"+color)
            deck.append(create_card)
    
    # Create 4 times every loop is done given a color range (double move cards)
    for _ in range(4):
    # Create double move cards
        for color in card_colors:
            create_card = (2, color, "D"+color)
            deck.append(create_card)
    
    card_specials = ((9, 'X', "CC"), (20, 'X', "IC"), (42, 'X', "JO"), (69, 'X', "GP"), (92, 'X', "LP"), (102, 'X', "PS"), (117, 'X', "BB"))

    # Append all of the card specials to the deck
    for card in card_specials:
        deck.append(card)
    
    return deck # Return the deck

def shuffle(a_deck):
    '''
    This function shuffles cards in a deck and returns a shuffled deck
    '''
    for index in range(len(a_deck)):
        selected = random.randrange(0, len(a_deck)) # Selects a random index
        a_deck[index] = a_deck[selected] # Change at the given index value with the new random index value
    return a_deck # Return shuffled deck

def draw(a_deck):
    '''
    This function picks a card out of the deck and returns it
    '''
    # Guard clause, returns None if a passed deck is empty
    if len(a_deck) == 0:
        return None
    
    picked_card = a_deck.pop() # Pops a card out of the deck, and stores it in picked_card variable

    return picked_card # Return picked_card variable
    
    